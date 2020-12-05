from django.shortcuts import render, redirect
from .models import Cuenta
from .forms import CuentaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def listar_cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request, "Registro/listar_cuentas.html", {'cuentas': cuentas})

def agregar_cuenta(request):
    if request.method == "POST":
        form = CuentaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_cuenta")
    else:
        form = CuentaForm()
        return render(request, "Registro/agregar_cuenta.html", {'form': form})

def borrar_cuenta(request, cuenta_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Cuenta.objects.get(id=cuenta_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_cuentas')

def editar_cuenta(request, cuenta_id):
    # Recuperamos la instancia de la carrera
    instancia = Cuenta.objects.get(id=cuenta_id)

    # Creamos el formulario con los datos de la instancia
    form = CuentaForm(instance=instancia)

    if request.method == "POST":
 
        form = CuentaForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()

    return render(request, "Registro/editar_cuenta.html", {'form': form})

class CuentaCreate(CreateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'Registro/cuenta_form.html'
    success_url = reverse_lazy("listar_cuentas")
    
class CuentaList(ListView):
    model = Cuenta
    template_name = 'Registro/list_cuenta.html'
    # paginate_by = 4

class CuentaUpdate(UpdateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = 'Registro/cuenta_form.html'
    success_url = reverse_lazy('list_cuenta')

class CuentaDelete(DeleteView):
    model = Cuenta
    template_name = 'Registro/cuenta_delete.html'
    success_url = reverse_lazy('list_cuenta')

def figuras(request):
    return render(request, 'figuras.html', {}) 

def mangas(request):
    return render(request, 'mangas.html', {})
        
def comics(request):
    return render(request, 'comics.html', {})





