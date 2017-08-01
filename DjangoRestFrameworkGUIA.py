##### Guía Django Rest Framework by dM #####

# Instalación del paquete
$ sudo pip install djangorestframework

################################################
##### Hello worl con Django Rest Framework #####
################################################

Agregamos el paquete a las aplicaciones instaladas en el settings.py

# En settings.py
INSTALLED_APPS = [
    .
    'rest_framework',
]


# En urls.py de alguna aplicación declaramos una url sencilla que llame a una clase.

# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from app import views

urlpatterns = [
	url(r'^', views.TestView.as_view(), name='test-view'),
]


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
