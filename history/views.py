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
from history.models import *
from cashflow.models import *
from django.views.decorators.csrf import csrf_exempt
from .forms import HistoryForm

@login_required(login_url='/login')
def show_history(request):
    context = {}
    form = HistoryForm(request.POST or None)
    context['form']= form
    # if form.is_valid():
    #     budgetType= form.cleaned_data.get("budget_type")
    #     monthInput= form.cleaned_data.get("month_field")
    return render(request, "history.html", context)

@login_required(login_url='/login')
@csrf_exempt
def add_history(request):
    if request.method == 'POST':
        budgetType = request.POST.get('budget_type')
        monthInput = request.POST.get('month_field')
        amount = request.POST.get('amount')

        budgetHistory.objects.filter(user=request.user, month=monthInput).delete()
        new_history = budgetHistory.objects.create(budget_type = budgetType, totalAmount = amount, month = monthInput, user=request.user,)
        new_history = {
            'pk' : new_history.pk,
            'fields':{
                'budget_type':new_history.budget_type,
                'totalAmount':new_history.totalAmount,
                'month':new_history.month,
            }
        }
        return JsonResponse(new_history);

@login_required(login_url='/login')
def show_json_history(request):
    data = budgetHistory.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json",data), content_type="application/json")

