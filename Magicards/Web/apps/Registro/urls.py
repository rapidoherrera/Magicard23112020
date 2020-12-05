from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [   
    #listar las cuentas de la bd
    path('listarCuentas', views.listar_cuentas, name=""),

    # agregar una cuenta    
    path('agregar_cuenta', views.agregar_cuenta, name="agregar_cuenta"),

    # editar una cuenta
    path('editar_cuenta/<int:cuenta_id>', login_required(views.editar_cuenta), name="editar_cuenta"),

    # borrar una carrera
    path('borrar_cuenta/<int:cuenta_id>', login_required(views.borrar_cuenta), name="borrar_cuenta"),

    
    path('add_cuenta', views.CuentaCreate.as_view(), name="add_cuenta"),

    path('list_cuenta/', views.CuentaList.as_view(), name='list_cuenta'),


    path('edit_cuenta/<int:pk>', views.CuentaUpdate.as_view(), name='edit_cuenta'),

    path('del_cuenta/<int:pk>', views.CuentaDelete.as_view(), name='del_cuenta'),


]
