### Guía Django by dM ###

"""
Django es un framework de desarrollo web de código abierto, escrito en Python, que respeta el
patrón de diseño conocido como Modelo–vista–controlador. Fue desarrollado en origen para gestionar
varias páginas orientadas a noticias de la World Company de Lawrence, Kansas, y fue liberada al
público bajo una licencia BSD en julio de 2005; el framework fue nombrado en alusión al guitarrista
de jazz gitano Django Reinhardt. En junio de 2008 fue anunciado que la recién formada Django Software
Foundation se haría cargo de Django en el futuro.

La meta fundamental de Django es facilitar la creación de sitios web complejos. Django pone énfasis en
el re-uso, la conectividad y extensibilidad de componentes, el desarrollo rápido y el principio
No te repitas (DRY, del inglés Don't Repeat Yourself). Python es usado en todas las partes del framework,
incluso en configuraciones, archivos, y en los modelos de datos.
"""

# Cabecera para los scripts de Python, indica al compilador o editor que se trata de un fichero python
# La segunda linea da codificación UTF-8 al programa
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A veces solo es necesario usar la segunda línea

# -*- coding: utf-8 -*-

####################################
##### Estándares de Desarrollo #####
####################################

Los estándares de desarrollo constituyen las normas o patrones de referencia que se deben implementar en el desarrollo de
aplicaciones de software. Entre los estándares de desarrollo más comunes se encuentran: normas de codificación, normas y
esquemas de seguridad, estándares de interfaz u/s, entre otros.

##### Normas de Codificación #####

Para el desarrollo de un sistema se pueden implementar algunos estándares básicos para su codificación, los cuales contemplan lo
establecido en la PEP-8 --> https://www.python.org/dev/peps/pep-0008/

Algunos puntos importantes que encontramos en el PEP8 son los siguientes:

-Use sangría de 4 espacios, sin tabulaciones.

-Las líneas no deberían sobrepasar los 79 caracteres.

-Use líneas en blanco para separar funciones y clases, también para grandes bloques de código dentro de funciones.

-Cuando sea posible, coloque los comentarios aparte del código de tal manera que en esa línea sólo haya comentarios.

-Use cadenas de documentación (docstrings)

-Use espacios a los lados de los operadores y después de comas, pero no directamente dentro de constructos
con paréntesis. Ej: a = f(1, 2) + g(3, 4)

-Nombre sus clases y funciones de forma consistente, como convención se utiliza CamelCase para las clases y
minúsculas_con_guion_bajo para funciones y métodos. Siempre utilice self como el nombre para el primer argumento de un método.

