from django.shortcuts import render
from .forms import RegistroForm
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User

# Create your views here.

# Usuario
class UserList(ListView):
    model = User
    template_name = 'Usuario/list_user.html'   

class UserList2(ListView):
    model = User
    template_name = 'Usuarios/list_user.html'
    # paginate_by = 4

# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home') 

class UsuarioCreate(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'Usuario/usuario_form.html'
    success_url = reverse_lazy("list_user")

class UsuarioUpdate(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = 'Usuario/usuario_form.html'
    success_url = reverse_lazy('list_user')

class UsuarioDelete(DeleteView):
    model = User
    template_name = 'Usuario/usuario_delete.html'
    success_url = reverse_lazy('list_user')
