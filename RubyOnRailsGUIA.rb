### Guía Ruby on Rails by dM ####

--- Ruby on Rails ---
#Es un framework de aplicaciones web de código abierto escrito en Ruby, siguiendo el paradigma de la arquitectura
#Modelo Vista Controlador (MVC). Trata de combinar la simplicidad con la posibilidad de desarrollar aplicaciones
#del mundo real escribiendo menos código que con otros frameworks y con un mínimo de configuración.
#El lenguaje de programación Ruby permite la metaprogramación, de la cual Rails hace uso, lo que resulta en una
#sintaxis que muchos de sus usuarios encuentran muy legible. Rails se distribuye a través de RubyGems, que es
#el formato oficial de paquete y canal de distribución de bibliotecas y aplicaciones Ruby.


--- Arquitectura MVC de Rails ---

--- Modelo ---
#En las aplicaciones web orientadas a objetos sobre bases de datos, el Modelo consiste en las clases que
#representan a las tablas de la base de datos.

#En Ruby on Rails, las clases del Modelo son gestionadas por ActiveRecord. Por lo general, lo único que
#tiene que hacer el programador es heredar una de las clases ActiveRecord::Base, y el programa averiguará
#automáticamente qué tabla usar y qué columnas tiene.

#Las definiciones de las clases también detallan las relaciones entre clases con sentencias de mapeo objeto

#El modelo representa:
#-Las Tablas de la Base de Datos.
#-Migraciones (Expresan Cambios en las BD)
#-Observadores
#-Emmigraciones

--- Vista ---
#Es la lógica de visualización, o cómo se muestran los datos de las clases del Controlador.
#Con frecuencia en las aplicaciones web la vista consiste en una cantidad mínima de código incluido en HTML.

#Existen maneras de gestionar las vistas. El método que se emplea en Rails por defecto
#es usar Ruby Empotrado (archivos.rhtml, desde la versión 2.x en adelante de RoR archivos.html.erb)
#que son básicamente fragmentos de código HTML con algo de código en Ruby.

#Es necesario escribir un pequeño fragmento de código en HTML para cada método del controlador
#que necesita mostrar información al usuario. El "maquetado" o distribución de los
#elementos de la página se describe separadamente de la acción del controlador y
#los fragmentos pueden invocarse unos a otros.

--- Controlador ---
#Las clases del Controlador responden a la interacción del usuario e invocan a la lógica
#de la aplicación, que a su vez manipula los datos de las clases del Modelo y muestra los
#resultados usando las Vistas. En las aplicaciones web basadas en MVC, los métodos del
#controlador son invocados por el usuario usando el navegador web.

--- Gemas ---
#Las gemas son plugins, paquetes y/o códigos añadidos a nuestros proyectos, que nos permiten
#nuevas funcionalidades, nuevas funciones predefinidas (como login de usuarios) o nuevas
#herramientas para el desarrollo como puedan ser Haml y SASS (la primera es una nueva
#forma de template basada en html pero más sencilla y potente, y la segunda es igual pero
#para el caso de las CSS). Para encontrar el listado de gemas disponibles puedes ir a RubyForge.

--- Soporte de Bases de Datos ---
#Dada que la arquitectura Rails favorece el uso de bases de datos se recomienda usar un
#SGBDR para almacenamiento de datos. Rails soporta la biblioteca SQLite por defecto.
#El acceso a la base de datos es totalmente abstracto desde el punto de vista del programador,
#es decir que es agnóstico a la base de datos, y Rails gestiona los accesos a la base de datos
#automáticamente (aunque, si se necesita, se pueden hacer consultas directas en SQL) Rails
#intenta mantener la neutralidad con respecto a la base de datos, la portatibilidad de la
#aplicación a diferentes sistemas de base de datos y la reutilización de bases de datos
#preexistentes. Sin embargo, debido a la diferente naturaleza y prestaciones de los SGBDRs
#el framework no puede garantizar la compatibilidad completa. Se soportan diferentes SGBDRs
#incluyendo MySQL, PostgreSQL, SQLite, IBM DB2 y Oracle.

--- PRUEBAS ---

#-Lo primero es comprobar que tienes instalada alguna versión reciente de Ruby:
$ ruby -v
ruby 2.2.1p85

#-Se debe contar con SQLite 3 instalado correctamente, comprobar.
$ sqlite3 --version
3.7.13

#-Instalar Rails con el comando de RubyGems: gem install.
$ gem install rails

#-Comprobar la correcta instalacion de Rails
$ rails --version

#-Instalar bundle, recorrerá todas las dependencias de gemas de la aplicación y las instalarái.
#Deberíamos hacerlo cada vez que creemos una nueva aplicación para asegurarnos de que tenemos las gemas
#correctas instaladas, y también deberíamos hacerlo cada vez que desplegamos una aplicación para que se
#instalen las gemas correctas en el servidor.
$ bundle install

#-Despues de instalar las gemas basicas necesarias para un proyecto, se pueden visualizar con:
$ bundle show

--- Comandos básicos de Ruby on rails ---

#Si quieres empezar un proyecto y ya tienes instalado RoR puedes comenzar con lo siguiente:
#Abre tu terminal, ve a la carpeta en donde meterás tus archivos y escribe los siguientes comandos:

