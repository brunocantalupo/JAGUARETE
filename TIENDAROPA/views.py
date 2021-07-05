from django.contrib.auth.models import User
from django.contrib.auth import login as do_login, authenticate, logout as do_logout
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Carrito, Producto, Categoria
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    productos = Producto.objects.all().order_by('-fecha')
    primeros3 = productos[:3]
    categorias = Categoria.objects.all()
    return render(request, "home.html", {'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'productos':productos, 'categorias':categorias, 'primeros3': primeros3})

def render_Registrar(request):
    categorias = Categoria.objects.all()
    return render(request, "register.html", {'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'categorias':categorias})

def render_login(request):
    categorias = Categoria.objects.all()
    return render(request, "login.html", {'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'categorias':categorias})

def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        print (username)
        password = request.POST['password']
        print (password)
        user = User.objects.filter(username=username, password=password).first()
        print (user)
        if user is not None:
            do_login(request, user)
            return redirect('TIENDAROPA:index')
        else:
            print ("TIRA ERROR")
            return redirect('TIENDAROPA:login')

def logout(request):
    do_logout(request)
    return redirect('TIENDAROPA:login')

def register(request):
    if (request.method == "POST"):
        User.objects.create(username=request.POST['email'], first_name=request.POST["nombre"], last_name=request.POST["apellido"], email= request.POST["email"], password=request.POST["password"])
        user = User.objects.get(username = request.POST['email'])
        Carrito.objects.create(usuario=user, total=0)
        return redirect('TIENDAROPA:login')
    return redirect('TIENDAROPA:register')

def acercaDe(request):
    categorias = Categoria.objects.all()
    return render (request, "acercaDe.html", {'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'categorias':categorias})

def contacto(request):
    categorias = Categoria.objects.all()
    return render(request, "contacto.html", {'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'categorias':categorias})

def contactar(request):
    nombre = request.POST['nombre']
    email = request.POST['email']
    men = request.POST['body']
    mensaje = EmailMessage(
        subject='Mensaje de usuario',
        body=men,
        from_email=email,
        to=['jaguarete@gmail.com']
    )
    mensaje.content_subtype = 'html'
    mensaje.send()

def carrito(request):
    if not request.user.is_authenticated:
        return redirect ('TIENDAROPA:login')
    user = User.objects.get(username=request.user.username)
    carro = Carrito.objects.get(usuario=user.id)
    productos= carro.productos.all()
    categorias = Categoria.objects.all()
    productosPost = []
    if len(productos) > 0:
        for each in productos:
            productosPost.append({
                'id': Producto.objects.get(id=each.id).id,
                'nombre': Producto.objects.get(id=each.id).titulo,
                'descripcion': Producto.objects.get(id=each.id).descripcionProducto,
                'precio': Producto.objects.get(id=each.id).precio,
            })
    return render (request,"carrito.html", {
        'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'productos': productosPost , 'carrito': carro, 'categorias':categorias
    })

def listaProductos(request):
    if request.user.is_staff:
        productos=Producto.objects.all()
        categorias = Categoria.objects.all()
        productosPost = []
        for each in productos:
            productosPost.append({
                'id': each.id,
                'titulo': each.titulo,
                'descripcion': each.descripcionProducto,
                'precio': each.precio,
                'categoria': each.categoria
            })
        return render(request, 'listaProductos.html',{
            'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'productos':  productosPost, 'categorias':categorias
        })

def verProducto(request, id):
    producto = Producto.objects.get(id=id)
    categorias = Categoria.objects.all()
    productoPost = {
        'id': producto.id,
        'titulo': producto.titulo,
        'imagen': producto.imagen,
        'descripcion': producto.descripcionProducto,
        'precio': producto.precio,
        'categoria': producto.categoria
    }
    return render (request, "verProduto.html", {
        'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'producto': productoPost, 'categorias':categorias
    })

def agregarAlCarrito(request,id):
    if not request.user.is_authenticated:
        return redirect ('TIENDAROPA:login')
    user = User.objects.get(username=request.user.username)
    carro = Carrito.objects.get(usuario=user.id)
    producto = Producto.objects.get(id=id)
    carro.total = carro.total + producto.precio
    carro.productos.add(producto)
    carro.save()
    return redirect('TIENDAROPA:carrito')

def vaciarCarrito(request):
    user = User.objects.get(username=request.user.username)
    carro = Carrito.objects.get(usuario=user.id)
    carro.productos.clear()
    carro.total=0
    carro.save()  
    return redirect('TIENDAROPA:carrito')

def agregarProducto(request):
    if request.user.is_staff:
        categorias = Categoria.objects.all()
        return render (request,"agregarProducto.html", {'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'categorias':categorias})

def agregar(request):
    if request.user.is_staff:
        if request.method == 'POST':
            categoria=Categoria.objects.get(id=request.POST['categoria'])
            Producto.objects.create(titulo=request.POST['titulo'], imagen=request.POST['imagen'], descripcionProducto=request.POST['descripcion'], precio=request.POST['precio'], categoria=categoria)
            return redirect('TIENDAROPA:listaProductos')

def eliminarProducto(request,id):
    if request.user.is_staff:
        producto = Producto.objects.get(id=id)
        producto.delete()
        return redirect('TIENDAROPA:listaProductos')

def render_editar_producto(request,id):
    if request.user.is_staff:
        producto = Producto.objects.get(id=id)
        categorias = Categoria.objects.all()
        productoPost = {
            'id': producto.id,
            'titulo': producto.titulo,
            'imagen': producto.imagen,
            'descripcion': producto.descripcionProducto,
            'precio': producto.precio,
            'categoria': producto.categoria
        }
        return render (request, 'editarProducto.html',{'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'categorias':categorias, 'producto': productoPost})

def editarProducto(request,id):
    if request.user.is_staff:
        producto = Producto.objects.get(id=id)
        producto.delete()
        return redirect('TIENDAROPA:listaProductos')

def eliminarProductoDelCarrito(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        carro = Carrito.objects.get(usuario=user.id)
        producto = Producto.objects.get(id=id)
        carro.productos.remove(producto)
        carro.total = carro.total - producto.precio
        carro.save()
        return redirect('TIENDAROPA:carrito')

def verProductosDeCategoria(request,id):
    productos = Producto.objects.filter(categoria=id)
    categorias = Categoria.objects.all()
    productoPost = []
    for each in productos:
        productoPost.append({
            'id': each.id,
            'titulo': each.titulo,
            'descripcion': each.descripcionProducto,
            'precio': each.precio
        })
    return render (request,'verBusqueda.html',{'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'categorias':categorias, 'productos': productoPost})

def buscar(request):
    data = request.POST['busqueda']
    categorias = Categoria.objects.all()
    if data != ' ' or data != '':
        productos = Producto.objects.filter(titulo__contains=data) | Producto.objects.filter(descripcionProducto__contains=data)
        productoPost = []
        for each in productos:
            productoPost.append({
                'id': each.id,
                'titulo': each.titulo,
                'descripcion': each.descripcionProducto,
                'precio': each.precio
            })
        return render (request,'verBusqueda.html',{'ok': request.user.is_authenticated, 'tipo':request.user.is_staff, 'categorias':categorias, 'productos': productoPost})




