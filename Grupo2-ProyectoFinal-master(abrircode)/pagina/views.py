# Create your views here.
from pickle import FALSE
from poplib import POP3_SSL_PORT
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Post

def index(request):
    return render(request, "pagina/index.html")

def index1(request):
    return render(request, "pagina/index1.html")

def index2(request):
    return render(request, "pagina/index2.html")

def index3(request):
    return render(request, "pagina/index3.html")

def index4(request):
    return render(request, "pagina/index4.html")

def index5(request):
    return render(request, "pagina/index5.html")

def index6(request):
    return render(request, "pagina/index6.html")

def index7(request):
    posts = Post.objects.filter(estado = True)
    print(Post)
    return render(request, "pagina/indexpost.html",{"posts":posts})

def detallePost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    print(post)
    render(request, "post.html")
