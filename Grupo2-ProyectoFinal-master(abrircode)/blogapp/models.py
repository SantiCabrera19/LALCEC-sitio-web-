from django.db import models
# Create your models here.
from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm # esto son los formularios que nos da django
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    class Meta :
        model = User
        fields =['first_name', 'last_name','email','username', 'password1', 'password2']