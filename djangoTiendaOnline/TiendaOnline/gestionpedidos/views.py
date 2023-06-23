from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import Articulos
from django.core.mail import send_mail#impota la libreria que nos permite enviar correos
from django.conf import settings#esto es para que se pueda usar el email del usuario

# Create your views here.

def busqueda_productos(request):
     return render(request, "busqueda_productos.html")#esto es para que se muestre la pagina de busqueda_productos.html

def buscar(request):
     if request.GET["producto"]:#esto evaluara si se ha introducido algo en el campo de busqueda
          #mensaje="eh encontrado: %r" %request.GET["producto"]#esto es para que se muestre el mensaje de que se encontro el articulo
          producto=request.GET["producto"]#esto es para que se muestre el mensaje de que se encontro el articulo
          
          #return HttpResponse(mensaje)#esto es para que se muestre el mensaje de que se encontro el articulo 
          if len(producto)>20:#esto sirve para que no se pueda buscar un texto de mas de 20 caracteres
               return HttpResponse("El texto de búsqueda es demasiado largo.")#esto muestra un mensaje si el texto es mayor a 20 caracteres se usa el HttpResponse en lugar de la variable por mque el mensaje es demasiado largo
          else:#de lo contrario si el texto es menor a 20 caracteres
             articulos=Articulos.objects.filter(nombre__icontains=producto)#esto para que encuentre datos de la base de datos. el icontains es para que encuentre coincidencias en nla base de datos como el like de sql
             return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})#el query es para que se muestre el nombre del articulo que se busco este es el return de el primer if
     else:
          #mensaje="no haz introducido nada"
          #return HttpResponse(mensaje)
          return HttpResponse("No has introducido nada en el campo de búsqueda.")
     
def contacto(request):
     if request.method=="POST":#esto dice si rel request es igual a post  #post es para que se envie la informacion
        
        subject=request.POST["asunto"]#esto es para que se guarde el asunto que se escribio en el campo de asunto
        message=request.POST["mensaje"]+" "+request.POST["email"]#esto es para que se guarde el mensaje que se escribio en el campo de mensaje y el email
        email_from=settings.EMAIL_HOST_USER#esto es para que se guarde el email del usuario
        recipient_list=["luis111fdo5@gmail.com"]#esto es para que se guarde el email del destinatario
        send_mail(subject, message, email_from, recipient_list)#esto es para que se envie el mensaje
        return render(request, "gracias.html")
     
     return render(request, "contacto.html")#es para que se muestre la pagina de contacto.html

