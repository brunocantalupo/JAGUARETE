from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth.views import LoginView,logout_then_login

app_name = "TIENDAROPA"
urlpatterns = [
    path('',views.index, name="index"),
    path('register/',views.render_Registrar, name="register"),
    path('registerUser/',views.register, name="registerUser"),
    path('login/',views.render_login,name='login'),
    path('loginUser/',views.login,name='loginUser'),
    path('logout/',views.logout,name='logout'),
    path('acercaDe/',views.acercaDe,name='acercaDe'),
    path('contacto/',views.contacto,name='contacto'),
    path('contactar/',views.contactar,name='contactar'),
    path('carrito/',views.carrito,name='carrito'),
    path('productos/',views.listaProductos,name='listaProductos'),
    path('verProducto/<id>/',views.verProducto,name='verProducto'),
    path('agregarAlCarrito/<id>/',views.agregarAlCarrito,name='agregarAlCarrito'),
    path('vaciarCarrito/',views.vaciarCarrito,name='vaciarCarrito'),
    path('agregarProducto/',views.agregarProducto,name='agregarProducto'),
    path('agregar/',views.agregar,name='agregar'),
    path('render_editar_producto/<id>/',views.render_editar_producto,name='render_editar_producto'),
    path('editarProducto/<id>',views.editarProducto,name='editarProducto'),
    path('eliminarProducto/<id>/',views.eliminarProducto,name='eliminarProducto'),
    path('eliminarProductoDelCarrito/<id>/',views.eliminarProductoDelCarrito,name='eliminarProductoDelCarrito'),
    path('verProductosDeCategoria/<id>/',views.verProductosDeCategoria,name='verProductosDeCategoria'),
    path('buscar/',views.buscar,name='buscar'),
    path('mostrarFoto/<id>/',views.mostrar_foto,name='mostrarFoto'),
]