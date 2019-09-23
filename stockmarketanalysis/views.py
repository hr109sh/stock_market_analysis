# For division
from __future__ import division
from django.shortcuts import redirect,render
from  django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from stockmarketanalysis.models import contactForm

import pandas as pd
from pandas import Series,DataFrame
import numpy as np

# For reading stock data from yahoo
from pandas_datareader import data
# For time stamps
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# Create your views here.

tech_list = ['AAPL','GOOG','MSFT','AMZN']
end = datetime.now()
start = datetime(end.year - 1,end.month,end.day)
for stock in tech_list:
# Set DataFrame as the Stock Ticker
    globals()[stock] = data.DataReader(stock,'yahoo',start,end)


# Data for Apple
AAPL['Date'] = AAPL.index
AAPL_periods = AAPL.Date.dt.to_period("M")
AAPL_group = AAPL.groupby(AAPL_periods).mean()
AAPL_group['Date'] = AAPL_group.index
pd.options.display.float_format = '{:,.0f}'.format


# data for google
GOOG['Date'] = GOOG.index
GOOG_periods = GOOG.Date.dt.to_period("M")
GOOG_group = GOOG.groupby(GOOG_periods).mean()
GOOG_group['Date'] = GOOG_group.index
pd.options.display.float_format = '{:,.0f}'.format

# data for microsoft
MSFT['Date'] = MSFT.index
MSFT_periods = MSFT.Date.dt.to_period("M")
MSFT_group = MSFT.groupby(MSFT_periods).mean()
MSFT_group['Date'] = MSFT_group.index
pd.options.display.float_format = '{:,.0f}'.format

# data for Amazone
AMZN['Date'] = AMZN.index
AMZN_periods = AMZN.Date.dt.to_period("M")
AMZN_group = AMZN.groupby(AMZN_periods).mean()
AMZN_group['Date'] = AMZN_group.index
pd.options.display.float_format = '{:,.0f}'.format

# Create your views here.
@login_required
def index(request):
    return render(request,'stockmarketanalysis/index.html')

def registration(request):
    return render(request,'stockmarketanalysis/registration.html')

def user_registration(request):
    first_name = request.GET.get('first_name', None)
    last_name = request.GET.get('last_name', None)
    email = request.GET.get('email', None)
    password = request.GET.get('password', None)

    try:
        user = User.objects.create_user(username=email,
                                    email=email,
                                    password=password,
                                    first_name = first_name,
                                    last_name = last_name)
        data = {
            'message':1
        }
    except:
        data = {
            'message':0
            }
    return JsonResponse(data)

@login_required
def opening(request):
    AAPL_date = AAPL_group['Date'].values.tolist()
    AAPL_Open = AAPL_group['Open'].values.tolist()
    AAPL_Open = list(map(int, AAPL_Open))

    GOOG_date = GOOG_group['Date'].values.tolist()
    GOOG_Open = GOOG_group['Open'].values.tolist()
    GOOG_Open = list(map(int, GOOG_Open))

    MSFT_date = MSFT_group['Date'].values.tolist()
    MSFT_Open = MSFT_group['Open'].values.tolist()
    MSFT_Open = list(map(int, MSFT_Open))

    AMZN_date = AMZN_group['Date'].values.tolist()
    AMZN_Open = AMZN_group['Open'].values.tolist()
    AMZN_Open = list(map(int, AMZN_Open))

    data = {
        'AAPL_date':AAPL_date,
        'AAPL_Open':AAPL_Open,
        'GOOG_date':GOOG_date,
        'GOOG_Open':GOOG_Open,
        'MSFT_date':MSFT_date,
        'MSFT_Open':MSFT_Open,
        'AMZN_date':AMZN_date,
        'AMZN_Open':AMZN_Open
    }
    return render(request,'stockmarketanalysis/opening.html',context=data)

@login_required
def contact(request):
	return render(request,'stockmarketanalysis/contact.html')


@login_required
def adjacentclose(request):
    AAPL_date = AAPL_group['Date'].values.tolist()
    AAPL_adjcent_close = AAPL_group['Adj Close'].values.tolist()
    AAPL_adjcent_close = list(map(int, AAPL_adjcent_close))

    GOOG_date = GOOG_group['Date'].values.tolist()
    GOOG_adjcent_close = GOOG_group['Adj Close'].values.tolist()
    GOOG_adjcent_close = list(map(int, GOOG_adjcent_close))

    MSFT_date = MSFT_group['Date'].values.tolist()
    MSFT_adjcent_close = MSFT_group['Adj Close'].values.tolist()
    MSFT_adjcent_close = list(map(int, MSFT_adjcent_close))

    AMZN_date = AMZN_group['Date'].values.tolist()
    AMZN_adjcent_close = AMZN_group['Adj Close'].values.tolist()
    AMZN_adjcent_close = list(map(int, AMZN_adjcent_close))

    data = {
    'AAPL_date':AAPL_date,
    'AAPL_adjcent_close':AAPL_adjcent_close,
    'GOOG_date':GOOG_date,
    'GOOG_adjcent_close':GOOG_adjcent_close,
    'MSFT_date':MSFT_date,
    'MSFT_adjcent_close':MSFT_adjcent_close,
    'AMZN_date':AMZN_date,
    'AMZN_adjcent_close':AMZN_adjcent_close
    }
    return render(request,'stockmarketanalysis/adjacentclose.html',context =data)


