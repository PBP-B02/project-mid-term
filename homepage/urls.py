from unicodedata import name
from django.urls import path
from homepage.views import homepage_article
from homepage.views import show_json
from homepage.views import homepage_landingpage


urlpatterns = [
    path('homepage', homepage_article, name='homepage-article'),
    path('json', show_json, name = 'show_json'),
    path('', homepage_landingpage, name = 'homepage_landingpage'),
    
] 