from django.urls import path, include
from . import views

urlpatterns = [   
    # 127.0.0.1:8000/
    path('', views.index),

    path('acerca', views.acerca, name='acerca'),
    path('contacto', views.contacto, name='contacto'),
    path('recibedatos', views.recibedatos, name='recibedatos'),
    path('cliente/new', views.cliente_new, name='cliente_new'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    
    #del proyecto
    path('index/', views.index, name='index'),


    # localhost:8000/blanca/blanca.html
    path('blanca', views.pagina_blanca, name='pagina_blanca'),
    
    # localhost:8000/diccionario/diccionario.html
    path('diccionario', views.pagina_diccionario, name='pagina_diccionario'),
    
    # localhost:8000/post/numero_de_la_pk
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # localhost:8000/post/new
    path('post/new', views.post_new, name='post_new'),
    
    # localhost:8000/post/numero_de_la_pk/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    #del proyecto
    
    
]


