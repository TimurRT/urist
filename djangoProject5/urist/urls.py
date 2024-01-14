from django.urls import path
from .views import home, uslugi, prices, user_data_form, onas

urlpatterns = [
    path('', home, name='home'),
     path('uslugi/', uslugi, name='uslugi'),
     path('prices/', prices, name='prices'),
     path('userform/', user_data_form, name='user_form'),
     path('onas/', onas, name='onas'),
]
