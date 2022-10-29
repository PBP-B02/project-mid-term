from django.urls import path
from cashflow.views import *

app_name = 'cashflow'

urlpatterns = [   
    path('', show_cashflow, name='show_cashflow'),
    path('my-income/', show_my_income, name='show_my_income'),
    path('my-spending/', show_my_spending, name='show_my_spending'),
    path('add-income/', add_income, name='add_income'),
    path('add-spending/', add_spending, name='add_spending'),
    path('delete-income/<int:id>', delete_income, name='delete_income'),
    path('json/income/', show_json_income, name='show_json_income'),
    path('json/income/<int:id>', show_json_income_by_id, name='show_json_income_by_id'),
    path('json/spending/', show_json_spending, name='show_json_spending'),
    path('json/spending/<int:id>', show_json_spending_by_id, name='show_json_spending_by_id'),
]