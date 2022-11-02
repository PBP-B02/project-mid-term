from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
import json
from validate_email import validate_email
from django.contrib import messages
from django.http import JsonResponse
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User


# Create your views here.
def register(response):
    
    if response.user.is_authenticated:
        messages.warning(response, 'You have to logout your account first!')
        return redirect("/")
    else:
        if response.method == "POST":
            form = SignupForm(response.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                selected = form.cleaned_data.get('role_choice')
                email = form.cleaned_data.get('email')

                if selected == 'regular':
                    login(response, user)
                    update_profile(username, selected, email)
                    messages.success(response, f'Welcome to CATFISH, { user.username }')
                    return redirect("/homepage-cashflow")
                elif selected == 'writer':
                    login(response, user)
                    update_profile(username, selected, email)
                    messages.success(response, f'Welcome to CATFISH, { user.username }')
                    return redirect("/homepage-article")

        else:
            form = SignupForm()

        return render(response, "signup.html", {"form": form})

def update_profile(user_username, user_role, email):
    user = (User.objects.get(username=user_username)).profile
    user.role = user_role
    user.email = email
    user.save()

def login_view(request):

    if request.user.is_authenticated:
        messages.warning(request, 'You have to logout your account first!')
        return redirect("/")
    else:
        if request.method == "POST":
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user.profile.role == 'regular':
                    login(request, user)
                    return redirect("/homepage-cashflow")
                if user.profile.role == 'writer':
                    login(request, user)
                    return redirect("/homepage-article")
        else:
            form = LoginForm()

        return render(request, "login.html", {"form": form})

class ValidateLoginUsername(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_valid': 'Username terdaftar'})
        return JsonResponse({'username_error': False})

def logout_view(response):
    logout(response)
    return redirect("/")

class ValidateUsername(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username hanya mengandung alphanumeric'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Username sudah terdaftar'}, status=409)
        return JsonResponse({'username_valid': True})

class ValidateEmail(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email tidak valid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email sudah terdaftar'}, status=409)
        return JsonResponse({'email_valid': True})