-No use codificaciones de caracteres lujosas si su código pretende ser utilizado en el ámbito internacional.
Se prefiere que utilicen UTF-8. Tomar en cuenta el PEP-0263 colocando la directiva para codificación
UTF-8 (# -*- coding: utf-8 -*-) a los archivos .py

##### Estándares para la documentación del código fuente #####

-La utilización de docstrings permite generar automáticamente documentación, como alternativas a utilizar para generar la
documentación del proyecto tenemos doxygen o Sphinx.

Cabecera para los scripts de Python, indica al compilador o editor que se trata de un fichero python
La segunda linea da codificación UTF-8 al programa

#!/usr/bin/env python
# -*- coding: utf-8 -*-

A veces solo es necesario usar la segunda línea

# -*- coding: utf-8 -*-

##################
##### TEORIA #####
##################

Framework de desarrollo web de codigo abierto escrito en Python
(todo lo que se haga dentro de Django sera en Python)

-Permite construir aplicaciones web mas rapido y con menos codigo.

-El un proyecto en Django se divide en varias partes llamadas
aplicaciones, el conjunto esas aplicaciones genera un proyecto
general en Django.

-Django se basa en la reutilizacion de el codigo que ya hemos hecho,
en tratar de no repetir y volver a escribir ese codigo. No duplcaremos
el codigo.

-Cuenta con su propia ORM (Object relational maping)  
Quiere decir que nuestra base de datos relacional que ya conocemos
la va a transformar a una base de datos orientada a objetos
Las tablas que soliamos tener vamos a verlas en formas de clases
y las consultas en SQL seran a nivel de Python.

-Django trae su propio administrador por defecto:
Podemos gestionar todos los datos de nuestro proyecto
con el administrador.

####################################
##### PATRON DE DESARROLLO MVT #####
####################################

##### Modelo-vista-controlador #####

-Modelo: Se encarga de manipular toda la informacion
de nuestro proyecto que este en nuestras bases de datos.

-Vista: Es la que decide como es que vamos a mostrar toda
esta informacion almacenada.

-Controlador: Es el que se encarga de hacer
la comunicacion entre el modelo y las vista

##### Modelo-Vista-Template #####

(Ahora Django hara el papel de el controlador, que se encargaba
de la comunicacion de los modelos y las vistas)

-Modelo: Se encarga de manipular toda la informacion
de nuestro proyecto que este en nuestras bases de datos.

-Vista: Es la que se encarga de decir que informacion vamos
a mostrar y en que template.

-Template: Es el que se encarga de coger toda la informacion, organizarla
y ver como se va a mostrar.

###########################
##### Instalar Django #####
###########################

Django está escrito completamente en Python por lo que el primer paso en la instalación de Django 
es el asegurarse de que Python esta instalado.

-Bajar Django de: http://www.python.org/download/
Ejemplo: Django-1.5.12.tar.gz

-Descomprimir el archivo: Nos dejara una carpeta
Ejemplo: Django-1.5.12

-Dentro de (Django-1.5.12) esta el archivo setup.py

-Ejecutar: sudo python setup.py install #Estando en el directorio del archivo

-Recomendada: Tambien podemos realizar la instalación desde PIP
que es un repositorio de paquetes python facil de manejar.

#######################################
##### Verificación de instalación #####
#######################################

-Dentro de la consola de Python ejecutamos:
>>> import django
>>> django.VERSION # Nos mostrara la version de Django instalada
(1, 5, 12, 'final', 0)

De igual forma podemos comprobar versiones de otros paquetes que estén instalados: ejemplo:

>>> import django_extensions # Si estuviése instalado.
>>> django_extensions.VERSION
(1, 7, 4)

-Otra forma:
>>> import django # Si el Comando se ejecuta sin errores es que Django esta instalado
>>> print(django.get_version()) #Nos mostrar la version de Django Instalada
1.5.12

##########################################
##### Compatibilidad / Base de Datos #####
##########################################

Django es compatible con cuatro motores de base de datos:

-PostgreSQL (http://www.postgresql.org/)
-SQLite 3 (http://www.sqlite.org/)
-MySQL (http://www.mysql.com/) #Django requiere MySQL 4.0 o superior
-Oracle (http://www.oracle.com/)

###############################
##### Creando un proyecto #####
###############################

-Un proyecto es una colección de ajustes de una instancia de Django
incluyendo la configuración de la base de datos, las opciones
específicas de Django, y la configuración de la aplicación.

-Para crear un proyecto hay que abrir unaconsola
situarse donde se quiere crear el proyecto y Ejecutar:

$ django-admin.py startproject NombreDelProyecto #Se creará un directorio NombreDelProyecto 

-El comando startproject crea un directorio (NombreDelProyecto)
que contiene cuatro archivos:

1) __init__.py
-Es un fichero vacío, y normalmente no se le añade nada
-Le dice a Python que este directorio debería ser considerado
un paquete Python (un grupo de módulos)

2) manage.py
-Permite interactuar con el proyecto Django, administrar el proyecto.

3) settings.py
-Opciones/configuraciones para este proyecto de Django
-Muestra las características de configuración
de este proyecto Django: Administradores, conexion y acceso
a la base de datos, aplicaciones instaladas, sesiones etc.
-Es un módulo Python normal con variables a nivel de
módulo que representan configuraciones de Django

4) urls.py
-La declaración de las URL para este proyecto de Django;
-Es como una tabla de contenidos de tu sitio hecho con Django.
-Las URLs(Localizador uniforme de recursos: Sirve para nombrar recursos
en Internet o en servidores locales. Tiene como proposito asignar una 
direccion unica a cada uno de los recursos disponibles ejemplo:
textos, imagenes, vdeos, etc...) para este proyecto Django
-Contiene las direcciones URL de este proyecto Django.
-Al principio no contiene ninguna.

(Estos archivos ya constituyen una aplicación Django de trabajo)

##### El servidor de desarrollo #####

-Entrar al directorio (NombreDelProyecto)
y ejecuta el comando:

$ python manage.py runserver #Verás la siguiente salida en la línea de comandos:

$ python manage.py check #Validar los modelos en busca de errores sin necesidad de correr el servidor.

Validating models...

0 errors found
February 22, 2015 - 13:35:04
Django version 1.5.12, using settings 'NombreDelProyecto.settings'
Development server is running at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

(Arranca el servidor de desarrollo de Django
un servidor web liviano escrito completamente en Python.
Se incluye en Django para que puedas desarrollar de manera rápida
sin tener que vértelas con la configuración de un servidor de producción
como Apache, hasta que estés listo para producción)

-Cuando el servidor está inicializado, visita http://127.0.0.1:8000/
usando un navegador web. Se observara una página "Welcome to Django"

-Por defecto, el comando runserver arranca el servidor de desarrollo
en el puerto 8000

$ python manage.py runserver 8080 #Arranca el servido en el puerto 8080

-Cambiando la direccion IP donde va a correr el servidor:

$ python manage.py runserver 127.0.0.1:8000

ó

$ python manage.py runserver mi_ip_privada_en_la_red:8000

-Con 0.0.0.0:8000 toma automáticamente la ip privada del equipo en la red local.

$ python manage.py runserver 0.0.0.0:8000

#############################################
##### Configuración de la base de datos #####
#############################################

En settings.py se pueden configurar los privilegios, nombre, etc a la base de datos.
y ya existen unas variables predeterminadas a las cuales podemos cambiar el valor
según se necesite, entre ellas están las variables de conexión con la base de datos como:

ENGINE: Ya sea 'django.db.backends.postgresql_psycopg2', 'django.db.backends.mysql'
o 'django.db.backends.sqlite3'. Otros backends también están disponibles.

NAME: El nombre de tu base de datos. Si estás usando SQLite la base de datos
será un archivo en tu ordenador; en tal caso, NAME debería ser la ruta absoluta
incluyendo nombre de archivo, de dicho archivo. Si el archivo
no existe se creará automáticamente cuando sincronices la base
de datos por primera vez.

USER: El usuario de la base de datos (no usado en SQLite).

PASSWORD: La contraseña de la base de datos (no usado en SQLite).

HOST: La máquina donde está ubicada la base de datos.
Déjalo como una cadena vacía si la base de datos está en la misma
máquina física (no usado en SQLite).

PORT: Le indica a Django qué puerto usar cuando se conecte a la base de datos. Si
estás utilizando SQLite, deja este en blanco. En otro caso, si dejas este en blanco,
el adaptador de base de datos subyacente usará el puerto por omisión acorde al
servidor de base de datos. En la mayoría de los casos, el puerto por omisión está
bien, por lo tanto puedes dejar este en blanco.

'PORT': '5432', # Puerto por defecto de postgresql, generalmente no es necesario especificar uno
# porque así lo tomará por defecto.

Fragmento tomado de un settings.py sobre éste tópico:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'admin',
        'PASSWORD': 123456,
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

##########################################
##### Ejemplo de conexión con sqlite #####
##########################################

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

##########################
##### INSTALLED_APPS #####
##########################

En el settings.py, la variable INSTALLED_APPS contiene el nombre de todas
las aplicaciones Django que están activadas en esta instancia de Django.
Las aplicaciones pueden ser empacadas y distribuidas para ser usadas por otros proyectos.

Por defecto, INSTALLED_APPS contiene las siguientes aplicaciones, todas ellas vienen con Django:

-django.contrib.auth -- Un sistema de autenticación.
-django.contrib.contenttypes -- Un framework para tipos de contenidos.
-django.contrib.sessions -- Un framework para manejar sesiones.
-django.contrib.sites -- Un framework para manejar múltiples sitios con una única instalación Django.

################################
##### Aplicación de Django ##### 
################################

Es una colección de archivos de código fuente, incluyendo modelos y vistas, que conviven en un solo
paquete de Python y representen una aplicación completa de Django.

-La aplicacion se creara en el directorio (NombreDelProyecto) con:

python manage.py startapp NombreAplicacion

-Esto creará un directorio NombreAplicacion, que contiene los siguiente archivos:

- __init__.py

- models.py: En este archivo es donde vamos a crear nuestras tablas de las bases de datos.
Un modelo de Django es una descripción de los datos en la base de datos, esta es tu capa de datos

- tests.py

- views.py: En este archivo es donde pondremos todas las funciones que necesitemos
ejecutar en nuestro proyecto

Las variables las llamo en mi template así: {{ variable }}

#######################
##### Tips varios #####
#######################

*****Crear el proyecto
django-admin startproject NombreDelProyecto

*****Configura el settings
Configurar zona horaria, lenguaje
--> Using Language Identifiers: http://www.i18nguy.com/unicode/language-identifiers.html

*****Configurar la base de datos
Elegir el motor y el nombre de la db, si se usa postgres esta debe estar creada y tner un usuario, si se
usa sqlite3 no hace falta crearla, solo agregando el nombre Django la crea

*****Habilitar el administrador (apps,urls)
Descomentar las lineas correspondientes en el settings/apps y en el urls

*****Sincronisar la db
python manage.py syncdb #Anterior a Django 1.7.x

*****Crear el super usuario
Escribir el user, pass y email del superuser

*****Correr el servidor, validar los modelos y probar el admin
Probar el admin /admin 

python manage.py runserver

*****Crear aplicacion y registrarla en el settings
python manage.py startapp NombreAplicacion

*****Crear carpeta templates y declararla en el settings
Declarar la carpeta de nuestras plantillas en el settings en 
TEMPLATE_DIRS con la ruta completa '/home/osorio/Escritorio/inscripcion/templates'

*****Abrir el views.py y declarar la funcion con el render y la template que corresponda
En la vista iran nuestras funciones y clases y decimos que plantillas
vamos a usar 

*****Crear el Index de la funcion y guardarlo en templates
Crear el html y guardarlo en nuestra carpeta de plantillas 

*****Declarar la funcion de la vista en las urls
Las vistas deben ser declaradas en las urls
url(r'^$', 'aplicacion.views.funcion', name='funcion'),

*****Probar el index con el servidor andando
python manage.py runserver

*****Creamos los modelos 
En el models.py crearemos las clases que al final
seran nuestras tablas con sus campos en nuestra base de datos 

python manage.py sqlall books / books es el nombre de la aplicación, podremos
observar nuestros modelos de datos antes de crear las tablas con la sincronizacion de la db

*****Sincronizamos la db 
Al sincronizar, las clases que creamos en los modelos
se generaran en tablas de nuestra base de datos 

python manage.py syncdb

*****Corremos el servidor y entramos al admin para ver nuestras tablas
En principio no veremos nuestras tablas en el admin, tenemos que crear el archivo admin.py
en el directorio de la aplicacion y declaramos

from django.contrib import admin 
from .models import NombreClase

admin.site.register(NombreClase) 

volvemos a correr el servidor, entramos al admin y ya podemos ver nuestra tabla creada
y podemos llenarla de datos

*****Creamos un template donde mostraremos nuestro formulario
basado en los modelos de la base de datos, podemos usar el modelo como base para los 
forms, creamos el template con el formulario, el metodo etc

<form method="POST"> {% csrf_token %} # Este token lo agregamos por segridad, Django lo exige
    {{ form }}
    <input type="submit" value="Enviar">
</form>

*****En la vista creamos una clase que contendra nuestro modelo

class RegistrarAlumno(CreateView):
    template_name = "registrar.html"
    model = Alumno

Con esto mandamos a la plantilla declarada un form el cual recibe el form en el template
asignado

*****Declaramos nuestra clase en la URLS para que la lea como vista 
url(r'^registrar/$', RegistrarAlumno.as_view(), name='RegistrarAlumno'),
####Debemos revisar siempre los import, son muy importantes

##### Declarando los CSS #####

Creamos la carpeta static que contendra nuetros css, imagenes y demas
archvos estaticos, se debe guardar a nivel de las plantillas
 (aplicacion/static/css/estilo.css)
 (aplicacion/templates/index.html)

 Con esto llamamos nuestro CSS en la plantilla:

 <head>
    <title>PAGOS</title> 
    <meta http-equiv="content-type" content="text/html;charset=utf-8" /> 
    <meta charset="UTF-8" /> 
    {% load staticfiles %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/estilo.css' %}" />
</head>

##### Agregando imagenes a la plantilla #####

Los archivos de media seran llamados de la carpeta Img
que por lo general acompaña al css, se hace referencia a la 
carpeta static con {{STATIC_URL}} y luego la ruta de la imagen:
Ejemplo:

<img src="Imagen.jpg" width="200px" heigth="200px"></img>

<img src="{{STATIC_URL}}css/Img/gris.JPG"></img> Agregando una imagen local

######################
##### Migrations #####
######################

Mediante la ejecución de makemigrations, le estás diciendo a Django que has hecho algunos cambios a
sus modelos y que desea que los cambios se almacenarán como la migración.

Las migraciones son cómo almacena Django cambios a sus modelos (y por tanto el esquema de base de datos)

Si hay modelos declarados en una aplicación, se creará una carpeta "migrations" que contiene el esquema de la
base de datos, muy similar a un fichero .sql, con los nombres de las tablas, sus campos, y las fechas en que se crearon.

####################################
##### Estructura de un proyecto ####
####################################

# Algunos directorios debemos crearlos nosotros por ejemplo: templates, static, admin.py

project
  manage.py
  database.db  
  project/
    settings.py
    urls.py
    wsgi.py

  app/
    templates/
      app/
        base.html
        index.html
    admin.py
    tests.py
    models.py
    forms.py
    views.py  
    
    static/
      css/
        styles.css

    img/ 
      a.jpg
      b.png

    js/
      jquery.js
-----

##### Recommended Django Project Layout #####

myproject/
    manage.py
    myproject/
        __init__.py
        urls.py
        wsgi.py
        settings/
            __init__.py
            base.py
            dev.py
            prod.py
    blog/
        __init__.py
        models.py
        managers.py
        views.py
        urls.py
        templates/
            blog/
                base.html
                list.html
                detail.html
        static/
           …
        tests/
            __init__.py
            test_models.py
            test_managers.py
            test_views.py
    users/
        __init__.py
        models.py
        views.py
        urls.py
        templates/
            users/
                base.html
                list.html
                detail.html
        static/
            …
        tests/
            __init__.py
            test_models.py
            test_views.py
     static/
         css/
             …
         js/
             …
     templates/
         base.html
         index.html
     requirements/
         base.txt
         dev.txt
         test.txt
         prod.txt

'''
Estructura con los templates fuera de las aplicaciones
Es un tipo de proyecto menos modular
'''

myproject/
    manage.py
    myproject/
        __init__.py
        urls.py
        wsgi.py
        settings.py
    app/
        __init__.py
        models.py
        managers.py
        views.py
        urls.py
    users/
        __init__.py
        models.py
        views.py
        urls.py
    static/
        css/
            …
        js/
            …
    templates/
        base/
            base.html
        app/
            index.html
        users/
            index.html
    requirements/
        base.txt
        dev.txt
        test.txt
        prod.txt

# La siguiente configuración de los templates dirs aplica a la estructura menos modular.

##############################################################
##### Configuración del settings para los templates dirs #####
##############################################################

# Esta configuración se usa cuando se crea una carpeta templates/app/xxx.html
# para alvergar todos los templates de las aplicaciones

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#################################################
##### LANGUAGE_CODE, idioma de los mensajes #####
#################################################

Django por defecto muestra una variedad de mensajes
en los templates, ya sea para validaciones en formularios u otros...

Por ellos el cambio del codigo de lenguaje es muy importante, por ejemplo

#LANGUAGE_CODE = 'en-us' Ver los mensajes en ingles
#LANGUAGE_CODE = 'en-es' Ver los mensajes en español

#######################
##### Comentarios #####
#######################

Al igual que en HTML o en un lenguaje de programación como Python, el lenguaje de
plantillas de Django permite usar comentarios. Para designar un comentario, usa
{# #}
{# Esto es un comentario #}
Este comentario no será mostrado cuando la plantilla sea renderizada.
Un comentario no puede abarcar múltiples líneas. Esta limitación mejora la
performance del analizador sintáctico de plantillas. En la siguiente plantilla, la salida
del renderizado mostraría exactamente lo mismo que la plantilla (esto es, la etiqueta
comentario no será tomada como comentario):

Esto es una {# Esto no es
un comentario #}
prueba.

Si quieres usar un comentario que abarque varias líneas, usa la etiqueta {%
comment %}, así:
 
{% comment %}
    Este es un comentario
    que abarca varias líneas
{% endcomment %}

############################
##### Tiempo de sesión #####
############################

#Variable del settings.py que indica que a los 40min se destruye la sesión creada de algún usuario autenticado.
# SESSION AGE 40 Minutes
#SESSION_COOKIE_AGE = 40*60

#######################################################
##### Cerrar sesión cuando se cierra el navegador #####
#######################################################

#Variable del settings.py
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

##############################
##### Modelos en Django  #####
##############################

¿Qué es un modelo?

- En Django los modelos son como django tratara los datos, contendrá los campos de los objetos que queremos guardar.
Generalmente django creara por cada modelo una tabla en la base de datos.

- Cada modelo es una clase python que hereda de django.db.models.Model

- Cada atributo del modelo representa un campo de la tabla de la base de datos.

##### Los campos #####

Los campos son el tipo de objeto del atributo que guardara, hay varios tipos:

**AutoField: Es un IntegerField que se incrementa cuando creas un nuevo objeto, casi que no es
necesario ya que django lo crea solo si no especificas otro campo como id.

**BigIntegerField: Representa un Entero de 64 bit, es como el IntegerField, solo que permite números
desde el -9223372036854775808 hasta el 9223372036854775807. El campo por defecto de los formularios es el TextField.

**BooleanField: El campo de true/false. El campo por defecto de los formularios es un CheckboxInput.
El vlaor por defecto es None si no defines el default.

**CharField: Para string pequeños, frases o palabras. El campo por defecto en los formularios es el TextInput.
    max_length=20: Establece el tamaño máximo del string, es requerido.

**CommaSeparateIntegerField: Guarda una lista de enteros separados por coma. 
    Max_length=20: Establece el valor máximo de los enteros, es requerido.

**DateField: Guarda una instancia de la fecha a partir de la clase datetime.date de python.
    auto_now=True: Actualiza la fecha cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la fecha de cuando se creo.

**DateTimeField: Como el DateField solo que guarda también la hora
    auto_now=True: Actualiza la fecha cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la fecha de cuando se creo.

**DecimalField: Guarda números decimales.
    max_digits=5: Establece el numero de dígitos máximo, la suma de la parte entera y la decimal
    decimal_places=2: Establece el número de dígitos de la parte decimal.

**EmailField: Es un CharField que comprueba lo introducido para verificar que sea un email.
    max_length=75: Establece el tamaño máximo del email, es requerido.

**FileField: Sirve para guardar archivos en el servidor. En el formulario saldría el campo de escoger un
fichero del ordenador. Tiene que estar definido el MEDIA_ROOT en el settings para que guarde los archivos.
Guardara el archivo en la ruta especificada por el MEDIA_ROOT.
upload_to='/videos': Subirá el archivo a la carpeta vídeos alojada en la carpeta definida por MEDIA_ROOT. (Requerido)
FileField(upload_to='/video'[, max_length=100, **options]): si se quiere poner los atributos opcionales tendrán que añadirse así.

**FilePathField: Sirve para mostrar los archivos accesible de una carpeta siguiendo una restricción si se quiera, para
hacer alguna operación sobre ellos.
FilePathField(path=None[, match=None,recursive=False, max_length=100, **options])
    path (requerido): directorio del que sacara FilePathField las opciones.
    match: filtro por el que pasaran los archivos, se usaran expresiones regulares.
    recursive: False por defecto, especifica si entran las subcarpetas de la ruta indicada por path.
    max_length: Indica el tamaño máximo del nombre del archivo.

**FloatField: Campo que guarda una instancia del modelo Float de python.

**ImageField: Como el FileField pero solo acepta formatos de imágenes. Tiene dos campos opcionales mas que el FielField
    height_field: Representa el alto máximo de la imagen.
    width_field: Representa el ancho máximo de la imagen.

**IntegerField: Guarda un entero.

**IPAddressField: Guarda un string que coincida con el formato ip (192.168.0.1).

**GenericIPAddressField: Guarda una ip, ya sea ipv4 o ipv6. Para saber como las guarda Doc Django.

**NullBooleanField: Como el BooleanField pero permite null.

**PositiveIntegerField: Guarda un entero mayor o igual que cero.

**SlugField:  Campo que guarda una pequeña etiqueta (letras, números, guiones) suele usarse en las url.

**TextField: Campo que guarda texto.

**TimeField: Guarda una hora, comparte los campos con DateField
    auto_now=True: Actualiza la hora cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la hora de cuando se creo.

**URLField: Guarda una dirección html, comprueba que lo introducido sea una dirección html.

##### Campos de relación #####

ForeignKey:  Para referir objetos a un objeto, un modelo puede referirse a un modelo, pero un modelo puede estar referido a mas de uno, es lo que se llama un many-to-one referencia.

ManyToManyField: Para guardar una referencia a varios objetos de la misma clase. Hay que definir la clase con la que se relaciona. Va guardando las referencias a esos objetos en una lista con las primary keys referncia.

OneToOneField: Es como el ForeignKey pero tiene unique=True, por lo que solo puede haber una referencia a ese objeto.

##### Opciones que tienen todos los campos #####

null=True: Permite que los valores puedan ser null.

blank=True: Permite que el campo se pueda quedar en blanco.

blank=True,null=True # Para que de verdad acepte valores en blanco en la base de datos y en el formulario.

choices=meses: Permite asignar un diccionario de elementos a un objetos para que los valores solo sean los contenidos en el diccionario. La clave del diccionario sera lo que se guarda en la base de datos, el valor asociado sera lo que se mostrar en el formulario que lo use.

db_column: El nombre de la columna donde django guardara el campo, si no se especifica guarda el nombre del campo.

db_index=True: Sirve para indexar el campo en las búsqueda de django. Por defecto django busca entre las PK de la base de datos, si añades esto también buscara entre esos datos y no tendrás que acceder directamente al objeto para comprobar el campo en las búsquedas.

db_tablespace: El nombre al que se referencia para buscar si ha sido indicado como index.

default: El valor por defecto que tiene el modelo, si se va a guardar un valor distinto a vació se guardara con el valor por defecto.

editable=False: Indica si el valor se puede modificar, si es falso no aparecerá en el admin ni similares.

error_messages={null:"Hay que darle un valor",blank:"No se puede dejar en blanco",invalid="El valor introducido es erróneo", invalid_choice:"Has escogido un valor inadecuado", unique="Este valor ya existe"}: Como se ve en el ejemplo hacer referencia a los mensajes que se mostraran si se produce ese error. No hace falta crear todos los mensajes. Si no los creas saldrá el que tiene por defecto.

help_text="Inserta un nombre": Un texto que aparecerá en forma de ayuda en el campo del formulario.

primary_key=True: Para asignar que el campos es la clave primaria del modelo.

unique=True: Indica que el valor es único, solo podrá haber uno en la base de datos.

unique_for_date='pub_date': El valor de esta propiedad tendrá que existir como campo del modelo y tendrá que ser del tipo DateField o DateTimeField. Lo que hace es no dejar que haya un elemento con el mismo valor del campo y el mismo día.

unique_for_month='pub_date': El valor de esta propiedad tendrá que existir como campo del modelo y tendrá que ser del tipo DateField o DateTimeField. Lo que hace es no dejar que haya un elemento con el mismo valor del campo y el mismo mes.

unique_for_year='pub_date': El valor de esta propiedad tendrá que existir como campo del modelo y tendrá que ser del tipo DateField o DateTimeField. Lo que hace es no dejar que haya un elemento con el mismo valor del campo y el mismo año.

verbose_name="Nombre de usuario": Nombre del campo comprensible por humanos, si no se crea django lo generar automáticamente, convirtiendo los guiones en espacios.

validators=[]: Una lista de validaciones para el campo referencia.

on_delete: Se utiliza para decirle a Django qué hacer con instancias de modelo que dependen de la instancia de modelo que elimine.
(Por ejemplo, una relación de ForeignKey). El on_delete = models.CASCADE le dice a Django que coloque en cascada el efecto
de supresión, es decir, continúe eliminando también los modelos dependientes.

user = models.OneToOneField(User, on_delete=models.CASCADE)

'''
Declarando la clase Articulo y Comentarios para una publicacion, y estableciendo
la relacion entre los comentarios y un articulo
'''

from django.db import models

class Articulo(models.Model):
   autor = models.CharField(max_length = 30)
   titulo = models.CharField(max_length = 100)
   texto = models.TextField()
   fecha = models.DateTimeField()

class Comentario(models.Model):
   nombre = models.CharField(max_length = 200)
   cuerpo = models.TextField()
   fecha_pub = models.DateTimeField('fecha publicacion')
   articulo = models.ForeignKey(Articulo)

#Modelos para un blog, con un método para la fecha de publicación.
#Más en --> https://tutorial.djangogirls.org/es/

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def __unicode__(self): Para python 2.x
        #return self.title

    def __str__(self): # Para python 3.x
        return self.title


##################################
##### Hello world con Django #####
##################################

# En urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# En views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

############################
##### *args y **kwargs #####
############################

La sintaxis especial, *args y **kwargs en definiciones de funciones se utiliza para pasar un número variable
de argumentos a una función. El forma simple (*args) se utiliza para pasar una lista de argumentos de longitud
variable sin palabra clave y la forma de doble asterisco (**kwargs) se utiliza para pasar una lista de
argumentos con palabras clave de longitud variable o diccionarios, un ejemplo sería:

def get_context_data(self, **kwargs):

equivale a:

def get_context_data(self, pk, id_x, id_y):

##############################################################################
##### Ejemplo de admin.py para mostrar los modelos en el admin de django #####
##############################################################################

# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post

admin.site.register(Post)

###############################################
##### Pasando un diccionario en el render #####
###############################################

"""
xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
chartdata = {'x': xdata, 'y': ydata}
charttype = "pieChart"
chartcontainer = 'piechart_container'
data = {
    'charttype': charttype,
    'chartdata': chartdata,
    'chartcontainer': chartcontainer,
    'extra': {
        'x_is_date': False,
        'x_axis_format': '',
        'tag_script_js': True,
        'jquery_on_ready': False,
    }
}
"""
data = {'x': "xxxx", 'y': "yyyy"}
return render_to_response('piechart.html', data)

##################################################
##### Pasando un diccionario en TemplateView #####
##################################################

#views.py
class Xxx(TemplateView):
    template_name = "index.html"
    form_class = XxxForm

    #def get(self,request):
    def get(self,request,*args, **kwargs):
        data = {'x': "xxxx", 'y': "yyyy"}
        return render(request,self.template_name, {'data':data})

#index.html
<div id="content">
  {{ data.x }}<br />
  {{ data.y }}
</div>

######################################################################
##### Contando objetos con querysets y pasando datos al template #####
######################################################################

# views.py
def datos(request):
    x = Persona.objects.filter(voto__icontains='d').count()
    y = Persona.objects.filter(voto__icontains='n').count()
    z = Persona.objects.filter(voto__icontains='c').count()    
    data = {
      'x': x,
      'y': y,
      'z': z,
    }
    print "----------"
    print data
    return render_to_response('registro/datos.html', {'data':data})

# template.html
<h3>Datos</h3>
{{ data.x }}
{{ data.y }}
{{ data.z }}

##############################################
##### Declarando variable en el template #####
##############################################

{% with name="World" greeting="Hello" %}
    <div>{{ greeting }} {{name}}!</div>
{% endwith %}

##################################
##### Creating an admin user #####
##################################

First we’ll need to create a user who can login to the admin site. Run the following command:

$ python manage.py createsuperuser

Enter your desired username and press enter.

Username: admin

You will then be prompted for your desired email address:

Email address: admin@example.com

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

Password: #####
Password (again): *********
Superuser created successfully.

##########################
##### login_required #####
##########################

# Trabaja con el from django.contrib.auth.decorators import login_required en las urls
# url(r'^lista$', login_required(views.PostLista.as_view()), name='post_lista'),
# url(r'^detalle/(?P<pk>\d+)$', login_required(views.PostDetalle), name='post_detalle'),

# Variable en el settings.py, url a la que se redirecciona cuando no hay usuario logeado
# y se intenta acceder a una url protegida. 
LOGIN_URL = "/login"

# Usandolo en una función en views.py
from django.template import RequestContext

@login_required(login_url='/')
def index(request):
    user = request.user
    return render_to_response('index.html', {'usuario':user},context_instance=RequestContext(request))

# En urls.py

# -*- coding: utf-8 -*-
from django.conf.urls import url
from app import views
from app.views import *
import app.views as views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.Login.as_view(), name='login'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'success/', login_required(views.Success.as_view(), login_url='login'), name='success'),
    url(r'logout/$', views.Logout.as_view(), name='logout'),
]

################################
##### if/else en templates #####
################################

La etiqueta {% if %} evalúa una variable, y si esta es "true" (esto es, existe, no está
vacía y no es un valor Boolean falso), el sistema mostrará todo lo que hay entre
{% if %} y {% endif %}, por ejemplo:

{% if es_fin_de_semana %}
    <p>¡Bienvenido fin de semana!</p>
{% endif %}

La etiqueta {% else %} es opcional:
 
{% if es_fin_de_semana %}
    <p>¡Bienvenido fin de semana!</p>
{% else %}
    <p>De vuelta al trabajo.</p>
{% endif %}


# If else en una tabla con un for.
{% for x in log %}
<tr>
    <td>{{ x.username }}</td>
    <td>{{ x.status }}</td>
    {% if x.status == 1 %}
        <td>Active</td>
    {% else %}
        <td>Inactiva</td>
    {% endif %}
</tr>
{% endfor %}

# Comparando con una cadena de caracteres
{% if x.tipo == "Acceso" %}
  <td class="access">Acceso</td>
{% else %}
  <td>yyyy</td>
{% endif %}

# If else and elif en una tabla con un for.
{% for x in log %}
<tr>
    <td>{{ x.user }}</td>
    <td>{{ x.status }}</td>
    {% if x.status == 1 %}
        <td>Active</td>
    {% elif x.status == 2 %}
        <td>Inactive</td>
    {% else %}
        <td>Dead</td>
    {% endif %}
</tr>
{% endfor %}

############################
##### for en templates #####
############################

La etiqueta {% for %} permite iterar sobre cada uno de los elementos de una
secuencia. Como en la sentencia for de Python, la sintaxis es for X in Y, dónde Y es la
secuencia sobre la que se hace el bucle y X es el nombre de la variable que se usará
para cada uno de los ciclos del bucle.
Cada vez que atravesamos el bucle, el sistema de plantillas renderizará todo entre
{% for %} y {% endfor %}.
Por ejemplo, puedes usar lo siguiente para mostrar una lista de atletas tomadas de
la variable lista_atletas:

<ul>
{% for atleta in lista_atletas %}
    <li>{{ atleta.nombre }}</li>
{% endfor %}
</ul>

# Cuando instanciamos un objeto en la vista, para ser renderizado en la plantilla usamos:
<ul>
{% for objeto in objetos %}
    <li>{{ objeto.attr }}</li>
{% endfor %}
</ul>

##################################################
##### Permisos de contenido según el usuario #####
##################################################

# Si el usuario está autenticado
{% if request.user.is_authenticated %}
  Bienvenido: {{user.username}}
{% else %}
  Bienvenido: Anónimo
{% endif %}

# Si el usuario es admin
{#% if user.is_staff %#}
{% if user.is_superuser %}
  <h1>Soy Admin </h1>
{% else %}
  <h1>No soy Admin </h1>
{% endif %}

##############################################################
##### Permisos de contenido según el usuario en la vista #####
##############################################################

'''
En este caso tenemos una vista que renderiza una bitacora de eventos
y que solo se podrá acceder si es superusuario entonces queda así:
'''

from django.template import RequestContext

class BitacoraView(ListView):
    """
    Clase que muestra la lista de entradas de la bitácora, solo muestra la lista
    si el usuario es staff.
    """
    model = Bitacora
    template_name = "bitacora.html"

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object_list=self.object_list)
        #print "***** Entró por get"
        #if request.user.is_superuser:
        if request.user.is_staff:
            #print "--------------------"
            #print request.user
            return self.render_to_response(context)
        else:
            #print "--------------------"
            #print "No tiene permiso"
            return render_to_response('index.html',context_instance=RequestContext(request))

#######################################################
##### Ruta de instalación convencional de Django ######
#######################################################

$ python
>>> import django
>>> django.__file__
'/usr/local/lib/python2.7/dist-packages/django/__init__.pyc'

####################################################################
##### Ruta de instalación de Django dentro de entorno virtual ######
####################################################################

/home/user/Entornos_virtuales/Django_1.10.1/local/lib/python2.7/site-packages/django

###############################
##### Estáticos en Django #####
###############################

El primer lugar donde inicia el manejo de los archivos estáticos reside en el archivo
de configuraciones del proyecto: settings.py, en este archivo tenemos líneas
exclusivamente dedicadas al manejo del contenido estático.

**STATICFILES_DIRS, esta variable permite declarar la ruta, desde la cual
se enlazará el contenido estático, por ejemplo:

# Configuración de los directorios en donde se encuentran los archivos estáticos
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

Podemos tener mas carpetas para los estáticos como: static y media, y para que sean bien servidas deben incluirse
en STATICFILES_DIRS tal que:

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'media/'),
)

Ahora las dos carpetas serán servidas desde mysite/static/ por la definición de la variable STATIC_URL.

Su proyecto probablemente también tendrá activos estáticos que no están vinculados a una aplicación en particular.
Además de usar un directorio static/ dentro de sus aplicaciones, puede definir una lista de directorios (STATICFILES_DIRS)
en su archivo de configuración donde Django también buscará archivos estáticos. Por ejemplo:

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

**STATIC_URL, es la variable que va a definir la url donde se encuentras
los archivos estáticos a ser servidos.

STATIC_URL = '/static/'

Este ejemplo permite ver los estáticos en la ruta 

http:example.com/static/css/theme.css
http:example.com/static/js/functions.js
http:example.com/static/img/x.png

Así la carpeta donde se encuentran se llame media o estaticos o x, a nivel de url serán servidos
desde lo que se definió en STATIC_URL.

**{% load staticfiles %}
Cuando usamos el tag load staticfiles cargamos la ruta de nuestro directorio de archivos estáticos,
es decir <name_project>/static, luego cada vez que escribamos una etiqueta static estaremos haciendo
referencia a esa ruta.

**MEDIA_ROOT
Ruta del sistema de archivos absoluto al directorio que contiene archivos cargados por el usuario.
Valor predeterminado: '' (Cadena vacía)

Ejemplo: "/var/www/example.com/media/"

**STATIC_ROOT
La ruta absoluta del directorio donde collectstatic va a colectar los estaticos, esto para entornos de producción.
Establezca la configuración STATIC_ROOT en el directorio desde el que desea servir estos archivos, por ejemplo:

STATIC_ROOT should be the absolute path to the directory static files should be
collected to:

STATIC_ROOT = "/var/www/example.com/static/"

**MEDIA_ROOT
Esta es la ruta absoluta a la carpeta que mantendrá las subidas del usuario.
Por ejemplo MEDIA_ROOT = "/User/Timmy/Sites/Pho/root/media/".

MEDIA_ROOT y STATIC_ROOT deben tener valores diferentes. Antes de que STATIC_ROOT se introdujera, era
común confiar o fallback en MEDIA_ROOT para también servir archivos estáticos; Sin embargo, ya que
esto puede tener serias implicaciones de seguridad, hay una comprobación de validación para evitarlo.

**MEDIA_URL
Valor predeterminado: '' (Cadena vacía)

URL que maneja los medios servidos desde MEDIA_ROOT, utilizados para administrar archivos almacenados.
Debe terminar en una barra inclinada si se establece en un valor no vacío. Tendrá que configurar estos
archivos para que se publiquen en entornos de desarrollo y producción.

MEDIA_URL = "media/"

Si desea utilizar {{ MEDIA_URL }} en sus plantillas, añada 'django.template.context_processors.media' en la
opción 'context_processors' de TEMPLATES.

#######################################################
##### Agregando enlaces a archivos para descargas #####
#######################################################

Deben estar en la carpeta static del proyecto

{% load staticfiles %}
<!--b>Ubicación Electrónica:</b> <a href="static/biblioteca/2017/x.pdf" target="_blank">Descargar</a-->
<b>Ubicación Electrónica:</b> <a href="{% static 'biblioteca/2017/x.pdf' %}" target="_blank">Descargar</a>
<br />
<img src="{% static 'biblioteca/2017/x.jpg' %}"></img>

####################################
##### Recolectar los estáticos #####
####################################

definir en el settings.py a:

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

$ python manage.py collectstatic

si falla entonces se prueba comentando a:

#STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'static'),
#)

luego:

$ python manage.py collectstatic

Si todo va bien se tienen que haber copiado los estáticos del admin de django a static.

Cuando el:

$ python manage.py collectstatic

falla, se pueden recolectar manualmente los estáticos, solo hay que buscar la ruta adecuada dentro del core de django, en
un entorno virtual sería en:

/home/user/Entornos_virtuales/Django_1.10.1/local/lib/python2.7/site-packages/django/contrib/admin/static/

Dentro está la carpeta admin/ con todos los estáticos que necesita el servidor, sobre todo los estáticos del admin de django, por lo tanto
podemos copiar esa carpeta admin/ a la carpeta static de nuestro proyecto.

####################################################
##### Personalizar templates del administrador #####
####################################################

Para poder personalizar las plantillas del administrador es recomendable no trabajar directamente
en los templates del core del framework si no copiar esos templates en nuestro proyecto.

El sitio de administración muestra "Administración de Django" en la cabecera porque esto es lo que se incluye en la plantilla
admin/base_site.html. Por defecto, esta plantilla se encuentra en el directorio de plantillas de administración de
Django, django/contrib/admin/templates, que puedes encontrar buscando en tu directorio site-packages de Python, o donde sea
que Django fue instalado. Para personalizar esta plantilla base_site.html, copia la original dentro de un subdirectorio
llamado admin dentro de cualquier directorio este usando TEMPLATE_DIRS. Por ejemplo, si tu TEMPLATE_DIRS
incluye "/home/misplantillas", entonces copia django/contrib/admin/templates/admin/base_site.html
a /home/misplantillas/admin/base_site.html. No te olvides del subdirectorio admin, entonces asi Django encuentra las plantillas por
defecto de la interfaz de administración primero en nuestros directorios templates, lo que sucede es que, por defecto, Django
automáticamente busca plantillas dentro del subdirectorio templates/ de cada paquete de aplicación
como alternativa, si no consigue nada usara las plantillas de su core.

###################################################################
##### Desplegar aplicación web en Django - pythonanywhere.com #####
###################################################################

Tutorial en Español en --> ttps://stories.devacademy.la/django-y-como-desplegar-tu-peque%C3%B1a-aplicaci%C3%B3n-web-y-no-morir-en-el-intento-e18551c0c8b6#.z8mol0onp

Otro Tutorial en Español en --> https://tutorial.djangogirls.org/es/deploy/

Pythonanywhere que cuenta con un sin fin de paquetes de Python y soporta Python desde la ultima versión estable de la 2.7.x y
las ultimas versiones estables de la 3.x.

1) Creamos una cuenta en Pythonanywhere como principiante ( Beginner), lo que nos da un plan gratuito (obviamente con algunas
limitaciones, como solo poder crear o desplegar un proyecto por cuenta).

