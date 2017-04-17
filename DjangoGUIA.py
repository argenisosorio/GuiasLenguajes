### Guía Django by dM ###

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

##### Modelo-vista-template #####

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

python manage.py runserver 8080 #Arranca el servido en el puerto 8080

python manage.py runserver 0.0.0.0:8000 #Cambiando la direccion IP

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
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
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

<form method="POST"> {% csrf_token %} #Este token lo agregamos por segridad, Django lo exige
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

*****Declarando los CSS

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

*****Agregando imagenes a la plantilla

Los archivos de media seran llamados de la carpeta Img
que por lo general acompaña al css, se hace referencia a la 
carpeta static con {{STATIC_URL}} y luego la ruta de la imagen:
Ejemplo:

<img src="Imagen.jpg" width="200px" heigth="200px"></img>

<img src="{{STATIC_URL}}css/Img/gris.JPG"></img> Agregando una imagen local 

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

AutoField: Es un IntegerField que se incrementa cuando creas un nuevo objeto, casi que no es necesario ya que django lo crea solo si no especificas otro campo como id.

BigIntegerField: Representa un Entero de 64 bit, es como el IntegerField, solo que permite números desde el -9223372036854775808 hasta el 9223372036854775807. El campo por defecto de los formularios es el TextField.

BooleanField: El campo de true/false. El campo por defecto de los formularios es un CheckboxInput. El vlaor por defecto es None si no defines el default.

CharField: Para string pequeños, frases o palabras. El campo por defecto en los formularios es el TextInput.
    max_length=20: Establece el tamaño máximo del string, es requerido.

CommaSeparateIntegerField: Guarda una lista de enteros separados por coma. 
    Max_length=20: Establece el valor máximo de los enteros, es requerido.

DateField: Guarda una instancia de la fecha a partir de la clase datetime.date de python.
    auto_now=True: Actualiza la fecha cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la fecha de cuando se creo.

DateTimeField: Como el DateField solo que guarda también la hora
    auto_now=True: Actualiza la fecha cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la fecha de cuando se creo.

DecimalField: Guarda números decimales.
    max_digits=5: Establece el numero de dígitos máximo, la suma de la parte entera y la decimal
    decimal_places=2: Establece el número de dígitos de la parte decimal.

EmailField: Es un CharField que comprueba lo introducido para verificar que sea un email.
    max_length=75: Establece el tamaño máximo del email, es requerido.

FileField: Sirve para guardar archivos en el servidor. En el formulario saldría el campo de escoger un fichero del ordenador. Tiene que estar definido el MEDIA_ROOT en el settings para que guarde los archivos. Guardara el archivo en la ruta especificada por el MEDIA_ROOT.
    upload_to='/videos': Subirá el archivo a la carpeta vídeos alojada en la carpeta definida por MEDIA_ROOT. (Requerido)
    FileField(upload_to='/video'[, max_length=100, **options]): si se quiere poner los atributos opcionales tendrán que añadirse así.

FilePathField: Sirve para mostrar los archivos accesible de una carpeta siguiendo una restricción si se quiera, para hacer alguna operación sobre ellos.
    FilePathField(path=None[, match=None,recursive=False, max_length=100, **options])
        path (requerido): directorio del que sacara FilePathField las opciones.
        match: filtro por el que pasaran los archivos, se usaran expresiones regulares.
        recursive: False por defecto, especifica si entran las subcarpetas de la ruta indicada por path.
        max_length: Indica el tamaño máximo del nombre del archivo.

FloatField: Campo que guarda una instancia del modelo Float de python.

ImageField: Como el FileField pero solo acepta formatos de imágenes. Tiene dos campos opcionales mas que el FielField
    height_field: Representa el alto máximo de la imagen.
    width_field: Representa el ancho máximo de la imagen.

IntegerField: Guarda un entero.

IPAddressField: Guarda un string que coincida con el formato ip (192.168.0.1).

GenericIPAddressField: Guarda una ip, ya sea ipv4 o ipv6. Para saber como las guarda Doc Django.

NullBooleanField: Como el BooleanField pero permite null.

PositiveIntegerField: Guarda un entero mayor o igual que cero.

SlugField:  Campo que guarda una pequeña etiqueta (letras, números, guiones) suele usarse en las url.

TextField: Campo que guarda texto.

TimeField: Guarda una hora, comparte los campos con DateField
    auto_now=True: Actualiza la hora cada vez que se actualiza el objeto.
    auto_now_add=True: Guarda la hora de cuando se creo.
URLField: Guarda una dirección html, comprueba que lo introducido sea una dirección html.

##### Campos de relación #####

ForeignKey:  Para referir objetos a un objeto, un modelo puede referirse a un modelo, pero un modelo puede estar referido a mas de uno, es lo que se llama un many-to-one referencia.

ManyToManyField: Para guardar una referencia a varios objetos de la misma clase. Hay que definir la clase con la que se relaciona. Va guardando las referencias a esos objetos en una lista con las primary keys referncia.

OneToOneField: Es como el ForeignKey pero tiene unique=True, por lo que solo puede haber una referencia a ese objeto.

##### Opciones que tienen todos los campos #####

null=True: Permite que los valores puedan ser null.

blank=True: Permite que el campo se pueda quedar en blanco.

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

##### Declarando la clase Articulo y Comentarios para una publicacion, y estableciendo
#la relacion entre los comentarios y un articulo #####
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post

admin.site.register(Post)

###############################################
##### Pasando un diccionario en el render #####
###############################################

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
@login_required(login_url='/')
def index(request):
    user = request.user
    return render_to_response('index.html', {'usuario':user},context_instance=RequestContext(request))

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

# Si el usuario está autenticado}
{% if request.user.is_authenticated %}
    Bienvenido: {{user.username}}
{% else %}
    Bienvenido: Anónimo
{% endif %}

# Si el usuario es admin
{% if user.is_staff %}
<h1>Soy Admin </h1>
{% else %}
<h1>No soy Admin </h1>
{% endif %}

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

####################################
##### Recolectar los estáticos #####
####################################

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

Ahora toca configurar el fichero WSGI, Django funciona utilizando el "protocolo WSGI", un estándar para servir sitios web usando Python, que PythonAnywhere soporta. La forma de configurar PythonAnywhere para que reconozca nuestro blog Django es editar un fichero de configuración WSGI.

Haz clic en el enlace "WSGI configuration file" (en la sección "Code" en la parte de arriba de la página; se llamará algo parecido a /var/www/<tu-usuario>_pythonanywhere_com_wsgi.py) y te redirigirá al editor, o tambien lo puedes editar desde la consola web, eso está en /var/www

Lo que me ha funcionado es crear un proyecto desde la interfaz web y luego desde la pestaña web modificar las rutas para que apunten al proyecto que clone.

##### Tips #####

- El nombre de usuario que elijamos sera parte de nuestro subdominio en la web, es decir, si mi usuario es dm, el dominio de mi web/applicación sera:
--> dm.pythonanywhere.com es decir, cuando elijas tu nombre de usuario ten en cuenta que la URL de tu blog tendrá la forma nombredeusuario.pythonanywhere.com, así
que o bien elije tu propio apodo o bien un nombre que describa sobre qué trata tu blog.

- En /var/www está el fichero usuario_pythonanywhere_com_wsgi.py para editarlo, lo reemplazamos todo con lo siguiente:

import os
import sys

path = '/home/{mi usuario}/default'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "default.settings")

application = get_wsgi_application()

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

#############################################
##### Mensajes / messages al hacer post #####
#############################################

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
      {% if message.tags %}{% endif %}>
      {{ message }}
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
