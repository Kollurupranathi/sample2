"""project1 URL Configuration

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
from tkinter.font import names
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.que,name="que"),
    path('answer/',views.answer, name="answer"),
    path('login/',views.login, name="login"),
    path('loginn/',views.login, name="login"),
    path('logged/',views.logged, name="logged"),
    path('dashBoard/',views.dashBoard, name="dashBoard")
  
]
