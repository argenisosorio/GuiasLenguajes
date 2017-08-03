##### Guía Django Rest Framework by dM #####

##################
##### Teoría #####
##################

DRF Es una librería que nos permite construir un API REST sobre Django de forma sencilla. Ofreciendo una alta
gama de métodos y funciones para el manejo, definición y control de nuestros recursos.

##### Qué es un API REST #####

API, por sus siglas en inglés (Application Programming Interface). Básicamente, representan una colección
de métodos y funciones implementadas en un sistema con el fin de que las mismas sean utilizadas por otros.

A medida que surgieron APIs sobre aplicaciones y plataformas web, se fue formando el término API REST, el
cual se usa para denominar a las API que están implementadas bajo el protocolo HTTP. En otras palabras, un
API REST permite el uso de un servicio(función o método) perteneciente a una plataforma a un usuario externo
para que el mismo lo use en una aplicación propia. Puede ocurrir el caso que ese usuario externo también seamos
nosotros mismos.

##### Los recursos #####

Un recurso básicamente representa una sección, archivo o contenido que deseamos obtener o modificar de
una plataforma web a través de su API REST. Los mismos serán identificados por una URI, la cuál nos ayudará
a obtener/modificar el mismo.

Las URI’s deben cumplir con ciertas características:

No deben llevar un verbo que implique una acción
  Incorrecto: /recursos/id/editar
  Correcto: /recursos/id/

Deben identificar solo a un recurso, deben ser únicas.

No deben tomar en cuenta el formato en la construcción de la URI
  Incorrecto: /recursos/archivo.pdf
  Correcto: /recursos/archivo

Deben mantener una jerarquía lógica.
  Incorrecto: /apartamentos/2/edificio/3
  Correcto: /edificios/3/apartamentos/2

Los filtrados de información deben hacerse mediante los parámetros HTTP
  Incorrecto: /edificios/3/apartamentos/2/orden/asc
  Correcto: /edificios/3/apartamentos/2/?orden=asc

Deben especificarse usando su forma plural
  Incorrecto: /apartamento/2/
  Correcto: /apartamentos/2/

##### Semántica de los métodos HTTP (GET, POST, PUT, PATCH, DELETE) #####

Una vez conocidas las principales reglas a la hora de construir nuestras URIs, pasamos al
siguiente paso, darle un significado semántico o de acción a los métodos HTTP. Ampliando
nuestro camino un poco más allá de los dos métodos más utilizados comúnmente: GET y POST.

Los métodos serían los siguientes:

GET: Para consultar y leer recursos
POST: Para crear recursos
PUT: Para editar recursos
DELETE: Para eliminar recursos.
PATCH: Para editar partes concretas de un recurso.

###################################
##### Instalación del paquete #####
###################################

$ pip install djangorestframework

# Agregamos el paquete a las aplicaciones instaladas en el settings.py
INSTALLED_APPS = [
    .
    'rest_framework',
]

#################################################
##### Hello world con Django Rest Framework #####
#################################################

# Agregamos el paquete a las aplicaciones instaladas en el settings.py
# En settings.py

INSTALLED_APPS = [
    .
    'rest_framework',
]

---

# En urls.py de alguna aplicación declaramos una url sencilla que llame a una clase.
# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^', views.TestView.as_view(), name='test-view'),
]

---

# En views.py declaramos una clase para mostrar un respuesta http, visitamos localhost para ver la respuesta
# En este caso un hello REST World.
# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    """
    Our First REST API for GET Requests
    """
 
    def get(self, request, format=None):
        return Response({'detail': "Hello REST World"})

---

# Corremos el servidor de desarrollo y visitamos la url que sirva, debemos ver nuestro mensaje
