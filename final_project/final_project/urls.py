"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from fp2_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='index' ),
    path('home/', views.home, name='index'),
    path('course/', views.courseshow, name='course'),
    path('result/', views.result, name='result'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('automation/', views.automation, name='Automation'),
    path('autocad/', views.autocad, name='Autocad'),
    path('dm/', views.dm, name='DM'),
    path('ds/', views.ds, name='DS_AI'),
    path('embedded/', views.embedded, name='Embedded'),
    path('java/', views.java, name='JavaFS'),
    path('plc/', views.plc, name='PLC'),
    path('python/', views.python, name='python'),
    path('registration',views.register, name='registration')
]

