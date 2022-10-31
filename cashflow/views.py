
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
from cashflow.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url='/login')
def show_cashflow(request):
    return render(request, "cashflow.html")

@login_required(login_url='/login')
def show_my_income(request):
    return render(request, "my-income.html")

@login_required(login_url='/login')
def show_my_spending(request):
    return render(request, "my-spending.html")

@login_required(login_url='/login')
def show_json_income(request):
    data = Income.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

@login_required(login_url='/login')
def show_json_income_by_id(request,id):
    data = Income.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

@login_required(login_url='/login')
def show_json_spending_by_id(request,id):
    data = Spending.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

@login_required(login_url='/login')
@csrf_exempt
def delete_income(request,id):
    if request.method == 'DELETE':
        Income.objects.filter(pk=id).delete()
        return HttpResponse(status=202)

@login_required(login_url='/login')
@csrf_exempt
def delete_spending(request,id):
    if request.method == 'DELETE':
        Spending.objects.filter(pk=id).delete()
        return HttpResponse(status=202)

@login_required(login_url='/login')
def show_json_spending(request):
    data = Spending.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

@login_required(login_url='/login')
@csrf_exempt
def add_income(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        income_type = request.POST.get('income_type')
        new_income = Income.objects.create(name = name, amount = amount, date = date, user=request.user, income_type=income_type)
        new_income = {
            'pk' : new_income.pk,
            'fields':{
                'name':new_income.name,
                'amount':new_income.amount,
                'date':new_income.date,
                'income_type':new_income.income_type
            }
        }
        return JsonResponse(new_income);

@login_required(login_url='/login')
@csrf_exempt
def add_spending(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        spending_type = request.POST.get('spending_type')
        new_spending = Spending.objects.create(name = name, amount = amount, date = datetime.date.today(), user=request.user, spending_type=spending_type)
        new_spending = {
            'pk' : new_spending.pk,
            'fields':{
                'name':new_spending.name,
                'amount':new_spending.amount,
                'date':new_spending.date,
                'spending_type':new_spending.spending_type
            }
        }
        return JsonResponse(new_spending);

def show_history(request):
    return render(request, 'history.html')
