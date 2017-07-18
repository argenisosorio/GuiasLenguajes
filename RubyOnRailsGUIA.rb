##### Guía Ruby on Rails by dM #####

Probados en: Debian GNU/Linux 7 y 8

#########################
##### Ruby on Rails #####
#########################

Es un framework de aplicaciones web de código abierto escrito en Ruby, siguiendo el paradigma
de la arquitectura Modelo Vista Controlador (MVC). Trata de combinar la simplicidad con la
posibilidad de desarrollar aplicaciones del mundo real escribiendo menos código que con
otros frameworks y con un mínimo de configuración. El lenguaje de programación Ruby permite
la metaprogramación, de la cual Rails hace uso, lo que resulta en una sintaxis que muchos
de sus usuarios encuentran muy legible. Rails se distribuye a través de RubyGems, que es
el formato oficial de paquete y canal de distribución de bibliotecas y aplicaciones Ruby.

#####################################
##### Arquitectura MVC de Rails #####
#####################################

##### Modelo #####

En las aplicaciones web orientadas a objetos sobre bases de datos, el Modelo consiste en
las clases que representan a las tablas de la base de datos.

En Ruby on Rails, las clases del Modelo son gestionadas por ActiveRecord. Por lo general, lo
único que tiene que hacer el programador es heredar una de las clases ActiveRecord::Base, y
el programa averiguará automáticamente qué tabla usar y qué columnas tiene.

Las definiciones de las clases también detallan las relaciones entre clases con sentencias
de mapeo objeto.

El modelo representa:
-Las Tablas de la Base de Datos.
-Migraciones (Expresan Cambios en las BD)
-Observadores
-Emmigraciones

##### Vista #####

Es la lógica de visualización, o cómo se muestran los datos de las clases del Controlador.
Con frecuencia en las aplicaciones web la vista consiste en una cantidad mínima de
código incluido en HTML.

Existen maneras de gestionar las vistas. El método que se emplea en Rails por defecto
es usar Ruby Empotrado (archivos.rhtml, desde la versión 2.x en adelante de RoR archivos.html.erb)
que son básicamente fragmentos de código HTML con algo de código en Ruby.

Es necesario escribir un pequeño fragmento de código en HTML para cada método del controlador
que necesita mostrar información al usuario. El "maquetado" o distribución de los
elementos de la página se describe separadamente de la acción del controlador y
los fragmentos pueden invocarse unos a otros.

##### Controlador #####

Las clases del Controlador responden a la interacción del usuario e invocan a la lógica
de la aplicación, que a su vez manipula los datos de las clases del Modelo y muestra los
resultados usando las Vistas. En las aplicaciones web basadas en MVC, los métodos del
controlador son invocados por el usuario usando el navegador web.

##### Gemas #####

Las gemas son plugins, paquetes y/o códigos añadidos a nuestros proyectos, que nos permiten
nuevas funcionalidades, nuevas funciones predefinidas (como login de usuarios) o nuevas
herramientas para el desarrollo como puedan ser Haml y SASS (la primera es una nueva
forma de template basada en html pero más sencilla y potente, y la segunda es igual pero
para el caso de las CSS). Para encontrar el listado de gemas disponibles puedes ir a RubyForge.

##### Soporte de Bases de Datos #####

Dada que la arquitectura Rails favorece el uso de bases de datos se recomienda usar un
SGBDR para almacenamiento de datos. Rails soporta la biblioteca SQLite por defecto.
El acceso a la base de datos es totalmente abstracto desde el punto de vista del programador,
es decir que es agnóstico a la base de datos, y Rails gestiona los accesos a la base de datos
automáticamente (aunque, si se necesita, se pueden hacer consultas directas en SQL) Rails
intenta mantener la neutralidad con respecto a la base de datos, la portatibilidad de la
aplicación a diferentes sistemas de base de datos y la reutilización de bases de datos
preexistentes. Sin embargo, debido a la diferente naturaleza y prestaciones de los SGBDRs
el framework no puede garantizar la compatibilidad completa. Se soportan diferentes SGBDRs
incluyendo MySQL, PostgreSQL, SQLite, IBM DB2 y Oracle.