Al ingresar vamos a dar click en Dashboard para acceder a nuestro panel principal en donde tendremos 5 pestañas especiales de las cuales
en esta vez solo usaremos 4: Consoles, Files, Web y Databases. En la pestaña de consola podremos elegir abrir una consola bash que nos 
situará en el directorio de nuestro usuario: /home/dm/ desde la consola podemos clonar repositorios y para nuestro caso podemos clonar el proyecto
que queremos desplegar. También podemos entornos virtuales por si necesitamos paquetes python adicionales, por defecto nuestra sesion en bash ya
tiene instalado django 1.10 y python 2.7.x.

Cuando te hayas registrado en PythonAnywhere serás redirigida a tu panel de control o página "Consoles". Elije la opción para iniciar una consola "Bash", que
es la versión PythonAnywhere de una consola, como la que tienes en tu PC.

Descarguemos nuestro código desde GitHub a PythonAnywhere mediante la creación de un "clon" del repositorio. Escribe lo siguiente en la consola de PythonAnywhere:

$ git clone https://github.com/<tu-usuario-github>/my-first-blog.git

$ virtualenv my_env

Instalamos los requerimientos en el entorno virtual.

Ahora toca configurar el fichero WSGI, Django funciona utilizando el "protocolo WSGI", un estándar para servir
sitios web usando Python, que PythonAnywhere soporta. La forma de configurar PythonAnywhere para que reconozca
nuestro proyecto Django es editar un fichero de configuración WSGI.

