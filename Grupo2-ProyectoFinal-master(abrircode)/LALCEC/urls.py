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
from django.urls import path
from django.urls import include
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pagina import views

Namespace = 'pagina'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('mama/', views.index1),
    path('utero/', views.index2),
    path('colon/', views.index3),
    path('pulmon/', views.index4),
    path('piel/', views.index5),
    path('prostata/', views.index6),
    path('foro/', views.index7),
    path('detallePost/<slug:slug>/', views.detallePost, name='detalle_post'),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += staticfiles_urlpatterns()

