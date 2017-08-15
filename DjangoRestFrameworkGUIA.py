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

###############################
##### La clase Serializer #####
###############################

Para comenzar una API Web es necesario tener una forma de serializar y deserializar las instancias de
los modelos en representaciones como JSON. Serializar significa tomar los objetos que provengan de los modelos
para manipularlos y mostrarlos en el formato que se requiera, generalmente json a traves de una url.

Podemos hacer esto declarando serializadores que trabajan muy similar a los formularios de Django.
Crea un archivo en el directorio de alguna aplicación un fichero llamado serializers.py

################################################
##### Serializando el model user de django #####
################################################

# En las urls.py de alguna app
# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from series import views

urlpatterns = [
    url(r'^users/$', views.user_list),
]

# In serializer.py
# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Serie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff',
        'is_active', 'date_joined', 'last_login')

# In views.py
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from series.models import Serie
from series.serializers import SerieSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets


def user_list(request):
    """
    List all users.
    """
    if request.method == 'GET':
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

###########################################################
##### Serializando el model user de django usando CBV #####
###########################################################

# En las urls.py de alguna app
# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from series import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    
    url(r'^users/$', views.UsersList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]


# In serializer.py
# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff',
        'is_active', 'date_joined', 'last_login')

# In views.py
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from series.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    """
    Index view, to tray.
    """
    return HttpResponse("Hello, world!")


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class UsersList(APIView):
    """
    List all Users
    """
    def get(self, request, format=None):
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UserSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UserSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#######################################
##### Utilizando ModelSerializers #####
#######################################

De la misma manera que Django ofrece las clases Form y ModelForm, REST framework incluye
las clases Serializer y ModelSerializer para trabajar los modelos.

# -*- coding: utf-8 -*-
from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet


# In serializer.py
class SnippetSerializer(serializers.ModelSerializer):
    """
    Utilizando ModelSerializers para mostrar la data
    """
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'language')


class SnippetSerializer(serializers.Serializer):
    """
    Utilizando Serializers para mostrar la data
    """
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    language = serializers.CharField(required=False, allow_blank=True, max_length=50)

#######################################
##### Paginar la lista de objetos #####
#######################################

Las vistas de listas de usuarios u otros modelos podrían terminar devolviendo un montón de instancias, así que
es conveniente paginar los resultados, esto permite que el cliente API pase por cada una de las página individuales.

# Variable de paginación en settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 5
}

#################################
##### Permisos del API-Rest #####
#################################

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
}
