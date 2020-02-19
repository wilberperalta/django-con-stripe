from django.shortcuts import render, redirect
from ventas.models import Productos, Categoria, Carrusel
from django.http import JsonResponse
import stripe
import json
stripe_pub = 'pk_test_UcvWnnOilQyzGZzXQsdnQv6K004zIkBU4w'
stripe_private = 'sk_test_ntuCZzWTNykAWb5LRqv7ss8d00qi3rzWIz'
stripe.api_key = stripe_private


def home(request):
    #Queryset api es un ORM
    productos = Productos.objects.filter(activo=True)
    categorias = Categoria.objects.filter(activo=True)
    banner = Carrusel.objects.all()
    #if(request.session.get('carrito','No')=='No'):
    #    request.session.get['carrito']=[]
    context = {"productos":productos,"categorias":categorias, "images":banner, "carrito":request.session['carrito']}
    return render(request,"ventas/home.html",context)
    
def categorias(request,slug):
    cat = Categoria.objects.get(slug=slug)
    productos= Productos.objects.filter(activo=True,categoria=cat)
    categorias = Categoria.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias, "only":cat, "carrito":request.session['carrito']}
    return render(request,"ventas/list.html",context)

def search(request):
    q = request.GET["q"]
    productos = Productos.objects.filter(activo=True,nombre__icontains=q)
    categorias = Categoria.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias}
    return render(request,"ventas/list.html",context)


def detail(request,slug):
    if Productos.objects.filter(activo=True,slug=slug).exists():
        productos=Productos.objects.get(activo=True,slug=slug)
        categorias= Categoria.objects.filter(activo=True)
        context = {"product":productos,"categorias":categorias,"carrito":request.session['carrito']}
        return render(request,"ventas/detail.html",context) 
    else:
        pass
    return render(request,"ventas/stripe.html")

#Este es el primer checkout que se debe mostrar
#para que devuelva todos los datos de la carpeta = char

def acceso_stripe(request):
    print("envio de informacion")
    print(request.POST)
    return render(request,"ventas/stripe.html",{'key':stripe_pub})
    
def checkout(request):
    amount= 1500
    customer =stripe.Customer.create(
        email= request.POST['stripeEmail'],
        source=request.POST['stripeToken']
    )
    
    charge =stripe.Charge.create(
        customer = customer.id,
        amount = amount,
        currency= 'aud',
        description='cursos en codigo'
    )
    #return render (request,'ventas/exito.html')
    
    #print("status, charge")
    return JsonResponse(charge)

# Create your views here.
def cart_add(request,id):
    obj = Productos.objects.get(pk=id)
    print(obj)
    prod = {
        "id":obj.id,
        "nombre":obj.nombre,
        "precio":23.00,
        "imagen":'demo',
        "cant":1
    }
    carrito = request.session['carrito']
    carrito.append(prod)
    request.session['carrito'] = carrito
    print(request.session['carrito'])
    return redirect('/')

def cart_list(request):
    carrito = request.session.get('carrito')
    print(carrito)
    return JsonResponse(carrito,safe=False)
    
    
    
    
    