#########################################
##### ¿Cómo instalar Ruby on Rails? #####
#########################################

De --> http://www.rubyonrails.org.es/instala.html

En general, instalar Rails es tan sencillo como gem install rails, pero primero hay
que tener el lenguaje Ruby y el gestor de librerías Rubygems en el sistema.

Linux es un entorno habitual para servidores, con lo que muchos desarrolladores
lo escogen minimizando así las diferencias entre el entorno de desarrollo y el de producción.

##################################################################
##### Instalar Rails con el comando de RubyGems: gem install #####
##################################################################

# Instalar la última version disponible
$ gem install rails 

# Podemos especificar la versión a instalar
$ sudo gem install rails --version 4.2.2

# Comprobar la correcta instalacion de Rails
$ rails --version
ó
$ rails -v

# Comando para ver los parametro disponibles de rails
$ rails

Instalar bundle(ver sección de bundle), recorrerá todas las dependencias de gemas de la
aplicación y las instalará.

Deberíamos hacerlo cada vez que creemos una nueva aplicación para asegurarnos de
que tenemos las gemas correctas instaladas, y también deberíamos hacerlo cada vez
que desplegamos una aplicación para que se instalen las gemas correctas en el servidor.

$ bundle install

# Despues de instalar las gemas basicas necesarias para un proyecto, se pueden visualizar con:
$ bundle show

DB: Si creamos un proyecto, rails esta configurado para usar por defecto una db de Sqlite3 y 
crear las tablas y campos en ella cuando se haga un rake, si cambiamos a otra base de datos
en la conf de la aplicacion, será necesario hacer de nuevo un rake db:migrate para que vuelva
a crear la estructura en la nueva db.

################################
##### Ruby Version Manager #####
################################

Evita administrar Ruby, RubyGems y demás con el gestor de paquetes de tu distribución ya
que estos suelen estar desactualizados.

En su lugar, puedes emplear "RVM". RVM te permite instalar y mantener varias versiones
de ruby a la vez. Puedes encontrar más información sobre
Ruby Version Mananger (RVM) en https://rvm.io

##### Paquetes requeridos por RVM #####

Instalaremos RVM desde el sitio web del proyecto, por lo que no confiamos en los
repositorios predeterminados de Debian para la instalación real. sin embargo, RVM
utiliza el gestor de paquetes para instalar las dependencias de los programas que
gestiona, por lo que debemos asegurarnos de que los repositorios estén actualizados:

# Actualizamos la lista de paquetes del repositorio.
# apt-get update

# Instalamos los paquetes requeridos por RVM.
# apt-get install git-core subversion nodejs curl

##### Instalación de la firma #####

El RVM a partir de la versión 1.26 introduce versiones firmadas y comprobación
automática de las mismas.

Para ello necesitamos instalar dicha firma. En caso contrario podría darnos
problemas al instalar RVM.

$ gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
  
##### Instalación rápida de RVM #####

$ \curl -sSL https://get.rvm.io | bash -s stable --rails --ruby
  
Este comando instala las últimas versiones estables de rvm, ruby y rails.
Nos pedirá la contraseña de root en algun momento, es recomendable según la
documentación que nos pida la contraseña, en vez de ejecutar el comando anterior como root.
Ejecutaremos este comando después de instalar la firma. Al ejecutar esto se produce
un montón de salida por pantalla.

Una vez finalizado este proceso, RVM nos dice que ejecutemos un comando que empieza
por source... o que reiniciemos las shells abiertas.

Por sencillez, cerramos la ventana de la consola y abrimos una nueva. A veces no pide
hacer nada si no que termina directamente sin problemas.

##### Comprueba la configuración #####

