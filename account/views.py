from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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

                login(response, user)
                update_profile(username, selected, email)
                messages.success(response, f'Welcome to CATFISH, { user.username }')
                return redirect("/")

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
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None :
                    login(request, user)
                    return redirect('/')
        else:
            form = LoginForm()

        return render(request, "login.html", {"form": form})

def validate(response):
    username1 = response.GET.get('username', None)
    password1 = response.GET.get('password', None)
    if (len(password1)<8 or len(username1)==0):
        return JsonResponse({"status":"fail"})
    else:
        return JsonResponse({"status":"ok"})

def logout_view(response):
    logout(response)
    return redirect("/")

def validate_username(response):
    username = response.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Username yang kamu gunakan tidak tersedia nih, coba yang lain ya!.'
    return JsonResponse(data)


def validate_email(response):
    email = response.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Email kamu sudah terdaftar, pakai email lain ya!'
    return JsonResponse(data)
