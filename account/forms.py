from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username", 
                "class": "form-control",
                "id": "username",
                "name": "username"
            }
        )
    )

    password = forms.CharField(
        label="Password",
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password", 
                "class": "form-control",
                "id": "password",
                "name": "password"
            }
        )
    )


class SignupForm(UserCreationForm):

    ROLE_CHOICES = [
        ('regular', 'Regular'),
        ('writer', 'Writer'),
    ]

    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "id": "username"
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                "id": "email"
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        label="Password Confirmation",
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control"
            }
        )
    )

    role_choice = forms.CharField(
        label="Saya adalah", widget=forms.RadioSelect(choices=ROLE_CHOICES)
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role_choice')