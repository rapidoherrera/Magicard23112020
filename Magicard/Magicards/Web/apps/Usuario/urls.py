from django.urls import path, include
from . import views

from .views import RegistroUsuario, UserList

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar_usuario', UserList.as_view(), name="list_user"),
    path('add_usuario/', views.RegistroUsuario.as_view(), name='add_usuario'),
    path('edit_usuario/<int:pk>', views.UsuarioUpdate.as_view(), name='edit_usuario'),
    path('del_usuario/<int:pk>', views.UsuarioDelete.as_view(), name='del_usuario'),
    path('<int:pk>', views.User, name='Usuarios'),
    path('catalogo/', views.UserList.as_view(), name='catalogo'), 
   

]
