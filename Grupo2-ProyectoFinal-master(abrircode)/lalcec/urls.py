"""lalcec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pagina import views


urlpatterns = [
    path('admin/', admin.site.urls, name='administrar'),
    path('', views.Home, name='inicio'),
    path('mama/', views.Mama, name = 'mama'),
    path('utero/', views.Utero, name = 'utero'),
    path('colon/', views.Colon, name = 'colon'),
    path('pulmon/', views.Pulmon, name = 'pulmon'),
    path('piel/', views.Piel, name = 'piel'),
    path('prostata/', views.Prostata, name = 'prostata'),
    path('foro/', views.listarPost.as_view(), name='lista_post'),
    path('post/<slug:url>/', views.DetallePost.as_view(), name='detalle_post'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile', views.profile),
]
urlpatterns += staticfiles_urlpatterns()

