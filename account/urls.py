from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name= 'login'),
    path('validate_username/', views.validate_username, name='validate_username'),
    path('validate_email/', views.validate_email, name='validate_email'),
    path('validate/',  views.validate, name='validate')
]