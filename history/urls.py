from django.urls import path
from history.views import *

app_name = 'history'

urlpatterns = [
    path('', show_history, name='show_history'),
    path('add-history/', add_history, name='add_history'),
    path('json/', show_json_history, name='show_json_history'),
]
