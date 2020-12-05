from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('conocenos', views.quienessomos, name='conocenos'),    
    path('registro', views.nuevousuario, name='nuevo'),
]