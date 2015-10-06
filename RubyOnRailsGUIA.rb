### Guía Ruby on Rails by dM ####

################################################
### Probados en: Debian GNU/Linux 7 (wheezy) ###
### ruby 2.2.1p85 ##############################
### Rails 4.2.4 ################################
################################################

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
	ó
$ rails -v

#-Instalar bundle, recorrerá todas las dependencias de gemas de la aplicación y las instalará.
#Deberíamos hacerlo cada vez que creemos una nueva aplicación para asegurarnos de que tenemos las gemas
#correctas instaladas, y también deberíamos hacerlo cada vez que desplegamos una aplicación para que se
#instalen las gemas correctas en el servidor.
$ bundle install

#-Despues de instalar las gemas basicas necesarias para un proyecto, se pueden visualizar con:
$ bundle show

#DB: Si creamos un proyecto, rails esta configurado para usar por defecto una db de Sqlite3 y 
#crear las tablas y campos en ella cuando se haga un rake, si cambiamos a otra base de datos
#en la conf de la aplicacion, será necesario hacer de nuevo un rake db:migrate para que vuelva
#a crear la estructura en la nueva db

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

config/ #Configura las reglas de ejecución de la aplicación, rutas, base de datos y más.

config.ru #Configuración Rack para servidores basados en Rack usados para iniciar la aplicación.

db/ #Contiene el esquema actual de tu base de datos, así como las migraciones de la base de datos.
#en el caso de Sqlite3, almacena el fichero de la db creada luego de la migrate.

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

#Ejemplos prácticos:

$ rails new universidad # Creamos la aplicacion de prueba

$ cd universidad # Entramos en el directorio creado

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

#Por defecto rails lanza su servidor en el puerto 3000 del localhost pero podemos iniciarlo en otro puerto dandole el parametro -p ejemplo:

$ rails server -P 8080 #Si visitamos 127.0.0.1:8080 comprobaremos el cambio de puerto

#Listo. Ahora se ingresa a la siguiente dirección en el navegador para utilizar la aplicación desarrollada:
localhost:3000/Empleados
	ó
localhost:3000/Alumnos

--- Otro ejemplo--- 

#Creando una aplicacion de (prueba) saludar y dar la hora

$ rails new prueba

$ cd prueba

$ rails server

#Comprobar en 127.0.0.1:3000 que el servidor esta corriendo correctamente
#La página "Welcome Aboard" es la primera prueba para una nueva aplicación Rails.
#Ésta asegura que tienes el software configurado correctamente para servir una página.

#Hola Rails
#Para conseguir que Rails diga "Hola Rails", necesitas crear como mínimo un controlador y una vista.
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

$ rails generate controller saludo index #Rails creará una serie de archivos y añadirá una ruta por ti.
#Se creará la ruta (http://localhost:3000/saludo/index) la primera parte indica la direccion base de 
#la aplicación, la segunda el controlador(welcome) y la tercera la accion a ejecutar(index)

#Los archivos más importantes de éstos son el controlador, que se encuentra en:
app/controllers/saludo_controller.rb

#y la vista, que se encuentra en:
app/views/welcome/index.html.erb.

#Abre el archivo app/views/saludo/index.html.erb en tu editor de texto y edítalo
#para que contenga sólo está línea de código:
<h1>Hola, Rails!</h1>

#Si visitamos:
127.0.0.1:3000/saludo/index #Veremos la vista que rails ha creado y nosotros hemos modificado

config/routes.rb #Es el archivo de enrutamiento de la aplicacion, le dice a rails como 
#conectar peticiones entrantes a controladores y acciones
#Encontraremos un:
get 'saludo/index' #Que esta asociado al controlador (saludo) de la accion (index)
#lo cual indica que en 127.0.0.1:3000/saludo/index se encuentra la vista del controlador que creamos

#Por defecto rails carga como pagina inicial la "Welcome aboard..." en el 127.0.0.1:3000
#Para que rails carge por defecto nuestra vista modificada vamos al fichero
config/routes.rb #y descomentamos la linea:

root 'welcome#index'

#la modificamos a:

root 'saludo#index' # Ahora rails cargará nuestra vista por defecto

#Supongamos que hemos credo dos controladores con sus respectivas vistas, cuyas
#rutas de ven reflejadas en el config/router.rb.
get 'saludo/index'
    y
get 'saludo2/index2'

#Si queremos que la vista principal sea ahora welcome2/index2 en vez de la primera entonces:
#en config/routes:
root 'welcomei2#index2' # Ahora rails cargará nuestra vista 2 por defecto

#Habiendo creado nuestro controlador y nuestra vista y haberlas probado
#vamos a mostrar la hora del sistema ademas del saludo.

#Para añadir contenido dinámico a una vista se incrusta código Ruby, algo así como la
#incrustacion de PHP en plantillas HTML. La incrustacion se hace en las vistas .html.erb
#ya que Rails lee interpreta esos ficheros usando el sistema ERb (de Embbeded Ruby).

#El contenido HTML es pasado al navegador directamente pero el contenido
#encerrado entre <%= %> es intrepetado y ejecutado como código Ruby.

#Editamos el controlado:
    prueba/app/controller/saludo_controller.rb

