from django.urls import path
from ventas import views
from .views import acceso_stripe,checkout


app_name="ventas"

urlpatterns = [
    path('', views.home,name='home'),
    path('categorias/<slug>', views.categorias,name='categorias'),
    path('search/', views.search,name='search'),
    path('<slug>/', views.detail,name='detail'),
    path('test/',acceso_stripe,name='test'),
    path('checkout',checkout,name='checkout'),
    path('cart/add/<id>',views.cart_add,name='cart_add')
]