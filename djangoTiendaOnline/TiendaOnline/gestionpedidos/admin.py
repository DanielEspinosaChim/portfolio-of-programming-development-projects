from django.contrib import admin#esto es para agregar tablas al panel de administrador de django

# Register your models here.
# from gestionpedidos.models import Clientes, Articulos, Pedidos
from gestionpedidos.models import Clientes#esto es importar las tablas que se crearon en models.py
from gestionpedidos.models import Articulos, Pedidos #tambien se pueden hacer asi osea dos a la vez
class ClientesAdmin(admin.ModelAdmin):#esto es para que en el panel de administrador de django se muestre mas informacion de la tabla
    list_display=("nombre","direccion","telefono")#esto es para que se muestre mas informacion de la tabla y le pones de parametro el nombre de los campos que quieres que se muestren que son las variables que pusiste em models.py
    search_fields=("nombre","telefono")#esto es para que se pueda buscar por nombre y telefono
    
class ClientesArticulos(admin.ModelAdmin):#esto es para que en el panel de administrador de django se muestre mas informacion de la tabla
    list_display=('nombre','seccion','precio')#esto es para que se muestre mas informacion de la tabla y le pones de parametro el nombre de los campos que quieres que se muestren que son las variables que pusiste em models.py
    search_fields=("nombre","seccion","precio")#que se pueda buscar por nombre, seccion y precio
    list_filter=("seccion", )#esto es para que se pueda filtrar por seccion
    
    
class PedidosAdmin(admin.ModelAdmin):#esto es para que en el panel de administrador de django se muestre mas informacion de la tabla
    list_display=('numero','fecha',)
    list_filter=('fecha',)#esto es para que se pueda filtrar por fecha
    date_hierarchy="fecha"#esto es para que se pueda filtrar por fecha pero con jerarquia

admin.site.register(Clientes, ClientesAdmin) #esto es para que se registren las tablas en el panel de administrador de django
admin.site.register(Articulos,ClientesArticulos)
admin.site.register(Pedidos, PedidosAdmin)#esto es para que se registren las tablas en el panel de administrador de django