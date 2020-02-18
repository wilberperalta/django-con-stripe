from django.shortcuts import render
from ventas.models import Productos,Categoria,Carrusel
from django.http import JsonResponse
import stripe 
import json
stripe_pub='pk_test_WUeO3jo8reqCbEiYzWfYEOdJ00wwTqlQoQ'
stripe_private=	'sk_test_RVLLiJnQd4WXi6UIYK7hlGLA00BIefjdyS'
stripe.api_key=stripe_private;


def home(request):
    #Queryset api es un ORM
    productos=Productos.objects.filter(activo=True)
    categorias= Categoria.objects.filter(activo=True)
    banner=Carrusel.objects.all()
    
    context = {"productos":productos,"categorias":categorias,"images":banner}
    return render(request,"ventas/home.html",context)

def categorias(request,slug):
    cat =Categoria.objects.get(slug=slug)
    productos=Productos.objects.filter(activo=True,categoria=cat)
    categorias= Categoria.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias}
    return render(request,"ventas/list.html",context)

def search(request):
    #esto tomara el text input del formulario que esta en el archivo
    #base llamado q
    q = request.GET["q"]
    productos=Productos.objects.filter(activo=True,nombre__icontains=q)
    categorias= Categoria.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias}
    return render(request,"ventas/list.html",context)

"""def detail(request,slug):
    productos=Productos.objects.get(activo=True,slug=slug)
    categorias= Categoria.objects.filter(activo=True)
    context = {"product":productos,"categorias":categorias}
    return render(request,"ventas/detail.html",context)"""

#este es el primer checkout que se debe mostrar oara que devuelva 
#todos los datos de la carga = change

def acceso_stripe(request):
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
    return render (request,'ventas/exito.html')