from django.urls import path

from comment.views import home
from comment.views import post_single

app_name = 'blog'

urlpatterns = [
    path('', home, name='homepage'),
    path('<slug:post>/', post_single, name='post_single'),
]