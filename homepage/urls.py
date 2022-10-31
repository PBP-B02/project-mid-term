from unicodedata import name
from django.urls import path
from homepage.views import homepage_article
from homepage.views import show_json

urlpatterns = [
    path('', homepage_article, name='homepage-article'),
    path('json', show_json, name = 'show_json')
    
] 