# Tipeamos lo siguiente:
$ type rvm | head -1
rvm: es una función # Será la salida si todo se instaló correctamente.
	
#################################################################
##### Problema con la función (comprobación de instalación) #####
#################################################################

Después de la instalación, al momento de hacer la comprobación
puede que muestre que rvm no es una función:

rvm is not a function, because gnome-terminal run as no-login shell

Esto lo arreglamos agregando una línea al fichero .bashrc, la siguiente:

[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"

y guardamos, luego actualizamos los cambios del fichero en el sistema con:

$ source .bashrc

Al momento de la instalación, rvm puede generar una línea como la que necesitamos pero que no funciona, algo
como esto:

$HOME/.rvm/scripts/rvm

Pero esa no funciona asi que la comentamos o borramos, agregamos la anterior descrita, guardamos, actualizamos
shell y luego volvemos a probar con la funcion inicial:

$ type rvm | head -1
rvm: es una función // Será la salida si todo se instaló correctamente.

Si todo está bien se habrá creado el directorio:
    
/home/user/.rvm/gems

Según la version de ruby instalada inicialmente podremos ver nuestras instancias en:

/home/user/.rvm/gems/
    ruby-2.4.0/

Suponiendo que se instaló esa versión de ruby, puesto que en el comando de instalación
de rvm también especificamos que se instalan las últimas versiones de ruby y Rails.

$ rvm install 2.2.1 # Instalando una version específica

Se creara un gemset o instancia o directorio para esa versión de ruby en:

/home/user/.rvm/gems/ruby-2.2.1
    ruby-2-2-1/
        gems/ # Es aquí donde se guardaran las gemas para esa instancia y versió de ruby

# Para listar las instalaciones de Ruby existentes y ver cual se está usando
$ rvm list 

---

rvm rubies

   ruby-2.2.4 [ x86_64 ]
=* ruby-2.3.0 [ x86_64 ]

# => - current
# =* - current && default
#  * - default

---

# En este caso vemos que tenemos dos instancias de ruby

# Para usar esa versión de ruby específica, algo así como acceder a un entorno virtual en python.
$ rvm use 2.3.0 

# Desinstalar una versión específica de ruby
$ rvm uninstall ruby-2.3.0 

###################
##### Gemsets #####
###################

Podemos crear conjuntos de gemas separadas para cada proyecto. Tan sólo hay que especificar
un nombre para ese gemset, y utilizar las herramientas que rvm proporciona
(puedes escribir "rvm gemset" para ver todos los comandos disponibles).

Por ejemplo, podemos crearnos un gemset para el proyecto 1, y cambiarnos a él:

$ rvm gemset create proyecto1

Es importante entender que el gemset se crea para el intérprete que estemos
usando en ese momento. De modo que antes de crear un gemset, selecciona el
intérprete adecuado es decir la version de ruby dentro de las disponibles.

Una vez que estemos usando ese gemset instalaremos las gemas específicas de ese proyecto

Ademas de versiones de gemas tambien es posible usar diferentes versiones de ruby, por lo tanto,
podemos crear una instancia y un gemset con:

$ rvm install ruby-2.2.5

y luego crear un gemset para esa versión:

$ rvm gemset create proyecto1

Esto creará el siguiente directorio:

/home/user/.rvm/gems/
    ruby-2.2.5@proyecto1 # Nuestro gemset recien generado
    ruby-2.2.4/

$ rvm gemset use ruby-2.2.5@proyecto1

Ahora podemos instalar cualquier gema y quedara dentro de esa instancia o versión
de ruby y en ese gemset específico.

##################
##### Bundle #####
##################

Bundler proporciona un entorno consistente para proyectos de Ruby mediante el
seguimiento y la instalación de las versiones y las gemas exactas que se necesitan.

Bundler es una salida del infierno de las dependencias, y asegura que las gemas
que necesita están presentes en el desarrollo, la puesta en escena, y la producción.
De empezar a trabajar en un proyecto es tan simple como paquete de instalación.

Bundler proporciona un entorno consistente para los proyectos de Ruby mediante el seguimiento y la instalación
de las gemas exactas y las versiones que se necesitan. 

Documentacio en --> http://bundler.io/

Cuando creamos un proyecto en una version específica de rails, este instala todas
las gemas necesarias para su funcionamiento, estas gemas están descritas en el fichero
Gemfile.

# En el Gemfile se especifican las dependencias de las gemas que usara nuestro proyecto, ejemplo:
source 'https://rubygems.org'
gem 'nokogiri'
gem 'rack', '~>1.1'
gem 'rspec', :require => 'spec'

# Visualizar las gemas instaladas en un proyecto
$ bundle show

# Detectar las gemas que están desactualizadas, bundle revisará cuáles de nuestras gemas
# tienen nuevas versiones y nos las listará
$ bundle outdated 

# Si queremos actualizarlas todas podemos ejecutar
$ bundle update

# Si solo queremos actualizar una gema en particular.
$ bundle update <nombre_de_la_gema>
  
Pero si agregamos una gema que no es instalada automáticamente
deberemos repasar la lista de dependencias para que se instalen
las nuevas que no han sido instaladas, esto lo haremos con el comando:

$ gem install bundler

#######################################
##### Crear un proyecto con rails #####
#######################################

$ rails new project

Se genera una nueva carpeta dentro del directorio, esa carpeta sera la aplicacion
rails creada, ademas de que ejecutara bundle install automaticamente para instalar
las dependencias(gemas) necesarias para el proyecto, a veces es necesario volver a
instalar bundle para verificar si e instalaron todas las gemas, verificar errores etc.
Las gemas que se instalan son las mencionadas en el gemfile que esta en el
directorio de la aplicacion creada.

#####################################################
##### Estructura básica de un proyecto en rails #####
#####################################################

app/ # Contiene los controllers, models, views, helpers, mailers y assets para tu aplicación.

app/assets # Aquí guardaremos las imagenes, javascripts y las hojas de estilo.
  images
  javascripts
  stylesheets

config/ # Configura las reglas de ejecución de la aplicación, rutas, base de datos y más.
  application.rb # El propósito de este archivo es configurar cosas para toda la aplicación.  

config.ru # Configuración Rack para servidores basados en Rack usados para iniciar la aplicación.

db/ # Contiene el esquema actual de tu base de datos, así como las migraciones de la base de datos.
# en el caso de Sqlite3, almacena el fichero de la db creada luego de la migrate.

doc/ # Documentación detallada de tu aplicación.

Gemfile # Fichero donde se especifícan las dependencias del proyecto

Gemfile.lock # Contienen una instantánea completa de todas las gemas de el Gemfile junto con la
# dependencia asociada a cada gema.
# Estos archivos son usados por la gema Bundler que es la que permite instalar las dependencias.

lib/ # Módulos extendidos para tu aplicación.

log/ # Archivos de Log de tu aplicación.

public/ # La única carpeta vista por el mundo tal como es. Contiene los archivos estáticos
# y assets compilados.

Rakefile # Este archivo localiza y carga tareas que pueden ser ejecutadas desde la línea de comandos.
# La lista de tareas son definidas a través de los componentes de Rails. En vez de cambiar
# el Rakefile, deberías agregar tus propias tareas, añadiendo archivos al directorio
# lib/tasks de tu aplicación.

README.rdoc # Este es un breve manual de instrucciones para tu aplicación. Deberías editar
# este archivo para comunicar a otros lo que tu aplicación hace, cómo configurala y demás.

script/ # Contiene el script de Rails que inicia tu aplicación y contiene otros scripts
# usados para correr tu aplicación.

test/ # Pruebas unitarias, fixtures y otras pruebas.

tmp/ # archivos temporales (como archivos de caché, PID y archivos de sesiones).

vendor/ # Lugar para código de terceros. En una típica aplicación Rails, ésta
# incluye librerías y plugins.

#############################################
##### Comandos básicos de Ruby on rails #####
#############################################

# Comprobar que tienes instalada alguna versión reciente de Ruby:
$ ruby -v

# Comprobar que tienes instalado SQLite 3 instalado correctamente.
$ sqlite3 --version

# Desinstalar una gema específica, a veces hay conflictos entre versiones de gemas a usar en el proyecto y las gemas instaladas.
# Si no se deja desinstalar la podemos borrar directamente donde fue instalada, si se uso rvm entonces seguro está
# instanciada en .rvm/gems/ruby-x.x.x/cache y .rvm/gems/ruby-2.2.1/gems en el home del usuario
$ gem uninstall <gem-name>

# Instalar una gema específica, usar el parametro "--version" acortado con "-v"
$ gem install rails -v 0.14.1

# Crear la db y hacer las migraciones descritas en el schema.rb
$ rake db:create db:schema:load

# Ver las rutas para todas las acciones estándar de las aplicaciones, direcciones REST, se
#especifican cuales peticiones van por GET, POST, etc.
$ rake routes
ó
$ bin/rake routes

# Especificando la DB si hay exepciones sobre ello
$ DB=postgres rake routes

# Saltandose erroes para ejecutar el comando
$ DB=postgres bundle exec rake routes

# Chequear las migraciones realizadas, cuales se levantaron y cuales estan pendientes o fallaron
$ DB=postgres bin/rake db:migrate:status

# Para moverse entre los estados de las migraciones donde X es el numero a retroceder
$ bin/rails db:rollback STEP=X

###########################################
##### Servidor de desarrollo de Rails #####
###########################################

Por defecto rails lanza su servidor en el puerto 3000 del localhost, pero podemos iniciarlo
en otro puerto dandole el parametro -p ejemplo:

Usos del server: server [options]

-p, --port=port  --- Runs Rails on the specified port.
                     Default: 3000
-b, --binding=ip --- Binds Rails to the specified ip.
                     Default: 0.0.0.0

$ rails server -P 8080 # Si visitamos 127.0.0.1:8080 comprobaremos el cambio de puerto

$ rails s -b 192.168.xx.xx -p 80 # Correr el servidor asignándole una ip y un puerto

Ctrl + C para  detener el servidor.

#######################################################
##### Activando un proyecto clonado o ya iniciado #####
#######################################################

Cuando trabajamos con un proyecto que fue generado en otra parte, lo mejor es instalar
todas las dependencias y las mismas versiones con las cuales se genero el proyecto.
Hablamos tanto de la version de ruby, RoR y bundle, aparte de las versiones de las gemas
restantes que son descritas en el Gemfile, la version de bundle original la encontraremos
el fichero Gemfile.lock que es un fichero generado a partir del gemfile al momento de
la instalación de dependencias, se visualizara con un:

BUNDLED WITH
    1.xx.x

Lo que nos lleva a instalar esa version de bundle para correr el servidor de ese proyecto, usamos:

$ gem install bundler 1.xx.x

Al momento de clonar algun proyecto es sabido que cuenta con algunas dependencias
específicas, ya sea una version de rails, sqlite3 u otras gemas, para instalar
esas dependencias usaremos bundle, que no es mas que un script que instala
lo que está descrito en el Gemfile, por eso instalamos bundle.

# Dentro del proyecto instalamos bundler:
$ gem install bundler 1.xx.x

# Luego, dentro del proyecto instalamos las dependencias(gemas) específicas para ese proyecto:
$ bin/bundle install

# Checks if the dependencies listed in Gemfile are satisfied by currently installed gems 
$ bundle check

#################################################
##### Lista de los tipos de datos - modelos #####
#################################################

Here are all the Rails 4 (ActiveRecord migration) datatypes:

:binary
:boolean
:date
:datetime
:decimal
:float
:integer
:bigint
:primary_key
:references
:string
:text
:time
:timestamp

If you use PostgreSQL, you can also take advantage of these:

:hstore
:json
:array
:cidr_address
:ip_address
:mac_address

##########################################
##### Ejemplo de .gitignore para RoR #####
##########################################

# Ignore bundler config.
/.bundle

# Ignore the default SQLite database.
/db/*.sqlite3
/db/*.sqlite3-journal

# Ignore all logfiles and tempfiles.
/log/*
/tmp/*
!/log/.keep
!/tmp/.keep

# Ignore Byebug command history file.
.byebug_history

# Ignore de temporary files
*.*.backup
*.*~
*.tar.gz
*.log
*.swp

#####################################
##### Trabajando los css y scss #####
#####################################

# Fichero creado automáticamente, son los estilos globales
# incluídos automaticamente a todas las plantillas
rails_project/app/assets/stylesheets/application.css

# Si por ejemplo generamos un controlador 'welcome'
# se creara una hoja de estilos .scss solo para ese controlador
# Todo lo que declaremos ahí será incluído automaticamente en application.css
rails_project/app/assets/stylesheets/welcome.scss

######################################
##### Trabajando los js y coffee #####
######################################

# Al igual que que con los css, al momento de crear un proyecto
# se crea un fichero 'application.js' que estará disponible
# para todas las vistas.
rails_project/app/assets/javascripts/application.js

# Cuando generamos un nuevo controlar y su vista, también
# se creará su fichero .coffee para agregar contenido .js
# que también será incluído automáticamente en application.js
rails_project/app/assets/stylesheets/welcome.coffee

################
##### Tips #####
################

# Enlace al path de otro controlador
# <%= link_to "proyecto", proyecto_path%>

##############################
##### Ejemplos prácticos #####
##############################

$ rails new universidad # Creamos la aplicacion de prueba

$ cd universidad # Entramos en el directorio creado

# Crear una tabla Empleados con algunos campos
$ rails g scaffold empleado Nombre:string direccion:string telefono:string fechadeEntrada:date 

# Otro Ejemplo:
$ rails g scaffold alumno Nombre:string Edad:string Cedula:string 

# Se migra (se hace corresponder el modelo del programa con una base de datos) con el comando
$ rake db:migrate

# Desde el terminal se lanza el servidor
$ rails s
ó
$ rails server # Se visita la direccion 127.0.0.1/3000 para comprobar que el servidor esta corriendo
# Ctrl + C para  detener el servidor.

Por defecto rails lanza su servidor en el puerto 3000 del localhost.

Ahora se ingresa a la siguiente dirección en el navegador para utilizar la aplicación desarrollada:

localhost:3000/Empleados
ó
localhost:3000/Alumnos

Según el ejemplo que se haya utilizado

####################################################################
##### Creando una aplicacion de (prueba) saludar y dar la hora #####
####################################################################

$ rails new prueba

$ cd prueba

$ rails server

Comprobar en 127.0.0.1:3000 que el servidor esta corriendo correctamente
La página "Welcome Aboard" es la primera prueba para una nueva aplicación Rails.
Ésta asegura que tienes el software configurado correctamente para servir una página.

##### Hola Rails #####

Para conseguir que Rails diga "Hola Rails", necesitas crear como mínimo un controlador
y una vista.

El propósito de un controlador es recibir las peticiones (requests) de la aplicación.
El enrutamiento (routing) decide qué controlador recibe qué petición.

A menudo, hay más de una ruta para cada controlador, y diferentes rutas pueden ser servidas
por diferentes acciones (actions). El propósito de cada acción es obtener información
para pasarla después a la vista.

El propósito de una vista es mostrar la información en un formato legible para los humanos.
Una distinción importante que hacer es que es el controlador, y no la vista, donde la
información es recolectada. La vista sólo debería mostrar la información. Por defecto,
las plantillas de las vistas están escritas en un lenguaje llamado ERB (del inglés, Embedded Ruby)
que se procesa automáticamente para cada petición servida por Rails.

Para crear un nuevo controlador, necesitas ejecutar el generador de controladores y
decirle que quieres un controlador llamado por ejemplo saludo con una acción llamada index.

$ rails generate controller saludo index

Rails creará una serie de archivos y añadirá una ruta por ti.
Se creará la ruta (http://localhost:3000/saludo/index) la primera parte indica la direccion base de 
la aplicación, la segunda el controlador(saludo) y la tercera la accion a ejecutar(index)

# Los archivos más importantes de éstos son el controlador, que se encuentra en:
app/controllers/saludo_controller.rb

# y la vista, que se encuentra en:
app/views/welcome/index.html.erb.

Abre el archivo app/views/saludo/index.html.erb en tu editor de texto y edítalo
para que contenga sólo está línea de código:

<h1>Hola, Rails!</h1>

Si visitamos:
127.0.0.1:3000/saludo/index # Veremos la vista que rails ha creado y nosotros hemos modificado

config/routes.rb # Es el archivo de enrutamiento de la aplicacion, le dice a rails como 
# conectar peticiones entrantes a controladores y acciones

# Dentro de config/routes.rb Encontraremos un:
get 'saludo/index' # Que esta asociado al controlador (saludo) de la accion (index)
# lo cual indica que en 127.0.0.1:3000/saludo/index se encuentra la vista del controlador que creamos

Por defecto rails carga como pagina inicial la "Welcome aboard..." en el 127.0.0.1:3000
Para que rails carge por defecto nuestra vista modificada vamos al fichero
config/routes.rb # y descomentamos la linea:

root 'welcome#index'

# la modificamos a:

root 'saludo#index' # Ahora rails cargará nuestra vista por defecto

# Supongamos que hemos credo dos controladores con sus respectivas vistas, cuyas
# rutas de ven reflejadas en el config/router.rb.

get 'saludo/index'
y
get 'saludo2/index2'

# Si queremos que la vista principal sea ahora welcome2/index2 en vez de la primera entonces:
# en config/routes:
root 'welcomei2#index2' # Ahora rails cargará nuestra vista 2 por defecto

Habiendo creado nuestro controlador y nuestra vista y haberlas probado
vamos a mostrar la hora del sistema ademas del saludo.

Para añadir contenido dinámico a una vista se incrusta código Ruby, algo así como la
incrustacion de PHP en plantillas HTML. La incrustacion se hace en las vistas .html.erb
ya que Rails lee interpreta esos ficheros usando el sistema ERb (de Embbeded Ruby).

# El contenido HTML es pasado al navegador directamente pero el contenido
# encerrado entre <%= %> es intrepetado y ejecutado como código Ruby.

#Editamos el controlado:
    prueba/app/controller/saludo_controller.rb

#Nos quedará así:

class SaludoController < ApplicationController
  def index
    t = Time.now
    @time = t.strftime('%H:%m:%S')
  end
end

# Guardamos, y ahora editaremos la vista para que muestre la hora que queremos:
prueba/app/views/saludo/index.html.erb

# Nos queda así:
'''

<h1>Hola, Rails!</h1>
Son las <%= @time %>

'''

Guardamos, si visitamos al url que hayamos asignado veremos el saludo y la hora.

En Ruby se definen las variables de una clase con @ al comienzo del nombre.
lo que nos permite hacer llamados de variables y funciones en la vista

###### Declarando variables en el controlador e imprimiendolas en la vista #####

Basándonos en el ejemplo de mostrar el saludo y la hora, ahora declararemos unas variables
y le daremos valores para imprimirlas en la vista, ejemplo:

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

 Las variables que comiencen con (@) que son variables de instancia
automáticamente estián disponibles para las vista.

prueba/app/views/saludo/index.html.erb

# Nos queda así:
'''
<h1>Hola, Rails!</h1>
<b>Nombre:</b> <%= @nombre %> <br />
<b>Apellido:</b> <%= @apellido%> <br />
<b>Cedula:</b> <%= @cedula %> <br />
<b>Email:</b> <%= @email %>
'''

Guardamos y ya podremos ver las variables impresas en la vista

##### Creando aplicacion blog (controladores, vistas y rutas a mano) #####

# Creamos nuestra aplicacion
$ rails new blog

# Entramos en el directorio de la aplicacion
$ cd blog

# Iniciamos el servidor de pruebas
$ rails server

$ bin/rails g controller articulos # Creamos el controlador (articulos)
# nos generara un nuevo controlador en el fichero:
blog/app/controllers/articulos_controller.rb

# así como como un directorio para guardar las vistas de nuestra aplicacion
# blog en:
blog/app/views/articulos

# Si abrimos el:
blog/app/controllers/articulos_controller.rb
# veremos que el controlador de nuestra aplicacion blog esta vacío:

class ArticulosController < ApplicationController
end

Un controlador es una clase que hereda de (ApplicationController) dentro
de la clase Articulos es donde definiremos los metodos de nuestra aplicación

# Definimos un nuevo método en:
blog/app/controllers/articulos_controller.rb

# El fichero nos quedaría así:
class ArticulosController < ApplicationController
  def nuevo
  end
end

# Sabemos que los controladores van asociados a una vista que mostrará
# el contenido que queremos, por ellos debemos crear esa vista, vamos a:
blog/app/views/articulos

# Creamos un nuevo fichero:
nuevo.html.erb
# La extensión de este nombre de archivo es muy importante: la primera extensión define el formato
# de la plantilla, y la segunda extensión el manejador de plantilla que se usará.
# Y pondremos un texto de ejemplo:

'''
<div algin="center">
  <h1>Nuevo artículo</h1>
</div>
'''

Guardamos, ahora esta sera la vista que se mostrara cuando hagamos uso del controlador creado

# Solo resta agregar la ruta de nuestro controlador y nuestra vista en:
blog/config/routes.rb

# Abrimos el routes.rb y agregamos en la segunda linea la ruta de nuestro
# controlador, nos quedaría así:

Rails.application.routes.draw do
  get 'articulos/nuevo'
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes"....... etc...

Como vemos, le hemos dicho que a rails que esa será la ruta que ejecutará un controlador
llamado (articulo) cuya vista es (nuevo) por lo que si visitamos:

127.0.0.1:3000/articulos/nuevo # Deberíamos visualizar la plantilla que creamos

# Por defecto rails carga el index 'Welcome aboard...' en el 127.0.0.1:3000, si queremos
# que nuestra vista creada se cargue predeterminadamente buscamos en:
blog/config/routes.rb 
# la línea root que esta comentada: # root 'welcome#index'
# la descomentamos y le damos la nueva ruta que va a nuestra vista para que se cargue por defecto:
root 'articulos/nuevo'

Guardamos y si vamos al localhost:3000 deberíamos ver nuestra vista cargada por defecto.

$ bin/rake routes # En la carpeta del proyecto, podremos ver las rutas establecidas para los controladores
# y vistas de nuestra aplicación 

###################################################################################
##### Creando aplicacion para hacer publicaciones (autor, titulo y contenido) #####
###################################################################################

$ rails new publicaciones

$ cd publicaciones

$ rails server

# Generamos el controlador y las vista de nuestra pagina principal
$ rails generate controller welcome index

$ rails generate scaffold Post autor:string titulo:string contenido:text 
# Se generaron los controladores y vistas que contienen los formularios con los campos establecidos

$ rake db:migrate # Se crearon las tablas correspondientes en la base de datos de desarrollo Sqlite3

# http://127.0.0.1:3000/posts
# Podemos visualizar la lista de publicaciones asi como enlaces a las operaciones CRUD que se crearon
