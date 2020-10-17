"""django_app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import re_path
from firstapp import views

urlpatterns = [
    path('', views.homePage),
    path('recordStep/', views.recordStep1),
    path('recordStep/<int:specDocID>/', views.recordStep2),
    path('recordStep/<int:specDocID>/<int:docID>/', views.recordStep3),
    path('recordStep/<int:specDocID>/<int:docID>/<int:ticketID>/', views.recordStep4),

    path('createDoctor/', views.createDoctor),
    path('delDoctor/<int:docID>/', views.deleteDoctor),
    path('doctorAccount/<int:docID>/', views.doctorAccount),
    path('takePatient/<int:docID>/<int:patID>/', views.takePatient),

    path('createSpecDoctor/', views.createSpecDoctor),
    path('delSpecDoctor/<int:specDocID>/', views.delSpecDoctor),

    path('createTicket/', views.createTicket),
    path('delTicket/<int:ticketID>/', views.delTicket)
]