Haz clic en el enlace "WSGI configuration file" (en la sección "Code" en la parte de arriba de la página; se
llamará algo parecido a /var/www/<tu-usuario>_pythonanywhere_com_wsgi.py) y te redirigirá al editor, o tambien
lo puedes editar desde la consola web, eso está en /var/www

Lo que me ha funcionado es crear un proyecto desde la interfaz web y luego desde la pestaña web modificar las
rutas para que apunten al proyecto que clone, los estáticos del admin ya deben estar collectados antes de clonar un proyecto.

##### Tips #####

- El nombre de usuario que elijamos sera parte de nuestro subdominio en la web, es decir, si mi usuario es dm, el dominio de mi web/applicación sera:
--> dm.pythonanywhere.com es decir, cuando elijas tu nombre de usuario ten en cuenta que la URL de tu blog tendrá la forma
nombredeusuario.pythonanywhere.com, así que o bien elije tu propio apodo o bien un nombre que describa sobre qué trata tu blog.

- En /var/www está el fichero usuario_pythonanywhere_com_wsgi.py para editarlo, lo reemplazamos todo con lo siguiente:

import os
import sys

path = '/home/{mi usuario}/default'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "default.settings")

application = get_wsgi_application()

ó tambien esta que me ha funcionado:

# This file contains the WSGI configuration required to serve up your
# web application at http://dm.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Django project

import os
import sys

# add your project directory to the sys.path
project_home = u'/home/miusuario/nombre_del_proyecto'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'nombre_del_proyecto.settings'


# serve django via WSGI in Django < 1.7
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()
# serve django via WSGI in Django >= 1.7
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

En la pestaña de web se configura todo, la ruta de los estáticos, la ruta del proyecto, la versión de python, la ruta del
entorno virtual si se usa uno, por eso hay que configurar todo eso primero.

########################################
##### Graficando modelos de Django #####
########################################

Cuando desarrollas en Django la logica la mandas a los modelos. A veces nos abastraemos de la capa y lo que se escribe en la base de datos, para esto
siempre es bueno poder visualizar de manera gráfica los modelos del proyecto.

Para Django existe una orma de poder graficar los modelos con PyGraphviz, que es un software de visualización.

Para instalar PyGraphviz usaremos pip:

$ pip install pygraphviz

ya instalado la extensión, vamos a nuestro proyecto y ejecutamos:

my_project$ ./manage.py graph_models -a -g -o mi_modelo.png

Lo que nos creará un archivo PNG con el modelo de datos.

Si obtienes un error como

from django.conf import settings; ‘django_extensions’ in settings.INSTALLED_APPS
 
Es porque debes instalar django-extensions con:

$ pip install django django-extensions

Y luego debes agregar django-extensions a las INSTALLED_APPS en tu archivo settings.py de tu proyecto
 

INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)

###################################################
##### Definiendo todos los fields en la clase #####
###################################################

#En views.py
class PostCrear(SuccessMessageMixin,CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post_lista')
    success_message = "Se creó la publicación con éxito"

#En forms.py
class Meta:
    model = Post
    fields = '__all__'

ó

#En forms.py para incluírlos todos y excluir algunos.
class Meta:
    model = Post
    exclude = ('id',)

#############################################
##### Mensajes / messages al hacer post #####
#############################################

#En el views.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class PostLista(ListView):
    model = Post


class PostCrear(SuccessMessageMixin,CreateView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se creó la publicación con éxito"


class PostActualizar(SuccessMessageMixin,UpdateView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se actualizó la publicación con éxito"


class PostEliminar(SuccessMessageMixin,DeleteView):
    model = Post
    fields = ['autor', 'titulo', 'cuerpo', 'fecha']
    success_url = reverse_lazy('post_lista')
    success_message = "Se eliminó la publicación con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostEliminar, self).delete(request, *args, **kwargs)

#En el template:

{% if messages %}
  <ul class="messages">
    {% for message in messages %}
      <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
    {% endfor %}
  </ul>
{% endif %}

ó

{% if messages %}
  {% for message in messages %}
    <div class="alert alert-success" role="alert">
      {% if message.tags %}{% endif %}
      {{ message }}
    </div>
  {% endfor %}
{% endif %}

con close alert:

{% if messages %}
  {% for message in messages %}
    <div class="alert alert-success alert-dismissable">
      <a href="#" class="close" data-dismiss="alert" aria-label="close">×</a>
        <strong>
          {% if message.tags %}{% endif %}
          {{ message }}
        </strong>
    </div>
  {% endfor %}
{% endif %}

### En un render ###

messages = '¡Registro exitoso!'
return render_to_response('base.login.html', {'messages': messages})

En el template:

{% if messages %}
  <div class=" warning">
    {{ messages }}
  </div>
{% endif %}

#### Usando los tags en los mensajes para mostrar el tipo de mensaje #####

# views.py
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class Borrar(DeleteView):
    model = Persona
    success_url = reverse_lazy('registro:consultar')
    success_message = "Se elimino una persona con éxito"

    def delete(self, request, *args, **kwargs):
        #messages.success(self.request, self.success_message)
        #messages.warning(self.request, self.success_message)        
        #messages.info(self.request, self.success_message)
        #Falla con .danger por ahora :S
        return super(Borrar, self).delete(request, *args, **kwargs)

# base.html
{% if messages %}
  {% for message in messages %}
    <div class="alert alert-{{ message.tags }} alert-dismissable">
      <a href="#" class="close" data-dismiss="alert" aria-label="close">×</a>
        <strong>
          {% if message.tags %}{% endif %}
          {{ message }}
        </strong>
    </div>
  {% endfor %}
{% endif %}

##### Usando los tag en el crud de django #####

# view.py
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class Consultar(ListView):
    model = Persona


class Registrar(CreateView):
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')
    success_message = "Se agrego una persona con éxito"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, self.success_message)
        return super(Registrar, self).form_valid(form)


class Editar(UpdateView):
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')
    success_message = "Se actualizo una persona con éxito"

    def form_valid(self, form):
        self.object = form.save()
        messages.warning(self.request, self.success_message)
        return super(Editar, self).form_valid(form)


class Borrar(DeleteView):
    model = Persona
    success_url = reverse_lazy('registro:consultar')
    success_message = "Se elimino una persona con éxito"

    def delete(self, request, *args, **kwargs):
        #messages.success(self.request, self.success_message)
        #messages.warning(self.request, self.success_message)
        messages.info(self.request, self.success_message)
        return super(Borrar, self).delete(self, request, *args, **kwargs)

# base.html

{% if messages %}
  {% for message in messages %}
    <div class="alert alert-{{ message.tags }} alert-dismissable">
      <a href="#" class="close" data-dismiss="alert" aria-label="close">×</a>
        <strong>
          {% if message.tags %}{% endif %}
          {{ message }}
        </strong>
    </div>
  {% endfor %}
{% endif %}

#########################################
##### Uso de formularios / forms.py #####
########################################

#En el models.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Post(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=5000)
    fecha = models.DateField(default=datetime.now, help_text='')

    def __unicode__(self):
        return self.autor

    def get_absolute_url(self):
        return reverse('post_editar', kwargs={'pk': self.pk})

#En el forms.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from app_blog.models import Post
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'autor',
            'titulo',
            'cuerpo',
            'fecha',
        ]

        widgets = {
            'autor': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'titulo': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'cuerpo': forms.Textarea(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'fecha': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%;',
            }),
        }

##### Otra forma #####

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from app_blog.models import Post
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)


class PostForm(forms.ModelForm):

    autor = forms.CharField(widget=TextInput(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 50%; display: inline;',
        }), required = True)
    titulo = forms.CharField(widget=TextInput(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 50%; display: inline;',
        }), required = True)
    cuerpo = forms.CharField(widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 50%; display: inline;',
        }), required = True)

    class Meta:

        model = Post

        fields = [
            'autor',
            'titulo',
            'cuerpo',
        ]

#En el views.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from app_blog.forms import PostForm

