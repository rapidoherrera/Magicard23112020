from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Cliente
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import ClienteForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

def index(request):
    return render(request, 'blog/index.html', {})

def acerca(request):
    return render(request, 'blog/acerca.html', {})

def contacto(request):
    return render(request, 'blog/contacto.html', {})

def recibedatos(request):
    return render(request, 'blog/recibedatos.html', {})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'blog/cliente_detail.html', {'cliente': cliente})

def cliente_new(request):
    form = ClienteForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user 
            cliente.save()
            return redirect('cliente_detail', cliente.id)
    return render(request, 'blog/cliente_edit.html', {'form': form})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user 
            cliente.save()
            return redirect('cliente_edit', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'blog/cliente_edit.html', {'form': form})



def pagina_blanca(request):
    return render(request, 'blog/blanca.html', {})

def pagina_diccionario(request):
    # El siguiente es un QuerySet (conjunto de datos pareceido a SELECT * FROM POSTS)
    #posts = Post.objects.all()
    #sql_query = str(posts.query)
    #nombre_usuario = "Ana Torres"
    #edad_usuario = 26
    #cant_usuario = 101
    #contexto = {'posts': posts,
    #            'la_query':sql_query,
    #            'nombre_user':nombre_usuario,
    #            'edad_user':edad_usuario,
    #            'total_usuario':cant_usuario}
    
    # para enviar datos al templates debemos cargar estos valores en un diccionario python
    return render(request, 'blog/diccionario.html', contexto)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.id)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# Post edit con mensajes
# def post_edit(request, pk):
#     print("\nDENTRO DEL CONTROLADOR\n")
#     post = get_object_or_404(Post, pk=pk)
#     print("\n\n================= post_edit(entrando) =======================\n\n")
#     print(post.title)
#     print (request.user)
#     print(post)
#     print("=================================================================\n\n")
#     if request.method == "POST":
#         print("\nDENTRO DEL POST\n")
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             print("\nDENTRO DEL FORMULARIO VALIDO\n")
#             post = form.save(commit=False)
#             post.author = request.user 
#             # post.author = User.objects.get(id=1) # Otra alternativa es escoger un usuario específico
#             # post.author = User.objects.create('myusername', 'myemail@crazymail.com', 'mypassword') # Otra alternativa es crear un nuevo usuario
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#         print("\n\n=============== post_edit(cuan no es POST) ======================")
#         print("CUANDO NO ES POST")
#         print(form)
#         print(post)
#         print("\n\n=================================================================")
#     return render(request, 'blog/post_edit.html', {'form': form})