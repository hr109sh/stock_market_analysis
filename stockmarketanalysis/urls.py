from django.urls import path
from stockmarketanalysis import views

app_name = 'stockmarketanalysis'
urlpatterns = [
    path('stockmarketanalysis/',views.index,name = 'index'),
    path('opening/',views.opening,name = 'opening'),
    path('volume/',views.volume,name = 'volume'),
    path('adjacent_close/',views.adjacentclose,name = 'adjacent_close'),
    path('closing/',views.closing,name = 'closing'),
    path('high/',views.high,name = 'high'),
    path('low/',views.low,name = 'low'),
    path('contact/',views.contact,name = 'contact'),
    path('contact_message/',views.contact_message,name = "contact_message"),
    path('registration/',views.registration,name="registration"),
    path('user_registration/',views.user_registration,name="user_registration")
]
