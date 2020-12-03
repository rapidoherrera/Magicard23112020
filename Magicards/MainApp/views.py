from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PersonaForm

def inicio(request):
    return render(request,'MainApp/inicio.html',{})

def quienessomos(request):
    return render(request,'MainApp/quienessomos.html', {})

def nuevousuario(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('login')
    else:
        form = PersonaForm()
    return render(request, 'MainApp/nuevo.html', {'form': form})