$ rails new prueba #Se genera una nueva carpeta dentro del directorio, esa carpeta sera la aplicacion
#rails creada, ademas de que ejecutara bundle install automaticamente para instalar las dependencias(gemas)
#necesarias para el proyecto, a veces es necesario volver a instalar bundle para verificar si
#se instalaron todas las gemas, verificar errores etc. Las gemas que se instalan son las mencionadas
#en el gemfile que esta en el directorio de la aplicacion creada.

-------------------

#Al crear la aplicacion se generaran los directorios y subdirectorios de la misma:

app/ #Contiene los controllers, models, views, helpers, mailers y assets para tu aplicación.
#Te centrarás en esta carpeta por el resto de esta guía.

config/ #Configura las reglas de ejecución de la aplicación, rutas, base de datos y más.

config.ru #Configuración Rack para servidores basados en Rack usados para iniciar la aplicación.

db/ #Contiene el esquema actual de tu base de datos, así como las migraciones de la base de datos.

doc/ #Documentación detallada de tu aplicación.

Gemfile Gemfile.lock #Estos archivos te permiten especificar qué dependencias de gemas son necesitadas
#para tu aplicación Rails. Estos archivos son usados por la gema Bundler.

lib/ #Módulos extendidos para tu aplicación.

log/ #Archivos de Log de tu aplicación.

public/ #La única carpeta vista por el mundo tal como es. Contiene los archivos estáticos y assets compilados.

Rakefile #Este archivo localiza y carga tareas que pueden ser ejecutadas desde la línea de comandos.
#La lista de tareas son definidas a través de los componentes de Rails. En vez de cambiar el Rakefile,
#deberías agregar tus propias tareas, añadiendo archivos al directorio lib/tasks de tu aplicación.

README.rdoc #Este es un breve manual de instrucciones para tu aplicación. Deberías editar este archivo
#para comunicar a otros lo que tu aplicación hace, cómo configurala y demás.

script/ #Contiene el script de Rails que inicia tu aplicación y contiene otros scripts
#usados para correr tu aplicación.

test/ #Pruebas unitarias, fixtures y otras pruebas.

tmp/ #rchivos temporales (como archivos de caché, PID y archivos de sesiones).

vendor/ #Lugar para código de terceros. En una típica aplicación Rails, ésta incluye librerías y plugins.

-------------------

#Crear una tabla Empleados con algunos campos
$ rails g scaffold empleado Nombre:string direccion:string telefono:string fechadeEntrada:date 

#Otro Ejemplo:
$ rails g scaffold alumno Nombre:string Edad:string Cedula:string 

#Se migra (se hace corresponder el modelo del programa con una base de datos) con el comando
$ rake db:migrate

#Desde el terminal se lanza el servidor
$ rails s
    ó
$ rails server #Se visita la direccion 127.0.0.1/3000 para comprobar que el servidor esta corriendo
#Ctrl + C para  detener el servidor

#Listo. Ahora se ingresa a la siguiente dirección en el navegador para utilizar la aplicación desarrollada:
localhost:333/Empleados
	ó
localhost:333/Alumnos

@@@ Creando una aplicacion de prueba @@@

$ rails new blog

$ cd blog

$ rails server

#Comprobar en 127.0.0.1:3000 que el servidor esta corriendo correctamente
#La página "Welcome Aboard" es la primera prueba para una nueva aplicación Rails.
#Ésta asegura que tienes el software configurado correctamente para servir una página.

#Hola Mundo
#Para conseguir que Rails diga "Hola", necesitas crear como mínimo un controlador y una vista.
#El propósito de un controlador es recibir las peticiones (requests) de la aplicación. El enrutamiento
#(routing) decide qué controlador recibe qué petición.

#A menudo, hay más de una ruta para cada controlador, y diferentes rutas pueden ser servidas
#por diferentes acciones (actions). El propósito de cada acción es obtener información
#para pasarla después a la vista.

#El propósito de una vista es mostrar la información en un formato legible para los humanos.
#Una distinción importante que hacer es que es el controlador, y no la vista, donde la
#información es recolectada. La vista sólo debería mostrar la información. Por defecto,
#las plantillas de las vistas están escritas en un lenguaje llamado ERB (del inglés, Embedded Ruby)
#que se procesa automáticamente para cada petición servida por Rails.

#Para crear un nuevo controlador, necesitas ejecutar el generador de controladores y
#decirle que quieres un controlador llamado por ejemplo welcome con una acción llamada index.

$ rails generate controller welcome index #Rails creará una serie de archivos y añadirá una ruta por ti.

#Los archivos más importantes de éstos son el controlador, que se encuentra en:
app/controllers/welcome_controller.rb

#y la vista, que se encuentra en:
app/views/welcome/index.html.erb.

#Abre el archivo app/views/welcome/index.html.erb en tu editor de texto y edítalo
#para que contenga sólo está línea de código:
<h1>Hello, Rails!</h1>

#Si visitamos 127.0.0.1:3000/welcome/index veremos la vista rails ha creado y nosotros hemos modificado

config/routes.rb #Es el archivo de enrutamiento de la aplicacion, le dice a rails como 
#conectar peticiones entrantes a controladores y acciones
#Encontraremos un:
get 'welcome/index' #Que esta asociado al controlador (welcome) de la accion (index)
#lo cual indica que en 127.0.0.1:3000/welcome/index se encuentra la vista del controlador que creamos




















