from django.urls import path, include
from . import views

from .views import RegistroUsuario, UserList

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),
]
