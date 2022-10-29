
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import random;
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def show_cashflow(request):
    return render(request, "cashflow.html")

def show_my_income(request):
    return render(request, "my-income.html")

