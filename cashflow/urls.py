from django.urls import path
from cashflow.views import *

app_name = 'cashflow'

urlpatterns = [   
    path('', show_cashflow, name='show_cashflow'),
    path('my-income/', show_my_income, name='show_my_income'),
]