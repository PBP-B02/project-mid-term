from article.views import show_artikel
from article.views import tambah_artikel
from article.views import delete_artikel
from article.views import get_artikel_json
from django.urls import path


app_name = 'article'

urlpatterns = [
    path('',show_artikel, name='show_artikel'),
    path('tambah-artikel/',tambah_artikel,name='tambah-artikel'),
    path('delete-artikel/<int:id>/',delete_artikel,name='delete-artikel'),
    path('json/', get_artikel_json,name='get-artikel-json'),
]