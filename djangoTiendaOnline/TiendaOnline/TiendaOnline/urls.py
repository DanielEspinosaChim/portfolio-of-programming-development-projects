"""
URL configuration for TiendaOnline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path #esto es para que se pueda usar la funcion path
from gestionpedidos import views #esto es para que se pueda usar la funcion busquefrom gestionpedidos.views import busqueda_productosda_productos


urlpatterns = [
    path('admin/', admin.site.urls),
    path("busqueda_productos/", views.busqueda_productos),
    path("buscar/", views.buscar),
    path("contacto/", views.contacto),#esto es para que se pueda acceder a la pagina de contacto el views.contacto es para que se pueda acceder a la funcion contacto de views.py
]
