
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
import article

from homepage.models import Bookmark
from django.contrib import messages
from django.http import HttpResponse, request
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from .forms import NameArticle
from article.models import *
import datetime
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.


def homepage_landingpage(request):
      return render(request, 'homepage.html')

@login_required(login_url='/login')
def homepage_cashflow(request):
    articles = None
    form = NameArticle(request.GET)
    if form.is_valid() :
        articles = Artikel.objects.filter(judul__contains = form.cleaned_data["article"])
    else:
        articles = Artikel.objects.all()

    context = {
        'articles' : articles,
        'search_form' : form,
    }
    return render(request, 'homepage-cashflow.html', context)


@login_required(login_url='/login')
def homepage_article(request):
    articles = None
    form = NameArticle(request.GET)
    if form.is_valid() :
        articles = Artikel.objects.filter(judul__contains = form.cleaned_data["article"])

    else:
        articles = Artikel.objects.all()

    context = {
        'articles' : articles,
        'search_form' : form,
    }
    return render(request, 'homepage-article.html', context)
    
def article_bookmark(request, id):
    if request.method == 'POST':
        data = Artikel.objects.filter(pk=id)
        article_name = data.fields.judul

        new_bookmark = Bookmark.objects.create(user=request.user, title=article_name)
        return JsonResponse(new_bookmark)

def show_bookmark(request):
    bookmarks = Bookmark.objects.all()

    context = {
        'bookmarks' : bookmarks,
    }
    return render(request, 'bookmark.html', context)

# @csrf_exempt

def show_json(request):
    data = Bookmark.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