@login_required
def volume(request):
    AAPL_date = AAPL_group['Date'].values.tolist()
    AAPL_volume = AAPL_group['Volume'].values.tolist()
    AAPL_volume = list(map(int, AAPL_volume))

    GOOG_date = GOOG_group['Date'].values.tolist()
    GOOG_volume = GOOG_group['Volume'].values.tolist()
    GOOG_volume = list(map(int, GOOG_volume))

    MSFT_date = MSFT_group['Date'].values.tolist()
    MSFT_volume = MSFT_group['Volume'].values.tolist()
    MSFT_volume = list(map(int, MSFT_volume))

    AMZN_date = AMZN_group['Date'].values.tolist()
    AMZN_volume = AMZN_group['Volume'].values.tolist()
    AMZN_volume = list(map(int, AMZN_volume))
    data = {
        'AAPL_date':AAPL_date,
        'AAPL_volume':AAPL_volume,
        'GOOG_date':GOOG_date,
        'GOOG_volume':GOOG_volume,
        'MSFT_date':MSFT_date,
        'MSFT_volume':MSFT_volume,
        'AMZN_date':AMZN_date,
        'AMZN_volume':AMZN_volume
    }
    return render(request,'stockmarketanalysis/volume.html',context =data)


@login_required
def closing(request):
    AAPL_date = AAPL_group['Date'].values.tolist()
    AAPL_Close = AAPL_group['Close'].values.tolist()
    AAPL_Close = list(map(int, AAPL_Close))

    GOOG_date = GOOG_group['Date'].values.tolist()
    GOOG_Close = GOOG_group['Close'].values.tolist()
    GOOG_Close = list(map(int, GOOG_Close))

    MSFT_date = MSFT_group['Date'].values.tolist()
    MSFT_Close = MSFT_group['Close'].values.tolist()
    MSFT_Close = list(map(int, MSFT_Close))

    AMZN_date = AMZN_group['Date'].values.tolist()
    AMZN_Close = AMZN_group['Close'].values.tolist()
    AMZN_Close = list(map(int, AMZN_Close))

    data = {
    'AAPL_date':AAPL_date,
    'AAPL_Close':AAPL_Close,
    'GOOG_date':GOOG_date,
    'GOOG_Close':GOOG_Close,
    'MSFT_date':MSFT_date,
    'MSFT_Close':MSFT_Close,
    'AMZN_date':AMZN_date,
    'AMZN_Close':AMZN_Close
    }
    return render(request,'stockmarketanalysis/closing.html',context=data)


@login_required
def high(request):
    AAPL_date = AAPL_group['Date'].values.tolist()
    AAPL_High = AAPL_group['High'].values.tolist()
    AAPL_High = list(map(int, AAPL_High))

    GOOG_date = GOOG_group['Date'].values.tolist()
    GOOG_High = GOOG_group['High'].values.tolist()
    GOOG_High = list(map(int, GOOG_High))

    MSFT_date = MSFT_group['Date'].values.tolist()
    MSFT_High = MSFT_group['High'].values.tolist()
    MSFT_High = list(map(int, MSFT_High))

    AMZN_date = AMZN_group['Date'].values.tolist()
    AMZN_High = AMZN_group['High'].values.tolist()
    AMZN_High = list(map(int, AMZN_High))

    data = {
    'AAPL_date':AAPL_date,
    'AAPL_High':AAPL_High,
    'GOOG_date':GOOG_date,
    'GOOG_High':GOOG_High,
    'MSFT_date':MSFT_date,
    'MSFT_High':MSFT_High,
    'AMZN_date':AMZN_date,
    'AMZN_High':AMZN_High
    }
    return render(request,'stockmarketanalysis/high.html',context=data)

@login_required
def low(request):
    AAPL_date = AAPL_group['Date'].values.tolist()
    AAPL_Low = AAPL_group['Low'].values.tolist()
    AAPL_Low = list(map(int, AAPL_Low))

    GOOG_date = GOOG_group['Date'].values.tolist()
    GOOG_Low = GOOG_group['Low'].values.tolist()
    GOOG_Low = list(map(int, GOOG_Low))

    MSFT_date = MSFT_group['Date'].values.tolist()
    MSFT_Low = MSFT_group['Low'].values.tolist()
    MSFT_Low = list(map(int, MSFT_Low))

    AMZN_date = AMZN_group['Date'].values.tolist()
    AMZN_Low = AMZN_group['Low'].values.tolist()
    AMZN_Low = list(map(int, AMZN_Low))

    data = {
    'AAPL_date':AAPL_date,
    'AAPL_Low':AAPL_Low,
    'GOOG_date':GOOG_date,
    'GOOG_Low':GOOG_Low,
    'MSFT_date':MSFT_date,
    'MSFT_Low':MSFT_Low,
    'AMZN_date':AMZN_date,
    'AMZN_Low':AMZN_Low
    }
    return render(request,'stockmarketanalysis/low.html',context=data)

@login_required
def contact_message(request):
    if request.method == 'POST':
        name_data = request.POST['name']
        email_data = request.POST['email']
        subject_data = request.POST['subject']
        message_data = request.POST['message']
        contactForm_data = contactForm(name =name_data,email=email_data,subject=subject_data,message=message_data )
        contactForm_data.save()
    return redirect('../contact/')
