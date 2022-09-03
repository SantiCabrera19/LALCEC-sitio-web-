# Create your views here.
from pickle import FALSE
from poplib import POP3_SSL_PORT
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from django.views.generic import DetailView

def Home(request):
    return render(request, "pagina/Home.html")

def Mama(request):
    return render(request, "pagina/Mama.html")

def Utero(request):
    return render(request, "pagina/Utero.html")

def Colon(request):
    return render(request, "pagina/Colon.html")

def Pulmon(request):
    return render(request, "pagina/Pulmon.html")

def Piel(request):
    return render(request, "pagina/Piel.html")

def Prostata(request):
    return render(request, "pagina/Prostata.html")

def index7(request):
    posts = Post.objects.filter(estado = True)
    print(Post)
    return render(request, "pagina/indexpost.html",{"posts":posts})


class DetallePost(DetailView):
    """Detalle del  post."""
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'

def profile(request):
    return render(request, "pagina/account/profile.html")
