from django.urls import path # importamos las url generales
from ventas import views # importamos la vistas 
from .views import acceso_stripe,checkout # importamos del archivo views estas funciones especificas 


app_name="ventas"

#Aqui configura las rutas esto se ra importante por la navegacion 

urlpatterns = [
    path('', views.home,name='home'), 
    path('categorias/<slug>', views.categorias,name='categorias'),
    path('search/', views.search,name='search'),
    path('<slug>/', views.detail,name='detail'),
    path('test/',acceso_stripe,name='test'),
    path('checkout',checkout,name='checkout'),
    path('cart/add/<id>',views.cart_add,name='cart_add')
]