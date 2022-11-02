from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


app_name='account'

urlpatterns = [
    path('', views.login_view, name= 'login'),
    path('validate_username/', csrf_exempt(views.ValidateUsername.as_view()),
         name="validate_username"),
    path('validate_email/', csrf_exempt(views.ValidateEmail.as_view()),
         name="validate_email"),
    path('validate_login_username/', csrf_exempt(views.ValidateLoginUsername.as_view()),
         name="validate_login_username")
]