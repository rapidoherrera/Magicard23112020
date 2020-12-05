from django.urls import path, include
from . import views

urlpatterns = [

    #Productos
    path('catalogo/', views.ProductoList.as_view(), name='catalogo'),

    path('listar_producto/', views.ProductoList2.as_view(), name='listar_producto'),

    path('add_producto/', views.ProductoCreate.as_view(), name='add_producto'),

    path('edit_producto/<int:pk>', views.ProductoUpdate.as_view(), name='edit_producto'),

    path('del_producto/<int:pk>', views.ProductoDelete.as_view(), name='del_producto'),

    path('<int:pk>', views.Producto, name='Productos'),

]