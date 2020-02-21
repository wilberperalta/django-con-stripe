from django.db import models # libreria para el uso de modelos 
from autoslug import AutoSlugField # 
from django.contrib.auth.models import User # importamos las variable user para verificar que esten auntenticado 

class Categoria(models.Model): # se declara el modelo categoria 
    nombre = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='nombre')
    imagen = models.ImageField(upload_to='categorias',blank=True)
    descripcion =models.TextField(blank=True)
    destacado = models.BooleanField(default=False)
    activo= models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural='Categorias'
        
class Productos(models.Model): # se declra el modxelo productos 
    nombre = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='nombre')
    imagen = models.ImageField(upload_to='productos',blank=True)
    marca = models.CharField(max_length=250,blank=True)
    descripcion =models.TextField(blank=True)
    precio =models.DecimalField(max_digits=15,decimal_places=2,default=0.0)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    destacado = models.BooleanField(default=False)
    activo= models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural='Productos' 

class Carrusel(models.Model): # se Declara el modelo carrusel
    nombre = models.CharField(max_length=250)
    nombreclass = models.CharField(max_length=250, null=True)
    imagen = models.ImageField(upload_to='carrusel',blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural='Carrusel' 
# Create your models here.