#Nos quedará así:

class SaludoController < ApplicationController
  def index
    t = Time.now
    @time = t.strftime('%H:%m:%S')
  end
end

#Guardamos, y ahora editaremos la vista para que muestre la hora que queremos:
    prueba/app/views/saludo/index.html.erb

#Nos queda así:

<h1>Hola, Rails!</h1>
Son las <%= @time %>

#Guardamos, si visitamos al url que hayamos asignado veremos el saludo y la hora.

#En Ruby se definen las variables de una clase con @ al comienzo del nombre.
#lo que nos permite hacer llamados de variables y funciones en la vista

### Declarando variables en el controlador e imprimiendolas en la vista ### 

#Basándonos en el ejemplo de mostrar el saludo y la hora, ahora declararemos unas variables
#y le daremos valores para imprimirlas en la vista, ejemplo:

    prueba/app/controller/saludo_controller.rb

#Nos quedará así:
class SaludoController < ApplicationController
  def index
    #t = Time.now
    #@time = t.strftime('%H:%m:%S')
    @nombre = "Maria"
    @apellido = "Sharapova" 
    @cedula = 12345678
    @email = "mariasha@fisk.com"
  end
end
#Las variables que comiencen con (@) que son variables de instancia
#automáticamente estián disponibles para las vista.

    prueba/app/views/saludo/index.html.erb

#Nos queda así:
<h1>Hola, Rails!</h1>
<b>Nombre:</b> <%= @nombre %> <br />
<b>Apellido:</b> <%= @apellido%> <br />
<b>Cedula:</b> <%= @cedula %> <br />
<b>Email:</b> <%= @email %>

#Guardamos y ya podremos ver las variables impresas en la vista

--- Creando aplicacion blog (controladores, vistas y rutas a mano)  ---

$ rails new blog #Creamos nuestra aplicacion

$ cd blog # Entramos en el directorio de la aplicacion

$ rails server # Iniciamos el servidor de pruebas

$ bin/rails g controller articulos #Creamos el controlador (articulos)
#nos generara un nuevo controlador en el fichero:
  blog/app/controllers/articulos_controller.rb
#así como como un directorio para guardar las vistas de nuestra aplicacion
#blog en:
  blog/app/views/articulos

#Si abrimos el
  blog/app/controllers/articulos_controller.rb
#veremos que el controlador de nuestra aplicacion blog esta vacío:

class ArticulosController < ApplicationController
end

#Un controlador es una clase que hereda de (ApplicationController) dentro
#de la clase Articulos es donde definiremos los metodos de nuestra aplicación

#Definimos un nuevo metodo en:
  blog/app/controllers/articulos_controller.rb
#El fichero nos quedaría así:

class ArticulosController < ApplicationController
  def nuevo
  end
end

#Sabemos que los controladores van asociados a una vista que mostrará
#el contenido que queremos, por ellos debemos crear esa vista,
#vamos a:
  blog/app/views/articulos
#Creamos un nuevo fichero:
  nuevo.html.erb
#La extensión de este nombre de archivo es muy importante: la primera extensión define el formato
#de la plantilla, y la segunda extensión el manejador de plantilla que se usará.
#Y pondremos un texto de ejemplo:

<div algin="center">
  <h1>Nuevo artículo</h1>
</div>

#Guardamos, ahora esta sera la vista que se mostrara cuando hagamos uso del controlador creado

#Solo resta agregar la ruta de nuestro controlador y nuestra vista en:
  blog/config/routes.rb

#Abrimos el routes.rb y agregamos en la segunda linea la ruta de nuestro
#controlador, nos quedaría así:

Rails.application.routes.draw do
  get 'articulos/nuevo'
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes"....... etc...

#Como vemos, le hemos dicho que a rails que esa será la ruta que ejecutará un controlador
#llamado (articulo) cuya vista es (nuevo) por lo que si visitamos:

  127.0.0.1:3000/articulos/nuevo #Deberíamos visualizar la plantilla que creamos

#Por defecto rails carga el index 'Welcome aboard...' en el 127.0.0.1:3000, si queremos
#que nuestra vista creada se cargue predeterminadamente buscamos en:
   blog/config/routes.rb 
#la linea root que esta comentada: # root 'welcome#index'
#la descomentamos y le damos la nueva ruta que va a nuestra vista para que se cargue por defecto:

  root 'articulos/nuevo'

#Guardamos y si vamos al localhost:3000 deberíamos ver nuestra vista cargada por defecto.

$ bin/rake routes #En la carpeta del proyecto, podremos ver las rutas establecidas para los controladores
#y vistas de nuestra aplicación 

--- Creando aplicacion para hacer publicaciones (autor, titulo y contenido)  ---

$ rails new publicaciones

$ cd publicaciones

$ rails server

$ rails generate scaffold Post autor:string titulo:string contenido:text 
# Se generaron los controladores y vistas que contienen los formularios
#con los campos establecidos

$ rake db:migrate #Se crearon las tablas correspondientes en la 
#base de datos de desarrollo Sqlite3

#http://127.0.0.1:3000/posts
#Podemos visualizar la lista de publicaciones asi como enlaces a las operaciones
#CRUD que se crearon
