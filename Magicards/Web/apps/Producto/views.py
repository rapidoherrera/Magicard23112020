from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.


# Producto

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Productos/producto_form.html'
    success_url = reverse_lazy("listar_producto")

class ProductoList(ListView):
    model = Producto
    template_name = 'Productos/catalogo.html'
    # paginate_by = 4

class ProductoList2(ListView):
    model = Producto
    template_name = 'Productos/listar_producto.html'
    # paginate_by = 4

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Productos/producto_form.html'
    success_url = reverse_lazy('listar_producto')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Productos/producto_delete.html'
    success_url = reverse_lazy('listar_producto')
from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.


# Producto

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Productos/producto_form.html'
    success_url = reverse_lazy("listar_producto")

class ProductoList(ListView):
    model = Producto
    template_name = 'Productos/catalogo.html'
    # paginate_by = 4

class ProductoList2(ListView):
    model = Producto
    template_name = 'Productos/listar_producto.html'
    # paginate_by = 4

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Productos/producto_form.html'
    success_url = reverse_lazy('listar_producto')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Productos/producto_delete.html'
    success_url = reverse_lazy('listar_producto')
