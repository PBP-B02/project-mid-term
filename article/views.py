from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from article.models import Artikel 
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.models import User
from article.forms import FormArtikel


# Create your views here.

@csrf_exempt
def show_artikel(request):
    form = FormArtikel()
    context = {
        'form':form,
        'user':request.user,
        'last_login': request.COOKIES.get('last_login'),
    }
    
    if(request.user.profile.role == "writer"):
        return render(request,"article-write.html",context)
    else:
        return render(request,"article-reguler.html",context)

@csrf_exempt
def tambah_artikel(request):
        if request.method == "POST":
            judul = request.POST.get("judul")
            author= request.user
            konten = request.POST.get("konten")
            artikel = Artikel(judul=judul,author=author, konten=konten)
            artikel.save()
        return JsonResponse({"pk":artikel.pk, "fields":
            {
                "judul":artikel.judul,
                "konten": artikel.konten
            }})

@csrf_exempt
def delete_artikel(request,id):
    artikel = Artikel.objects.get(pk=id)
    artikel.delete()
    return redirect('article:show_artikel')


def get_artikel_json(request):
    artikel = Artikel.objects.all()
    return HttpResponse(serializers.serialize("json", artikel),content_type="application/json")

def get_artikel_json_by_id(request, id):
    artikel = Artikel.objects.get(pk=id)
    return HttpResponse(serializers.serialize('json', [artikel]), content_type='application/json')

def get_artikel_by_id(request, id):
    artikel = Artikel.objects.get(pk=id)
    context = {
        'artikel': artikel
    }
    return render(request, 'artikel-id.html', context)




        
    



