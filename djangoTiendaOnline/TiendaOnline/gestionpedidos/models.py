from django.db import models

# Create your models here.
#aqui creas tus bases de datos

class Clientes(models.Model):
    nombre=models.TextField(max_length=30)#traducido esto crea una tabla en la base de datos con el metodo models de la case models, lo que esta despues del punto es el tipo de dato que recibe y como recibe texto se le pone la extencion
    direccion=models.CharField(max_length=50,blank=True,null=True)#el blank es para que no sea obligatorio llenar el campo y el null es para que no sea obligatorio llenar el campo en la base de datos
    email=models.EmailField(blank=True, null=True, verbose_name='la_direccion')#este es un metodo de la clase models que evalua que sea un correo valido. el verbose_name es para que en la base de datos se muestre con ese nombre
    telefono=models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre#este metodo es para que cuando se haga una consulta a la base de datos se muestre el nombre del cliente y no el id
    
class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()
    
    def __str__(self):
        return 'El nombre es %s, su seccion es %s, y su precio es %s'%(self.nombre,self.seccion, self.precio)
    #este metodo es para que cuando se haga una consulta a la base de datos se muestre el nombre del articulo y no el id
    
    
class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    
#estas teblas no las conoce el proyecto asi que dentro de settings debe estar siuuuuu