from dataclasses import field
from unicodedata import name

from django.forms import forms
from django.shortcuts import render
from django.template import context
from django.contrib.auth.decorators import login_required
import article

from homepage.models import Search, Comment
from django.contrib import messages
from django.http import HttpResponse, request
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from .forms import NameArticle
from .filters import ListingFilter
from article.models import *
import datetime
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.


def homepage_landingpage(request):
      return render(request, 'homepage.html')

@login_required(login_url='/login')
def homepage_cashflow(request):
    article_name = request.POST.get('article_name')
    search_article = Artikel.objects.filter(judul=article_name)
    listing_filter = ListingFilter(request.GET, queryset = search_article)
    context = {
        'listing_filter' : listing_filter
    }
    return render(request, 'homepage-article.html', context)

# @login_required(login_url='/login')
def homepage_article(request):
    # comment = request.POST.get('comment')
    # article_name = request.POST.get('article_name')
    articles = None
    # search_article = Artikel.objects.filter(judul=article_name)
    form = NameArticle(request.GET)
    if form.is_valid() :
        articles = Artikel.objects.filter(judul__contains = form.cleaned_data["article"])

    else:
        articles = Artikel.objects.all()


    # listing_filter = ListingFilter(request.GET, queryset = search_article)
    context = {
        'articles' : articles,
        'search_form' : form,
    }
    return render(request, 'homepage-article.html', context)

@csrf_exempt
def add_search(request):
        if request.method == 'POST':
           article_name =  request.POST.get('article_name')
           new_search = Search.objects.create(user=request.user, article_name = article_name)
           new_search = {
               'pk' : new_search.pk,
               'field':{
                   'article_name':new_search.article_name,
               }
           }
        return JsonResponse(new_search)
    

def show_json(request):
    data = Search.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