class PostCrear(SuccessMessageMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_lista')
    success_message = "Se creó la publicación con éxito"

#####################################
##### Validación de formularios #####
#####################################

'''
Los validadores son funciones simples que toman un solo argumento y disparan un ValidationError
en el caso de que una entrada sea no válida. Estos nos sirven para crear alarmas cuando los usuarios
insertan información errónea en los campos de un formulario de nuestra app.

##### ¿Cómo crear un validador en Django? #####

Supongamos que queremos validar el campo cuerpo que tenemos disponible en nuestro modelo Post.
Lo primero que tenemos que hacer es declarar un método dentro de la misma clase (PostForm), en donde
definiremos toda nuestra lógica de validación para un campo del formulario en especifico.

Vamos a validar el numéro de caractéres mínimo del campo del cuerpo. Para eso definimos el método
clean_cuerpo, si el número de caractéres escrito en el formulario no es mayor a 3 no dejará guardar
los datos del formulario y mostrara el error "El cuerpo debe tener mas de 3 caractéres", de momento
solo lo mostrara si renderizamos el formulario completo {{ form }}.

Por convención debemos denominar nuestro método con el prefijo clean seguido del nombre del campo.
En nuestro caso seria clean_cuerpo

Siempre debemos obtener el diccionario de data que proviene del formulario de manera limpia, para eso
utilizamos la siguiente instrucción: cuerpo = self.cleaned_data['cuerpo']
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from app_blog.models import Post
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput
)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'autor',
            'titulo',
            'cuerpo',
        ]

        widgets = {
            'autor': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 100%; display: inline;',
            }),
            'titulo': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 100%; display: inline;',
            }),
            'cuerpo': forms.Textarea(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 100%; display: inline;',
            }),
        }

    def clean_cuerpo(self):
        """
        Método que verifica si el campo cuerpo es menor a 3 caractéres.
        """
        cuerpo = self.cleaned_data['cuerpo']

        if len(cuerpo) < 3:
            raise forms.ValidationError("El cuerpo debe tener mas de 3 caractéres")
        return cuerpo

    ##### Otra comparación #####

    def clean_cuerpo(self):
        """
        Método que verifica si el campo cuerpo coincide con una cadena arbitraria.
        """
        cuerpo = self.cleaned_data['cuerpo']

        if (cuerpo!='admin'):
            raise forms.ValidationError("El texto de cuerpo no coincide con la cadena")
        return cuerpo


    def clean_cuerpo(self):
        """
        Método que verifica si el campo cuerpo es diferente al campo título.
        """
        cuerpo = self.cleaned_data['cuerpo']
        titulo = self.cleaned_data['titulo']

        if (cuerpo!=titulo):
            raise forms.ValidationError("El texto de cuerpo no coincide con el texto del título")
        return cuerpo

##### Otras validaciones #####

def clean_username(self):
    """
    Método que valida si un nombre de usuario a registrar ya existe
    """
    username = self.cleaned_data['username']
    try:
        user_var = User.objects.get(username=username)
    except user_var.DoesNotExist:
        print "***** El usuario no existe *****"
        return username
    print "***** El usuario ya existe *****"

def clean_email(self):
    """
    Método que valida si el email a registrar ya existe
    """
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
        print "Este email ya está registrado"
        raise forms.ValidationError("Este email ya está registrado.")
    return email

##### Para que muestre el mensaje de error en el template usaremos un if #####

{% extends "base/base.html" %}
{% block titulo %}Crear{% endblock %}
{% block cuerpo %}
<h2>Publicar artículo</h2>
<div class="well well-post_list cuerpo_post">
    <form method="post">{% csrf_token %}
        <b>Autor:</b><br />
        {{ form.autor }}
        <br />
        <br />
        <b>Titulo:</b><br />
        {{ form.titulo }}
        <br />
        <br />
        <b>Contenido:</b><br />
        {{ form.cuerpo }}
        <!-- Mostrando mensaje cuando hay error -->
        {% if form.cuerpo.errors %}
            <p>{{ form.cuerpo.errors}}</p>
        {% endif %}
        <br />
        <br />
        {{ form.fecha }}
        <a href="{% url 'post_lista' %}"><button type="button" class="btn btn-primary">Volver</button></a>
        <button class="btn btn-info" type="reset">Limpiar</button>
        <button class="btn btn-success" type="submit">Publicar</button>
    </form>
</div>
{% endblock %}

##################################################
##### forms.py para el modelo User de django #####
##################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
  

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user

#######################################################
###### Método save del UserCreationForm de django #####
#######################################################

class UserForm(UserCreationForm):
    """
    Clase del formulario que registra los usuarios
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name',  'email', 'username', 'password1', 'password2')

    first_name = forms.CharField(
        label=("Nombres"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'required': 'true',
            'title':'Ingrese su nombre completo',
            'id': 'first_name',
            'data-toggle': 'tooltip',
            'placeholder': 'Nombres'
        })
    )
    
    last_name = forms.CharField(
        label=("Apellidos"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'required': 'true',
            'title':'Ingrese sus apellidos completo',
            'id': 'last_name',
            'data-toggle': 'tooltip',
            'placeholder': 'Apellidos'
        })
    )

    email = forms.CharField(
        label=("Email"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'Dirección de correo',
            'required': 'true',
            'data-toggle': 'tooltip',
            'title':'Ingrese su email',
            'id': 'email',
        })
    )

    username = forms.CharField(max_length=30, label=("Usuario"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Nombre de usuario',
            'title':'Ingrese el nombre de usuario',
            'data-toggle': 'tooltip',
            'id': 'username',
        })
    )

    password1 = forms.CharField(
        label=("Contraseña"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Contraseña',
            'title':'Ingrese la contraseña de su preferencia',
            'data-toggle': 'tooltip',
            'id': 'password1',
        })
    )

    password2 = forms.CharField(
        label=("Contraseña (confirmación)"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'required': 'true',
            'placeholder': 'Vuelva a ingresar la contraseña elegida',
            'data-toggle': 'tooltip',
            'id': 'password2',
        })
    )

    def save(self, commit = True):
        """
        Metodo que crea el objeto usuario en la db y guarda los valores del
        formulario, también establece la condicion de estatus inactivo del usuario.
        """
        user = User.objects.create_user(self.cleaned_data['username'],
                                     self.cleaned_data['email'],
                                     self.cleaned_data['password1'])
        user.is_active = False
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

# Otra forma

class RegisterForm(UserCreationForm):
    """
    Clase del formulario que registra los usuarios
    """

    username = forms.CharField(max_length=30, label=("Usuario"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }))

    first_name = forms.CharField(label=("Nombres"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }))

    last_name = forms.CharField(label=("Apellidos"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }))

    email = forms.CharField(label=("Email"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }))

    password1 = forms.CharField(label=("Contraseña"), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }))

    password2 = forms.CharField(label=("Contraseña (confirmación)"), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name',  'email', 'username', 'password1', 'password2')

##############################################
##### Pasando varios parametros a la url #####
##############################################

# En el template
<td>
   <a href="{% url 'search' pk id_x id_y %}"><button class="btn btn-success">Detail
</td>

# En la url
url(r'^search/(?P<pk>\d+)/(?P<id_x>\d+)/(?P<id_y>\d+)$', ParticipacionCreate.as_view(), name = "search"),

###################
##### Filtros #####
###################

Los filtros de plantillas son formas simples de alterar el valor de una variable antes de mostrarla.
Los filtros se parecen a esto:

{{ nonmbre|lower }}

Esto muestra el valor de {{ nombre }} después de aplicarle el filtro lower, el cual
convierte el texto a minúscula. Usa una pipe o tubería (|) para aplicar el filtro.

Los filtros pueden ser encadenados, esto quiere decir que, la salida de uno de los
filtros puede ser aplicada al próximo. Aquí un ejemplo que toma el primer elemento
de una lista y la convierte a mayusculas:

{{ mi_lista|first|upper }} 

Algunos filtros toman argumentos.
Un filtro con argumentos se ve de este modo:
 
{{ bio|truncatewords:"30" }}

Esto muestra las primeras 30 palabras de la variable bio. Los argumentos de los
filtros están siempre entre comillas dobles.

##### Herencia de plantillas #####

Para trabajar correctamente en Django se usará el sistema de plantillas para crear páginas HTML
enteras, sin este tipo de sistemas de plantillas nos preguntaríamos ¿Cómo reducimos la duplicación y la redundancia
de las áreas comunes de las páginas, como por ejemplo, los paneles de navegación?
Una forma clásica de solucionar este problema es usar includes, insertando dentro
de las páginas HTML a "incluir" una página dentro de otra. Es más, Django admite
esta aproximación, con la etiqueta {% include %} Pero la
mejor forma de solucionar este problema con Django es usar una estrategia más
elegante llamada herencia de plantillas.
En esencia, la herencia de plantillas te deja construir una plantilla base "esqueleto"
que contenga todas las partes comunes de tu sitio y definir "bloques" que las
plantillas hijas puedan sobrescribir.

Ejemplo de plantilla base:

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>
      {% block title %}Base{% endblock %}
    </title>
    {% load staticfiles %}
    <link rel="stylesheet" type="text/css" href="{% static 'bootstrap/css/bootstrap.min.css' %}" />
    <link rel="stylesheet" type="text/css" href="{% static 'css/theme.css' %}" />
  </head>
  <body>
    <div class="container theme-showcase" role="main">
      {% block header %}
        <h1>Header</h1>
      {% endblock %}
      <br />
      {% block body %}
        <h1>body</h1>
      {% endblock %}
      <br />
      {% block footer %}
        <h1>footer</h1>
      {% endblock %}
    </div>
  </body>
</html>

{% extends "base/base.html" %}
{% block title %}Demo{% endblock %}
{% block header %}
<!-- Sobreescribiendo el contenido de los bloques -->
  <h1>hhh</h1>
{% endblock %}
<br />
{% block body %}
  <h1>bbb</h1>
{% endblock %}
<br />
{% block footer %}
  <h1>fff</h1>
{% endblock %}

#########################################
##### Etiqueta include en templates #####
#########################################

{% include %} Esta etiqueta te permite incluir el contenido de otra plantilla. El
argumento para esta etiqueta debería ser el nombre de la plantilla a incluir, y el
nombre de la plantilla puede ser una variable string hard-coded (entre comillas),
entre simples o dobles comillas. En cualquier momento que tengas el mismo código
en varias etiquetas, considera utilizar la etiqueta {% include %} para eliminar la
redundancia entre las plantillas.
Estos dos ejemplos incluyen el contenido de la plantilla nav.html. Los ejemplos son
equivalentes e ilustran que cualquier modo de comillas está permitido:
 
{% include 'nav.html' %}
{% include "nav.html" %}

Por convención las plantillas que van a ser incluidas se guardan en un
directorio "includes". En el ejemplo incluímos el contenido de la plantilla includes/nav.html:

{% include 'includes/nav.html' %}

####################
##### render() #####
####################

La función llamada render(), se encuentra en el módulo django.shortcuts.

Es un idioma muy común para cargar una template llenar un contexto y retornar un objeto HttpResponse con el resultado
de una template renderizada.

La función render toma como primer argumento la solicitud (objeto request), el nombre de una template como segundo
argumento y un diccionario como tercer argumento. Este devuelve un objeto HttpResponse de la template solicitada renderizada
con el contexto dado.

################################
##### render_to_response() #####
################################

El primer argumento de render_to_response() debe ser el nombre de la plantilla a utilizar.
El segundo argumento, si es pasado, debe ser un diccionario para usar en la creación de un Context para esa plantilla.
Si no se le pasa un segundo argumento, render_to_response() utilizará un diccionario vacío.

###############################################################
##### Agregar nuestros modelos al sitio del administrador #####
###############################################################

Para poder agregar, cambiar y borrar objetos en las tablas de la base de datos usando la interfaz
por defecto del administrador de Django es necesario declarar esos modelos en un fichero específico.

Dentro del directorio interno algún proyecto generado (project/app), existe un archivo
vacio llamado admin.py, creado automáticamente por el comando startapp
agreguémosle las siguientes líneas de código, para registrar nuestros tres modelos:

En app/admin.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Mymodel, MyModel2

admin.site.register(Mymodel)
admin.site.register(MyModel2)

Y si recargamos la interfáz de administración ya podremos listar los objetos de nuestras tablas de la base de datos.

#####################################################
##### Estatus de usuarios en el admin de django #####
#####################################################

La opción "Activo" define si el usuario está activo en todo sentido. Si está
desactivada, el usuario no tendrá acceso a ninguna URL que requiera
identificación.

La opción Es "staff" indica que el usuario está habilitado a ingresar a la interfaz
de administración (por ejemplo, indica que el usuario es considerado un
miembro del staff en tu organización). Como el mismo sistema de usuarios
puede usarse para controlar el acceso al sitio público (es decir, sitios
restringidos no administrativos. Mira él capítulo 12.), esta opción diferencia
entre usuarios públicos y administradores.

La opción es "superusuario" da al usuario completo e irrestricto acceso a todos
los elementos de la interfaz de administración, y sus permisos regulares son
ignorados.

#################################################
##### Integracions de postgresql con django #####
#################################################

# aptitude install postgresql postgresql-server libpq-dev python-dev

# aptitude install python-psycopg2

# pip install postgres

# pip install db-psycopg2

# pip install psycopg2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'name_db',  # Or path to database file if using sqlite3.
        'USER': 'owner_bd',  # Not used with sqlite3.
        'PASSWORD': 'password_bd',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
    }
}

####################################################################
##### Generar json a partir de un modelo (dumpdata y loaddata) #####
####################################################################

Generar un fichero json con los datos de los modelos de una aplicación:

$ python manage.py dumpdata app_name > data.json

Generar un fichero json con a partir de un modelo específico de la aplicación:

$ python manage.py dumpdata app_name.model_name > data.json

Esta generación por lo general es usada para crear un json con data inicial
que puede ser cargada en la db si necesidad de hacer un volvado de datos.
De esta manera podemos tener usuarios, permisos u otro tipo de data que seran cargados
automáticamente a partir de un comando:

$ python manage.py loaddata initial_data.json

Ejemplo:

Generamos un proyecto en django, migramos y creamos un usuario administrador, ahora vamos a generar
un fichero que tendra los datos del usuario creado, y haremos referencia al modelo que gestiona los usuarios

$ python manage.py dumpdata auth.user > auth_user.json

En ese fichero json estan los datos de usuario que se creo

Borramos la db, la volvemos a generar con migrate, como es obvio esta nueva db no tiene usuarios creados, entonces:

$ python manage.py loaddata auth_user.json

Installed 1 object(s) from 1 fixture(s) # Sera el mensaje si agregó el usuario con éxito

Con esto ya estará disponible el usuario en la db con todos los demas datos que corresponden a ese modelo.

Es posible hacer un dumpdata de todos los modelos en general, no especificando un modelo en particula

$ python manage.py dumpdata > data.json

##### Especificando app #####

$ python manage.py dumpdata app > app.json

##### Especificando tabla #####

$ python manage.py dumpdata app.table > app_table.json

##### Excluyendo modelos #####

$ python manage.py dumpdata --exclude auth.permission > db.json

##### Indentando la data #####

$ python manage.py dumpdata --indent 2 > data.json

##### Dando formato al fichero #####

$ python manage.py dumpdata auth.user --indent 2 --format xml > user.xml

################################
##### Relaciones en Django #####
################################

Ejemplo de como hacer una relacion triple, usando estados, municipios y parroquias.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Entidad(models.Model):
    """!
    Clase que contiene los Estados
    """
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        """!
        Método que muestra la información sobre el Estado
        """
        return self.nombre


class Municipio(models.Model):
    """!
    Clase que contiene los Municipios
    """
    codigo = models.CharField(max_length=50)
    entidad = models.ForeignKey(Entidad)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        """!
        Método que muestra la información sobre el Municipio
        """
        return self.nombre


class Parroquia(models.Model):
    """!
    Clase que contiene las Parroquias
    """
    codigo = models.CharField(max_length=50)
    Municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        """!
        Método que muestra la información sobre la Parroquia
        """
        return self.nombre

-----

from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)

#########################################################
##### Serialización de consultas de django con json #####
#########################################################

from django.contrib.auth.models import User
from django.http import HttpResponse
import json


def index(request):
    """
    Index view, to tray.
    """
    # Consultamos todos los usuarios
    usuarios = User.objects.all()
    #print usuarios
    # Covertimos los objetos del query en una lista mas limpia
    lista = [{'pk': x.pk,'username': x.username} for x in usuarios]
    #print lista
    # Convertimos la lista en un json
    serializado = json.dumps(lista)
    #print serializado
    # Descerializamos el json
    deserializado = json.loads(serializado)
    print deserializado
    return HttpResponse("Hello, world!")

################################################
##### ALLOWED_HOSTS = [] en el settings.py #####
################################################

Es una variable que contiendrá una lista de cadenas que representan los nombres
de host/dominio que ese sitio de Django puede servir.

Esta es una medida de seguridad para evitar ataques de encabezado HTTP Host, que son posibles
incluso bajo muchas configuraciones de servidor web aparentemente seguras.

###########################################################
##### Sobrescribiendo métodos de las clases genéricas #####
###########################################################

Las clases genéricas de Django simplifican el tiempo de creación de aplicaciones, puesto que
están predefinidas para realizar acciones específicas como crear, leer, eliminar, y detallar objetos,
pero a veces necesitamos realizar tareas mas complejas que van mas allá de lo que nos ofrecen por defecto
algunas de estas clases, es por ello que es común sobrescribir los métodos de estas clases y adaptarlos a
las necesidades que se tengan.

Para encontrar ejemplos de las cláses y su métodos: --> https://ccbv.co.uk/projects/Django/1.11/

# Ejemplo: Creando un post en una aplicación tipo blog y usando los métodos por defecto.

class PostCrear(SuccessMessageMixin,CreateView):
    """
    Clase que permite crear un post
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_lista')
    success_message = "Se creó la publicación con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método de la clase que imprime cuando se accede por get a la clase para crear posts
        """
        self.object = None
        print "Accediendo por GET"
        return super(PostCrear, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """
        Método de la clase que imprime que usuario creó la publicación
        """
        self.object = None
        print "********************************"
        print "Usuario:("+(request.user.username)+") creo la publicacion con exito"
        print "********************************"
        return super(PostCrear, self).post(request, *args, **kwargs)

########################
##### http y https #####
########################

Es común que cuando un proyecto esté en producción se protejan
los accesos a las páginas usando certificados ssl y se pueda
navegar usando https, pero en realidad solo es necesario en las
páginas donde se envian datos, como puede ser un login o un formulario
de consulta, o las páginas del administrador, las cuales si deben
cifrarse por seguridad, entonces podemos usar la variable SECURE_SSL_REDIRECT
como True en el settings, que hace que  todo vaya por https, y la variable
SECURE_REDIRECT_EXEMPT que es una lista de las urls que no queremos que
vayan por https, para nuestro cas necesitamos lo opuesto, entoncesagregando una
expresión regular con negación al valor de la variable logramos que
hiciera lo contrario , entonces quedaría así:

SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = ['^(?!admin).*$']

Usando entonces el middleware de django por defecto, y esas dos variables
logramos que todo lo que vaya desde /admin será con https.

Para un set mas configurable se puede usar el middleware personalizado:
--> https://github.com/argenisosorio/django_ssl_secure_redirect
En sustitución del middleware de django.

##############################################################
##### Clases y funciones para crear un usuario de Django #####
##############################################################

#urls.py
url(r'^crear_usuario/$', UsuarioCreate.as_view(), name='registro'),

#forms.py
class UserForm(UserCreationForm):
    """
    Clase del formulario que registra los usuarios
    """
    first_name = forms.CharField(
        label=("Nombres"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'required': 'true',
            'title':'Ingrese su nombre completo',
            'id': 'first_name',
            'data-toggle': 'tooltip',
            'placeholder': 'Nombres',
        })
    )
    
    last_name = forms.CharField(
        label=("Apellidos"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'required': 'true',
            'title':'Ingrese sus apellidos completo',
            'id': 'last_name',
            'data-toggle': 'tooltip',
            'placeholder': 'Apellidos',
        })
    )

    email = forms.CharField(
        label=("Email"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'Dirección de correo',
            'required': 'true',
            'data-toggle': 'tooltip',
            'title':'Ingrese su email',
            'id': 'email',
        })
    )

    username = forms.CharField(max_length=30, label=("Usuario"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Nombre de usuario',
            'title':'Ingrese el nombre de usuario',
            'data-toggle': 'tooltip',
            'id': 'username',
        })
    )

    password1 = forms.CharField(
        label=("Contraseña"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Contraseña',
            'title':'Ingrese la contraseña de su preferencia',
            'data-toggle': 'tooltip',
            'id': 'password1',
        })
    )

    password2 = forms.CharField(
        label=("Contraseña (confirmación)"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'required': 'true',
            'placeholder': 'Vuelva a ingresar la contraseña elegida',
            'data-toggle': 'tooltip',
            'id': 'password2',
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name',  'email', 'username', 'password1', 'password2',)

    def clean_username(self):
        """
        Método que verifica si el campo username es menor a 3 caractéres.
        Autor: Argenis Osorio (aosorio@cenditel.gob.ve)
        Fecha: 19-05-2017
        """
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError("El username debe tener mas de 3 caractéres")
        return username

    def clean_email(self):
        """
        Método que valida si el email a registrar ya existe
        Autor: Argenis Osorio (aosorio@cenditel.gob.ve)
        Fecha: 19-05-2017
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email

#views.py
class UsuarioCreate(SuccessMessageMixin,CreateView):
    """
    Clase que registra los usuarios del sistema
    Autor: Argenis Osorio (aosorio@cenditel.gob.ve)
    Fecha: 22-05-2017
    """
    model = User
    form_class = UserForm
    template_name = "registro.html"
    success_url = reverse_lazy('usuario:acceso')
    success_message = "¡Registro exitoso! debe esperar la activacion de su cuenta"

    def form_valid(self,form):
        """
        Método que verifica si el formulario es válido, en cuyo caso procede a registrar los datos del usuario.
        Autor: Argenis Osorio (aosorio@cenditel.gob.ve)
        Fecha: 22-05-2017
        """
        self.object = form.save(commit=False)
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.set_password(form.cleaned_data['password1'])
        self.object.email = form.cleaned_data['email']
        self.object.is_active = 0
        self.object.save()

        return super(UsuarioCreate, self).form_valid(form)


##########################################################################
##### Clases y funciones para editar el perfil del usuario de Django #####
##########################################################################

#urls.py
url(r'^perfil/(?P<pk>\d+)$', login_required(views.edit_profile), name="perfil"),

#forms.py
class EditProfileForm(forms.ModelForm):
    """
    Clase del formulario que permite editar el perfil del usuario autenticado.
    Autor: Argenis Osorio (aosorio@cenditel.gob.ve)
    Fecha: 03-04-2017
    """
    first_name = forms.CharField(
        label=("Nombres"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            #'required': 'true',
            'title':'Ingrese su nombre completo',
            'id': 'first_name',
            'data-toggle': 'tooltip',
            'placeholder': 'Nombres',
        })
    )
    
    last_name = forms.CharField(
        label=("Apellidos"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            #'required': 'true',
            'title':'Ingrese sus apellidos completo',
            'id': 'last_name',
            'data-toggle': 'tooltip',
            'placeholder': 'Apellidos',
        })
    )

    email = forms.CharField(
        label=("Email"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'Dirección de correo',
            'required': 'true',
            'data-toggle': 'tooltip',
            'title':'Ingrese su email',
            'id': 'email',
        })
    )

    username = forms.CharField(max_length=30, label=("Usuario"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'placeholder': 'Nombre de usuario',
            'title':'Ingrese el nombre de usuario',
            'data-toggle': 'tooltip',
            'id': 'username',
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name',  'email', 'username',)

#views.py
def edit_profile(request, pk):
    """
    Función que permite editar el perfil del usuarios autenticado.
    Autor: Argenis Osorio (argenisosorio580@hotmail.com)
    Fecha: 20-03-2017
    """
    user = User.objects.get(pk=request.user.pk)
    if request.method == 'GET':
        form = EditProfileForm(instance=user)
    else:
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        messages = '¡Perfil actualizado!'
        return render_to_response('user_profile.html', {'form': form, 'messages': messages}, context_instance=RequestContext(request))
    return render(request, 'user_profile.html', {'form':form})

ó
#views.py con clases genéricas
class PerfilUpdate(SuccessMessageMixin,UpdateView):
    """
    Clase que gestiona la actualización del perfil
    """
    model = User
    template_name = "user_profile.html"
    form_class = EditProfileForm
    success_message = "¡Perfil actualizado!"

    def dispatch(self, request, *args, **kwargs):
        """
        Metodo que redirecciona al usuario si no cuenta con los permisos
        """
        if int(self.request.user.id) != int(self.kwargs['pk']):
           return render_to_response('home.template.html',context_instance=RequestContext(request))
        return super(PerfilUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        """
        Metodo que permite definir la url con el pk del usuario autenticado.
        """
        return reverse_lazy('usuario:perfil', kwargs={'pk': self.kwargs['pk']})

    def get_initial(self, **kwargs):
        """
        Metodo para agregar valores de inicio al formulario
        """
        initial = super(PerfilUpdate, self).get_initial()
        usuario = User.objects.get(pk=self.request.user.pk)
        initial['username'] = usuario.username
        initial['first_name'] = usuario.first_name
        initial['last_name'] = usuario.last_name
        initial['email'] = usuario.email
        return initial

    def form_valid(self,form):
        """
        Metodo que valida si el formulario es valido
        """
        self.object = form.save()
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.save()

        return super(PerfilUpdate, self).form_valid(form)

####################################
##### Redirigir una url a otra #####
####################################

from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^some-page/$', RedirectView.as_view(url='/')),

####################################################################
##### Usando el select field para leer de datos de otro modelo #####
####################################################################

#models.py
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Familia(models.Model):
    familiar = models.CharField(max_length=200)

    def __unicode__(self):
        return self.familiar


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=8)
    persona_familiar = models.ForeignKey(Familia)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('registro:editar', kwargs={'pk': self.pk})

#views.py
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona


class Consultar(ListView):
    model = Persona


class Registrar(CreateView):
    model = Persona
    fields = '__all__'
    success_url = reverse_lazy('registro:consultar')


class Editar(UpdateView):
    model = Persona
    fields = '__all__'
    success_url = reverse_lazy('registro:consultar')


class Borrar(DeleteView):
    model = Persona
    success_url = reverse_lazy('registro:consultar')

################################################################
##### Ejemplo de instanciar otro modelo en un select field #####
################################################################

# models.py
class Proyecto(models.Model):
    """
    Modelo que contiene los campos de un Proyecto.
    """
    nombre_proyecto = models.CharField(max_length=400, blank=True,null=True)

    def __unicode__(self):
        return self.nombre_proyecto

    def get_absolute_url(self):
        return reverse('registro:editar_reporte', kwargs={'pk': self.pk})


class Reporte(models.Model):
    """
    Modelo de un Reporte de actividades de un proyecto.
    """
    autor = models.CharField(max_length=400, blank=True,null=True)
    nombre_proyecto = models.CharField(max_length=400, blank=True,null=True)

    def __unicode__(self):
        return self.autor

    def get_absolute_url(self):
        return reverse('registro:editar_reporte', kwargs={'pk': self.pk})

# forms.py
class ProyectoForm(forms.ModelForm):
    """
    Formulario con los campos de un Proyecto.
    """
    nombre_proyecto = forms.CharField(label='Nombre del Proyecto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:

        model = Proyecto
        fields = '__all__'

class ReporteForm(forms.ModelForm):
    """
    Formulario con los campos de un Reporte de actividades de un proyecto.
    """

    def __init__(self, *args, **kwargs):
        """
        Método que carga la data de los proyectos registrados
        del modelo Proyecto en el campo nombre_proyecto del
        modelo Reporte.
        """
        super(ReporteForm, self).__init__(*args, **kwargs)
        lista_proyectos = Proyecto.objects.all().values_list('nombre_proyecto','nombre_proyecto')
        self.fields['nombre_proyecto'] = forms.ChoiceField(label="Nombre del Proyecto", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_proyectos)

    autor = forms.CharField(label='Autor', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    nombre_caravisible = forms.CharField(label='Nombre completo del/la Cara Visible', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

###################################################
##### Imprimiento la fecha y hora del sistema #####
###################################################

from datetime import datetime

print datetime.now()
                       
# Cambiando el formato a humano
                       
from datetime import datetime

#print datetime.now()
myDate = datetime.now()
formatedDate = myDate.strftime("%d-%m-%Y %H:%M")
b = str(formatedDate)
print b

##################################################
##### Imprimiendo las acciones de un usuario #####
##################################################

# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona
from datetime import datetime


class Consultar(ListView):
    """
    Clase que muestra la lista de personas registradas
    """
    model = Persona

    def get(self, request, *args, **kwargs):
        """
        Método que muestra cual usuario y cuando visito la lista de personas.
        """
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object_list=self.object_list)
        print "***** El usuario: "+str(request.user)+", visito la lista de personas el: "+str(datetime.now())+" *****"
        return self.render_to_response(context)


class Registrar(CreateView):
    """
    Clase que permite registrar personas
    """
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')

    def form_valid(self, form):
        """
        Método que muestra cual usuario y cuando registro a una persona
        """
        self.object = form.save()
        print "***** El usuario: "+str(self.request.user)+", registro una persona el: "+str(datetime.now())+" *****"
        return super(Registrar, self).form_valid(form)


class Editar(UpdateView):
    """
    Clase que permite editar a las personas
    """
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')

    def form_valid(self, form):
        """
        Método que muestra cual usuario y cuando actualizo a una persona
        """
        self.object = form.save()
        print "***** El usuario: "+str(self.request.user)+", actualizo una persona el: "+str(datetime.now())+" *****"
        return super(Editar, self).form_valid(form)


class Borrar(DeleteView):
    """
    Clase que permite eliminar una persona
    """
    model = Persona
    success_url = reverse_lazy('registro:consultar')

    def delete(self, request, *args, **kwargs):
        """
        Método que muestra cual usuario y cuando elimino a una persona
        """
        print "***** El usuario: "+str(self.request.user)+", elimino a una persona el: "+str(datetime.now())+" *****"
        return super(Borrar, self).delete(self, request, *args, **kwargs)

########################################
##### Creando una bitácora de logs #####
########################################

"""
Creamos un modelo Bitacora, y hacemos un query para crear un objeto al realizar una acción específica.
Para este ejemplo crea una entrada en la bitacora cuando visita una vista y guarda el usuario y la fecha.
Así, si editamos el admin.py podemos ver la bitácora desde el admin, y podemos ordenar mejor el modelo,
agregando fecha y hora por ejemplo.
"""

# models.py
class Bitacora(models.Model):
    entrada = models.CharField(max_length=200)

    def __unicode__(self):
        return self.entrada

# views.py
from registro.models import Bitacora


def index(request):
    a = "El usuario: "+str(request.user)+", accedio al index: "+str(datetime.now())
    Bitacora.objects.create(entrada=a)
    return render_to_response('registro/index.html', context_instance=RequestContext(request))

#################################################
##### Usando las querys(consultas) QuerySet #####
#################################################

Un QuerySet es una lista de objetos de un modelo determinado. Un QuerySet te permite leer los
datos de una base de datos, filtrarlos y ordenarlos.

# Abrimos la consola interactiva de python que provee Django
$ python manage.py shell

# Importamos el modelo a consultar, en este caso consultaremos los objetos registrados del model User de Django
>>> from django.contrib.auth.models import User

# Si hay usuarios registrados nos mostrará la lista de objetos guardados
>>> User.objects.all()
[<User: admin>, <User: aosorio>, <User: dasd>, <User: dasdasd>, <User: dasda>]

##### Crear objeto #####

'''
En este ejemplo tenemos un modelo Persona, con dos campos, nombre y cedula.
'''

# Importamos el modelo
>>> from registro.models import Persona

# Listamos los objetos
>>> Persona.objects.all()
[<Persona: aosorio>, <Persona: maria>]

# Insertamos un nuevo objeto
>>> Persona.objects.create(nombre='karla', cedula=12345678)
<Persona: karla>

# Listamos los objetos de nuevo, vemos que hay uno nuevo, el que creamos.
>>> Persona.objects.all()
[<Persona: aosorio>, <Persona: maria>, <Persona: karla>]

##### Creando usuarios de django #####

>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
>>> user.last_name = 'Lennon'
>>> user.save()

##### Filtrar objetos #####

'''
Una parte importante de los QuerySets es la habilidad para filtrarlos. Digamos que queremos encontrar
todos los posts cuyo autor es el User ola. Usaremos filter en vez de all.
'''

# Filtrar cuando un objeto con el campo username coincída con la cadena.
>>> User.objects.filter(username='admin')
[<User: admin>]

# Filtrar cuando un objeto con el id coincída con el número.
>>> User.objects.filter(id=1)
[<User: admin>]

# Filtrar cuando un objeto contenga la cadena descrita.
>>> User.objects.filter(username__icontains='ad')
[<User: admin>]

##### Ordenando objetos #####

'''
Los QuerySets también te permiten ordenar la lista de objetos. Intentemos ordenarlos por el campo
'''

>>> Persona.objects.all()
[<Persona: aosorio>, <Persona: maria>, <Persona: karla>]

# Ordenar los objetos por id
>>> Persona.objects.order_by('id')
[<Persona: aosorio>, <Persona: maria>, <Persona: karla>]

# Con un - antes podemos invertir el ordenamiento
>>> Persona.objects.order_by('-id')
[<Persona: karla>, <Persona: maria>, <Persona: aosorio>]

# Ordenar los objetos por cedula
>>> Persona.objects.order_by('cedula')
[<Persona: maria>, <Persona: karla>, <Persona: aosorio>]

# Contar todos los objetos
x = Persona.objects.count()
print x

# Contar todos los objetos que contengan admin en el username
x = Persona.objects.filter(username__icontains='admin').count()

##### Limitando el número de objetos a consultar #####

# Mostrar solo 5 objetos
>>> Persona.objects.all()[:5]

# Mostrar solo 2 objetos
>>> Persona.objects.all()[:2]

##### Mostrar los objetos de la lista #####

>>> Persona.objects.all()[0]
<Persona: aosorio>

>>> Persona.objects.all()[1]
<Persona: maria>

>>> Persona.objects.all()[2]
<Persona: karla>

# Mostrar objetos en un rango
>>> Persona.objects.all()[5:10]
<Persona: karla>

##### Ejemplo de queryset para filtrar objetos #####

class BitacoraView(ListView):
    """
    Clase que muestra la lista de entradas de la bitácora
    """
    model = Bitacora
    template_name = "bitacora.html"

    def get_queryset(self):
        """
        Método que filtra los datos de la tabla, solo muestra si coincide con el filtro
        """
        #queryset = Bitacora.objects.filter(tipo='Actualización')
        queryset = Bitacora.objects.filter(tipo='Acceso')
        return queryset

---

def Consulta_datos(request, template_name='app/template.html'):
    """
    Función que permite aplicar 2 veces un filtro con los querysets
    """
    a = MyModel.objects.filter(campo1__icontains='varchar')
    b = a.filter(campo2__icontains='varchar')
    data = {}
    data['object_list'] = b
    print data
    return render(request,template_name, data)

#################################
##### search form in django #####
#################################

#urls.py
# -*- coding: utf-8 -*-
from django.conf.urls import url
from app import views
from app.views import *
import app.views as views
from .views import AppTemplate

urlpatterns = [
    url(r'^$', AppTemplate.as_view(), name='app'),
    url(r'^buscar/$', buscar, name='buscar'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
]

-----

#models.py
# -*- coding: utf-8 -*-
from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=8)

    def __unicode__(self):
        return self.nombre

-----

#views.py
# -*- coding: utf-8 -*-
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import *
from django.core.urlresolvers import *
from .models import *


class AppTemplate(TemplateView):
    template_name = "app/index.html"

 
def buscar(request):
    return render(request, 'app/buscar.html')


def busqueda(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        personas = Persona.objects.filter(nombre__icontains=q)
        return render(request, 'app/buscar.html',  {'personas': personas, 'query': q})
    else:
        return HttpResponse('Por favor introduce un termino de búsqueda.')

-----

#buscar.html
{% extends "base/base.html" %}
{% block titulo %}Buscar{% endblock %}
{% block cuerpo %}
<h3>Buscar persona por nombre</h3>
<form action="/busqueda/" method="get">
  <input type="text" name="q">
  <input type="submit" value="Buscar">
</form>
{% if personas %}
<p>Estas buscado: <strong>{{ query }}</strong></p>
  <p>Personas encontradas: {{ personas|length }} personas.</p>
  <ul>
    {% for x in personas %}
      <li>{{ x.nombre }} | {{ x.cedula }}</li>
    {% endfor %}
  </ul>
{% else %}
  <p>Ningúna persona coincide con el criterio de búsqueda.</p>
{% endif %}
{% endblock %}

##################################################
##### search form in django con doble filtro #####
##################################################

# urls.py
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
import registro.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^buscar/$', login_required(views.Buscar_reporte.as_view()), name='buscar'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
)

# views.py
class Buscar_reporte(TemplateView):
    """
    Plantilla que tiene el formulario para buscar.
    """
    template_name = "registro/buscar.html"


def busqueda(request):
    """
    Función que recibe los parámetros enviados desde el formulario de
    búsqueda y filtra los con querysets.
    """
    if 'ano' in request.GET and request.GET['ano'] and 'mes' in request.GET and request.GET['mes']:
        ano = request.GET['ano']
        mes = request.GET['mes']
        reportes_ano = Reporte.objects.filter(ano__icontains=ano)
        reportes = reportes_ano.filter(mes__icontains=mes)
        return render(request, 'registro/busqueda.html',  {'reportes': reportes, 'query': ano,'query2': mes})
    else:
        return HttpResponse('Por favor introduce un termino de búsqueda.')

# buscar.html
{% extends "base/base.html" %}
{% block titulo %}Buscar{% endblock %}
{% block cuerpo %}
<br />
<h1>Buscar</h1>
<br />
<form action="{% url 'registro:busqueda' %}" method="get">
  <label>Por Año</label>
  <br />
  <select class="form form-control" name="ano">
    <option value="-">-</option>
    <option value="2018">2018</option>
    <option value="2019">2019</option>
  </select>
  <br />
  <label>Por Mes</label>
  <br />
  <select class="form form-control" name="mes">
    <option value="-">-</option>
    <option value="Enero">Enero</option>
    <option value="Febrero">Febrero</option>
  </select>
  <button class="btn btn-success" type="submit">Buscar</button>
</form>
{% endblock %}

# busqueda.html
{% extends "base/base.html" %}
{% block titulo %}Resultados de la búsqueda{% endblock %}
{% block cuerpo %}
<br />
<h1>Resultados de la búsqueda</h1>
<br />
{% if reportes %}
  <p>Estas buscado objetos del Año <strong>{{ query }}</strong> en el Mes de <strong>{{ query2}}</strong></p>
  <p>Objetos encontrados: <strong>{{ reportes|length }}</strong>
  <br />
  <br />
  <table border="1px" id="example" class="display" cellspacing="0px" style="width:100%;">
    <thead>
      <tr>
        <th>N</th>
        <th>xxx</th>
      </tr>
    </thead>
    <tfoot>
      <tr>
        <th>N</th>
        <th>xxx</th>
      </tr>
    </tfoot>
    <tbody>
    {% for x in reportes %}
    <tr>
      <td></td>
      <td>{{ x.nombre_proyecto }}</td>
      <td>{{ x.xxx }}</td>
    </tr>
    {% endfor %}
    </tbody>
  </table>
{% else %}
  <p>Ningún objeto coincide con el criterio de búsqueda.</p>
{% endif %}
{% endblock %}

#####################
##### form.as_p #####
#####################

form.as_p nos permite renderizar un formulario de manera ordenada, tipo
párrafo o tabla sin necesidad deincluir mas nada. Los unicos requerimientos
es que en el forms.py estén descritas las clases de las que va a heredar, así
como los otros atributos propios como label, requiered, etc.

<form method="post">{% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="Submit" />
</form>

##############################################
##### Usando los labels en el formulario #####
##############################################

<form method="post">{% csrf_token %}
    {{ form.username.label }}
    <br />
    {{ form.username }}
    <br />
    {{ form.password.label }}
    <br />
    {{ form.password }}
    <br />
    <button class="btn btn-info" type="reset">Limpiar</button>
    <button class="btn btn-success" type="submit">Entrar</button>
  </form>

#############################################
##### Ejemplo de .gitignore para Django #####
#############################################

*.*.backup
*.*~
*.tar.gz
*.pyc
*.pyo
*.log
*.swp
*.sqlite3
*.db
#/project/app/migrations
#/project/settings.py

#######################################################
##### Campos del user de django - table auth_user #####
#######################################################

id
password
last_login
is_superuser
first_name
last_name
email
is_staff
is_active
date_joined
username

############################
##### Reiniciar id_seq #####
############################

Con PhpPgAdmin

// instalacion
# aptitude install phppgadmin

http://localhost/phppgadmin/ // Interfaz grafica en el navegador web

El usuario y contraseña para conectarse debe ser un usuario de postgres.

Entramos en la db, luego en public, luego en secuencias, luego en app_model_id_seq, modificar
el campo que dice "reiniciar valor" que equivale al campo "last_value" de la tabla app_model_id_seq

Por ahora me ha servido para reiniciar las secuencias de las tablas de django y esto permite
por ejemplo, que al restaurar valores desde un csv, permite insertar nuevos registros en la tabla.

Si hay 3976 registros se debe configurar que el último valor es 3977 para que guarde bien en la tabla.

##############################################################
##### Subir archivos usando un formulario en el tempalte #####
##############################################################

# En la rama upload del siguiente repo está el ejemplo funcional:
# https://github.com/argenisosorio/registro_vistas_clases/

# Activamos las siguientes variables en el settings, y le damos la ruta donde se va a almacenar el fichero adjunto.

# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# urls.py
url(r'^file$', views.file, name='file'),

# views.py
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def file(request):
    """
    Función que permite guardar los archivos subidos en el servidor.
    """
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # Ruta donde está almacenado el archivo
        file = fs.url(filename)
        return render(request, 'registro/file.html', {
            'file': file
        })
    # Definimos en el settings la carpeta donde se van a guardar los documentos adjuntos.
    # El archivo será guardado en la carpeta "media" en la raíz del proyecto.
    return render(request, 'registro/file.html')


# file.html
<form method="post" enctype="multipart/form-data">{% csrf_token %}
  <input type="file" name="myfile">
  <br />
  <button type="submit">Upload</button>
</form>
{% if file %}
  <p>File uploaded at: <a href="{{ file }}">{{ file }}</a></p>
{% endif %}

# Luego de renderizar el formulario y subir un archivo, vamos a la carpeta media
# en la raíz del proyecto para verificar si se subio correctamente.

#############################################
##### Subir archivos usando Model Forms #####
#############################################

# En la rama upload_model del siguiente repo está el ejemplo funcional:
# https://github.com/argenisosorio/registro_vistas_clases/

# Activamos las siguientes variables en el settings, y le damos la ruta donde se va a almacenar el fichero adjunto

# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# urls.py
url(r'^file$', views.file, name='file'),
url(r'^list_files$', views.List_files.as_view(), name='list_files'),

# models.py
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# forms.py
# -*- coding: utf-8 -*-
from django import forms
from registro.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

# views.py
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from registro.models import Document
from registro.forms import DocumentForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


def file(request):
    """
    Función que permite guardar los documentos, se guardar en /media
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registro:consultar')
    else:
        form = DocumentForm()
    return render(request, 'registro/file.html', {
        'form': form
    })


class List_files(ListView):
    """
    Clase que permite listar los documentos registrados
    """
    model = Document
    template_name = "registro/list_files.html"

# file.html
<form method="post" enctype="multipart/form-data">{% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Upload</button>
</form>

# list_files.html
{% extends "registro/base.html" %}
{% block titulo %}List of Files{% endblock %}
{% block cuerpo %}
<h1>Lista de documetnos</h1>
<ul>
  {% for x in object_list %}
  <li>
    {{ x.description}} | {{ x.document}} | {{ x.uploaded_at}}
  </li>
  {% endfor %}
</ul>
{% endblock %}

#############################################################
##### Levantar un proyecto de Django, con uwsgi y nginx #####
#############################################################

# Ver guías de uwsgi y nginx para entender mejor.

En este ejemplo trabajaremos con un entorno virtual de python, y nuestro proyecto de Django se llama "prueba".

El fichero wsgi.py que está junto al settings.py lo moveremos a la raíz del proyecto, esto para que uwsgi
lo consiga con la configuración que haremos luego.

Instalamos nginx.

# apt-get install nginx

Instalamos uwsgi globalmente y el plugin de uwsgi de python.

# apt-get install uwsgi uwsgi-core

# apt-get install uwsgi-plugin-python // Para python 2.7

El crear y mover ficheros o directorios lo harémos siempre como root.
Ahora vamos a configurar nginx y a mover la aplicación "prueba" al directorio de trabajo /srv

En /etc/nginx/sites-available vamos a crear un fichero de configuración para nuestra aplicación "prueba"

/etc/nginx/sites-available# touch prueba

Ahora vamos a empezar a crear la configuración del sitio

/etc/nginx/sites-available# vim prueba

Nuestro fichero debería quedar mas o menos así:

server {
    #Puerto por el que va a escuchar el servidor
    listen 80;

    #Dirección ip de nuestra máquina
    #Va a ser la url o dirección por donde se va a servir la aplicación
    server_name 192.168.12.148;

    #Codificación de caracteres de la configuración
    charset utf-8;

    # Cuerpo máximo del mensaje permitido en una petición
    client_max_body_size 30M;

    client_body_buffer_size 128k;

    #Ruta en que está alojada la aplicación
    #root /srv/prueba;

    # Habilitamos los logs de acceso de nginx
    access_log /var/log/nginx/prueba.access.log;

    # Habilitamos los logs de error de nginx
    error_log /var/log/nginx/prueba.error.log;

    # Le decimos al servidor donde estan los estáticos de la aplicación
    location /static/ {
        root /srv/prueba/;
    }

    # Configuración adicional para trabajar con uwsgi
    # Esto es necesario solo si el sistema va a correr por una ruta
    #location ~ ^/(?<ruta>/.*)?$ {
    #location ~ ^/{
    location / {
        uwsgi_pass unix:/var/run/uwsgi/app/prueba/socket;
        include uwsgi_params;
        uwsgi_param UWSGI_SCHEME $http_x_forwarded_protocol;
        uwsgi_param SCRIPT_NAME /;
        # Esto es necesario solo si el sistema va a correr por una ruta
        #adicional al dominio, ejemplo: domain/ruta_adicional
        #uwsgi_param PATH_INFO $ruta;
        # Tiempo de espera en la conexión de nginx con uwsgi.
        uwsgi_read_timeout 600;
    }
}

Ahora creamos un enlace simbólico de sites-available a sites-enabled

# ln -s /etc/nginx/sites-available/prueba /etc/nginx/sites-enabled/

Al listar los directorios en sites-enabled nos quedará así:

/etc/nginx/sites-enabled# ls -la
total 8
drwxr-xr-x 2 root root 4096 ago 25 08:31 .
drwxr-xr-x 6 root root 4096 ago 25 07:59 ..
lrwxrwxrwx 1 root root   34 ago 25 07:59 default -> /etc/nginx/sites-available/default
lrwxrwxrwx 1 root root   25 ago 25 08:31 prueba -> ../sites-available/prueba

Verificamos que esté bien la configuración del nginx con:

# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

Ahora harémos las configuraciones de uwsgi en /etc/uwsgi

# cd /etc/uwsgi

etc/uwsgi# ls
apps-available  apps-enabled

Al igual que en nginx crearemos un fichero de configuración, pero este va a ser un xml
que se va a guardar en apps-available:

Tenemos que tener mucho cuidado al momento de configurar este fichero, las rutas deben ser
declaradas muy bien, especial énfasis en la ruta del entorno virtual, y el usuario del sistema y grupo
dueño de la aplicación, así como la ruta local o dirección donde está alojada la aplicación.

# cd /etc/uwsgi/apps-available

/etc/uwsgi/apps-available# vim prueba.xml

<uwsgi>
        <threads>100</threads>
        <workers>2</workers>
        <master/>
        <chmod-socket>666</chmod-socket>
        <!-- Ruta del entorno virtual donde está instalado Django -->
        <!-- Si el django está instalado en el sistema base no hace falta especificar alguna ruta, solo se comento o borra la directiva home -->
        <home>/home/user/Entornos_virtuales/Django_1.8.8</home>
        <!-- prueba hace referencia a los archivos de configuración que creamos en apps-available, en este caso, prueba.xml -->
        <socket>/var/run/uwsgi/app/prueba/socket</socket>
        <pidfile>/var/run/uwsgi/app/prueba/pid</pidfile>
        <!-- Identificador de usuario con el que se va a correr el proyecto -->
        <uid>root</uid>
        <!-- Identificador del grupo que puede correr la aplicación -->
        <gid>root</gid>
        <log-x-forwarded-for/>
        <post-buffering>4096</post-buffering>
        <max-requests>1000</max-requests>
        <!-- Ruta donde está alojado el código fuente de la aplicación -->
        <chdir>/srv/prueba</chdir>
        <!-- Ruta donde está alojado el código fuente de la aplicación y el directorio donde esta el wsgi.py etc... -->
        <pythonpath>/srv/prueba/prueba/</pythonpath>
        <module>wsgi</module>
        <!-- Si usamos python 3 en el proyecto configuramos "python3" -->
        <plugins>python27</plugins>
</uwsgi>

// Guardamos como prueba prueba.xml y ahora creamos el enlace simbolico en app-enabled

# ln -s /etc/uwsgi/apps-available/prueba.xml /etc/uwsgi/apps-enabled/

// Reiniciar servicio de nginx
# systemctl restart nginx

// Reiniciar el servicio de uwsgi
# systemctl restart uwsgi

Cada vez que se haga un cambio en la configuración de nginx reiniciaremos el servicio, y si el cambio
es de python, es decir en el proyecto de Django entonces reiniciaremos el servicio de uwsgi.

// Para no detener e iniciar los servicios y a su vez tumbar las conexiones usaremos reload en vez de restart:

# systemctl reload nginx

Si todo está bien, podemos visitar la ip local desde el navegador, 192.168.12.148 configurada en
nginx y por la cual va a estar servida la aplicación.

Si la aplicación no se muestra nos ayudaremos con los logs a encontrar el error

Para ver en tiempo real el log de accesos del servidor a nuestra aplicación:

# tailf /var/log/nginx/prueba.access.log

Para ver en tiempo real el log de errores del servidor en nuestra aplicación :

# tailf /var/log/nginx/prueba.error.log

Para ver en tiempo real el log de uwsgi:

# tailf /var/log/uwsgi/app/prueba.log

##############################################################
##### Levantar un proyecto de Django, con uwsgi y Apache #####
##############################################################

# Ver guías de uwsgi y apache para entender mejor.

Instalamos apache

# apt-get install apache2

Esto nos creará el directorio /var/www/html/

Movemos el proyecto de django a /var/www/html/ y le damos permisos de lectura, escritura y ejecución al proyecto

# chmod -R 777 /var/www/html

Instalamos el modulo uwsgi

# apt-get install libapache2-mod-wsgi

// Reiniciamos el servicio de apache
# service apache2 restart

Una vez apache se halla reiniciado tendremos el modulo instalado y activado en apache.
A este punto solo nos queda configurar el host virtual.

// En base al fichero de configuración por defecto creamos una copia
# cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/prueba.conf

Editamos prueba.conf

<VirtualHost *:80>
    # Por convención personal uso para los nombres de dominio la siguiente convención
    # lenguaje.nombre_del_proyecto.rama_de_git
    ServerName python.my_project.dev
    ServerAdmin admin@email.com
    # El document root debe hacer referencia a la carpeta donde esta nuestro proyecto
    DocumentRoot /var/www/html/my_project/

    # El WSGIScriptAlias obtiene 2 parámetros el primero hace referencia a la ruta y el segundo al archivo wsgi.py de nuestro proyecto
    WSGIScriptAlias / /var/www/html/my_project/my_project/wsgi.py

    # El WDGIDaemonProcess recibe los siguientes parámetros
    # - ServerName
    # - El ejecutable de Python relacionado al DocumentRoot
    # - La cantidad de procesos, para lo cual es recomendable dejarlo en 2
    # - Los threads, del mismo modo se recomienda dejarlo en 15
    # - Y el nombre a mostrar
    WSGIDaemonProcess python.<reponame>.dev python-path=/var/www/public/<reponame>:/var/www/public/<reponame>/env/lib/python2.7/site-packages processes=2 threads=15 display-name=%{GROUP}
    # El WSGIProcessGroup hace referencia al ServerName
    WSGIProcessGroup python.<reponame>.dev

    <Directory /var/www/public/my_project/ />
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    Alias /robots.txt /var/www/public/<reponame>/static/robots.txt
    Alias /favicon.ico /var/www/public/<reponame>/static/favicon.ico

    # El directorio "static" será el encargado de servir los archivos css, js, etc...
    Alias /static/ /var/www/html/my_project/static/

    <Directory /var/www/public/<reponame>/static>
        Require all granted
    </Directory>

    # El directorio "media" se encarga en este caso de servir las imágenes, videos y demás
    Alias /media/ /var/www/public/<reponame>/media/

    <Directory /var/www/public/<reponame>/media>
        Require all granted
    </Directory>

    # LogLevel info ssl:warn

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # Include conf-available/serve-cgi-bin.conf
</VirtualHost>

Falta...

#########################
##### sqlitebrowser #####
#########################

Herramienta de alta calidad visual para crear, diseñar y editar archivos de bases de datos compatibles con SQLite.
Es para usuarios y desarrolladores que desean crear bases de datos, buscar y editar datos.
Utiliza una interfaz de tipo hoja de cálculo familiar y no necesita aprender comandos SQL complicados.

Ideal para gestionar datos de las db de django.

# aptitude install sqlitebrowser

$ sqlitebrowser // Para ejecutarlo

########################################
##### Línea de comandos de sqlite3 #####
########################################

# apt-get install sqlite3

// Para abrir la línea de comandos:

$ sqlite3

// Acceder a una base de datos desde la consola de sqlite3

$ sqlite3 db.sqlite3

// Listar las tablas de la db a la cual se acceso.

sqlite> .tables

// Acceder al modo csv, para poder ejecutar operaciones con estos ficheros.

sqlite> .mode csv

// Importamos los datos de el fichero .csv a la tabla especifica.
// Obviamente deben coincidir los campos en el .csv y en la tabla.

sqlite> .import test.csv yourtable

// Ver esquema de creación de la tabla.

sqlite> .schema tablename

// Listar todos los registros de una tabla.

sqlite> SELECT * FROM tablename;

// Para salir del prompt de sqlite3

sqlite> .exit

###############################################################################
##### Insertar data csv en una base de datos sqlite con un script de bash #####
###############################################################################

#!/bin/sh
# Insertar data csv en una base de datos sqlite con un script de bash.
sqlite3 db.sqlite3 <<EOF
.mode csv
.import data.csv table_name
EOF

###################################################
##### Implementación de django simple captcha #####
###################################################

Paquete requerido django-simple-captcha==0.5.5

// Instalamos el paquete

$ pip install django-simple-captcha==0.5.5

// Agregamos en el settings.py en la sección de aplicaciones el paquete captcha

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
]

// En los forms.py importamos a:

from captcha.fields import CaptchaField

// Agregamos el campo captcha a la clase del form que lo va a tener, como la clase del login por ejemplo

captcha = CaptchaField()

// En la urls generales agregamos la url del captcha.

url(r'^captcha/', include('captcha.urls')),

// En la plantilla html agregamos

<div class="input-field {% if form.captcha.errors %}invalid{% endif %}">
    <label>{{form.captcha.label}}</label>
    <div class="col s7">
        {{form.captcha}}
    </div>
    <a class="col s2" onclick="refresh_captcha(this);" style="cursor: pointer">
        <i class="small material-icons">cached</i>
    </a>
    {% include 'base.forms.errors.html' with form_errors=form.captcha.errors col_title_error='col s2' col_msg_error='col s10' %}
</div>

ó

<div class="form_captcha">
    {{ form.captcha }}
    <a href="" class="js-captcha-refresh">Refrescar</a>
</div>

// En los js

/**
 * @brief Función para recargar el captcha vía json
 * @param element Recibe el botón
 */
function refresh_captcha(element) {
    $form = $(element).parents('form');
    var url = location.protocol + "//" + window.location.hostname + ":" + location.port + "/captcha/refresh/";

    $.getJSON(url, {}, function(json) {
        $form.find('input[name="captcha_0"]').val(json.key);
        $form.find('img.captcha').attr('src', json.image_url);
    });

    return false;
}

##################################################################
##### Resetear o cambiar el password de un usuario de django #####
##################################################################

$ python manage.py changepassword <user_name>

Ejemplo:

$ python manage.py changepassword admin

###############################################
##### Plantilla error 404.html y 500.html #####
###############################################

La siguiente prueba se realiza en entorno de producción, osea DEBUG = False

No hace falta declarar ningun método page_not_found en views.py y no hay que
declarar ningun handler404 = 'views.page_not_found' en las urls.

1) Editar settings.py, configurando DEBUG = False

2) Editar en el settings.py a 'DIRS': ['myapp/templates/myapp'],

3) Finalmente, crear la plantilla 404.html y 500.html en el directorio myapp/templates/myapp.

Ejemplos:

# 404.html
<div align="center">
  <h1>Error 404 Not Found</h1>
  <p>Recurso no encontrado. Se utiliza cuando el servidor web no encuentra la página o recurso solicitado.</p>
</div>

y

# 500.html
<div align="center">
  <h1>Error 500 Internal Server Error</h1>
   <p>Es un código comúnmente emitido por aplicaciones empotradas en servidores web, mismas que generan contenido dinámicamente, por ejemplo aplicaciones montadas en IIS o Tomcat, cuando se encuentran con situaciones de error ajenas a la naturaleza del servidor web.</p>
</div>

#################################
##### Ejemplo de DetailView #####
#################################

##### Usando Funciones #####

# urls.py
url(r'^detalle/(?P<pk>\d+)$', login_required(views.PostDetail), name='post_detail'),

# views.py
def PostDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render (request, 'app/post_detail.html', {'post': post})

# post_detail.html
{% for post in object_list %}
<div>
    Posted: {{ post.date }}, autor: {{ post.autor }}
    <h2>{{ post.title }}</h2>
    {{ post.body }}
    <a href="{% url 'post_edit' post.id %}"><button id="boton">Edit</button></a>
    <a href="{% url 'post_delete' post.id %}"><button id="boton">Delete</button></a>
    <a href="{% url 'post_detail' post.id %}"><button id="boton">Detail</button></a>
</div>
{% endfor %}

##### Usando clases genéricas #####

# urls.py
url(r'^post_detail/(?P<pk>\d+)$', login_required(views.Post_detail.as_view()), name='post_detail'),

# views.py
from django.views.generic import DetailView

class Detallar_reporte(DetailView):
    model = Post
    template_name = "app/post_detail.html"

# post_detail.html
{% for post in object_list %}
<div>
    Posted: {{ post.date }}, autor: {{ post.autor }}
    <h2>{{ post.title }}</h2>
    {{ post.body }}
    <a href="{% url 'post_edit' post.id %}"><button id="boton">Edit</button></a>
    <a href="{% url 'post_delete' post.id %}"><button id="boton">Delete</button></a>
    <a href="{% url 'post_detail' post.id %}"><button id="boton">Detail</button></a>
</div>
{% endfor %}

######################################################
##### Método __init__ de un formulario de django #####
######################################################

from django import forms

from .models import MyModel

class MyModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['name'].required = True
        self.fields['age'].required = True
        self.fields['bio'].required = True
        self.fields['profession'].required = True

    class Meta:
        model = MyModel

##############################################
##### Método get en una clase CreateView #####
##############################################

class BaseCreateView(SuccessMessageMixin,CreateView):
    model = Mymodel
    form_class = MymodelForm
    success_url = reverse_lazy('app:list_object')
    success_message = "Objet created"

    def get(self, request, *args, **kwargs):
        self.object = None
        return super(BaseCreateView, self).get(request, *args, **kwargs)

###########################################################################
##### Formulario para el cambio de contraseña del usuario autenticado #####
###########################################################################

# urls.py
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from usuarios import views
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^$', LoginView.as_view(), name = "login"),
    url(r'logout/$', views.Logout.as_view(), name='logout'),
    url(r'^cambiar-contrasena/$', login_required(views.change_password), name='change_password'),
)


# views.py
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)

def change_password(request):
    """
    Función que gestiona el cambio de contraseña
    de un usuario autenticado en el sistema.
    """
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            #messages = ['Cambio de contraseña exitoso']
            #return render_to_response("registro/index.html",{'messages': messages}, context_instance=RequestContext(request))
            return redirect('usuarios:login')
        else:
            print "No se realizó el cambio de contraseña"
    return render(request, 'usuarios/change_password.html', {'form': form})


# change_password.html
<form action="" method="post"> {% csrf_token %}
<table class="table_change_password" cellpadding="0px" cellspacing="0px">
  <tbody>
    <tr>
      <td>
        <label>Contraseña actual</label>
        {{ form.old_password }}
        {% if form.old_password.errors %}
          <p>{{ form.old_password.errors}}</p>
        {% endif %}
      </td>
    </tr>
    <tr>
      <td>
        <label>Contraseña nueva</label>
        {{ form.new_password1 }}
        {% if form.new_password1.errors %}
          <p>{{ form.new_password1.errors }}</p>
        {% endif %}
      </td>
    </tr>
    <tr>
      <td>
        <label>Contraseña nueva (confirmación)</label>
        {{ form.new_password2 }}
        {% if form.new_password2.errors %}
          <p>{{ form.new_password2.errors }}</p>
        {% endif %}
      </td>
    </tr>
  </tbody>
</table>
<br />
<button class="btn btn-success" type="submit">Cambiar contraseña</button>
</form>
