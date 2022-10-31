from django.forms import forms
from django.shortcuts import render
from django.template import context
from homepage.forms import CreateComment
from homepage.models import Article_Cashflow
from django.contrib import messages
from django.http import HttpResponse, request
from django.core import serializers

import datetime

# Create your views here.


def homepage_landingpage(request):
     
      return render(request, 'homepage.html')

def homepage_article(request):
      comment_item = Article_Cashflow.objects.all()
      form = CreateComment()

      if request.method == "POST":
            # komentar = request.POST['komentar']

            # new_comment = CreateComment(comment_anonymous = komentar)
            # new_comment.save()
            form = CreateComment(request.POST)
            if form.is_valid():
                  new_form = form.save(commit=False)
                  new_form.instanace.user = request.user
                  new_form.save()
                  messages.success(request, 'Task telah berhasil dibuat!')

      context = {
            'comment_item' : comment_item,
            'form' : form,
      }

      return render(request, 'homepage-article.html', context)
      
def show_json(request):
    data = Article_Cashflow.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
