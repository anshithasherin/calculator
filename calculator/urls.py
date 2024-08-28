"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from greetings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodmorning/',views.goodmorningview.as_view()),
    path('goodevening/',views.goodeveningview.as_view()),
    path('time/',views.todayview.as_view()),
    path('add/',views.addview.as_view()),
    path('sub/',views.substractview.as_view()),
    path('cube/',views.cubeview.as_view())

]

