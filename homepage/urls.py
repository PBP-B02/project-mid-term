from unicodedata import name
from django.urls import path
from homepage.views import homepage_article
from homepage.views import show_json
from homepage.views import homepage_landingpage, homepage_cashflow
from homepage.views import article_bookmark, show_bookmark

app_name = 'landingpage'

urlpatterns = [
    path('', homepage_landingpage, name = 'homepage_landingpage'),
    path('homepage-article/', homepage_article, name='homepage-article'),
    path('homepage-cashflow/', homepage_cashflow, name='homepage-cashflow'),
    path('json/', show_json, name = 'show_json'),
    path('bookmark/<int:id>', article_bookmark, name= 'article_bookmark'),
    path('mybookmark/', show_bookmark, name= 'show_bookmark'),
    
] 