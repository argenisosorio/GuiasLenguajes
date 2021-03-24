=====================
Guía de Laravel by dM
=====================

Usaremos $ para describir los comandos que se usaran con usuario regular.

Usaremos # para describir los comandos que se usaran con superusuario.

================
¿Qué es Laravel?
================

Laravel es un framework de código abierto para desarrollar aplicaciones y
servicios web con PHP 5 y PHP 7. Su filosofía es desarrollar código PHP de forma
elegante y simple, evitando el "código espagueti". Fue creado en 2011 y tiene
una gran influencia de frameworks como Ruby on Rails, entre otros...

Gran parte de Laravel está formado por dependencias, especialmente de Symfony,
esto implica que el desarrollo de Laravel dependa también del desarrollo de sus
dependencias.

=======================
¿Como funciona Laravel?
=======================

Laravel utiliza el paradigma del "Modelo-vista-controlador"

1) Un usuario ingresa a una página o sistema web creado con Laravel, a ese
ingreso se le llama "solicitud" o "petición".

2) Esa "solicitud" o "petición" llega a un archivo llamado rutas, las rutas es
un archivo donde especificamos que rutas o direcciones url están disponible en
un sistema/página web.

Por ejemplo si yo tengo una página llamada misitio.com y puedo acceder a
"misitio.com/registro" donde muestra un formulario para registrarse, "/registro"
es una ruta. por tanto se debe definir en ese archivo donde están las rutas. si
intento acceder a "misitio.com/prueba" y me da error, eso quiere decir que esa
ruta no existe o no ha sido especificada en el archivo de rutas.

Si una ruta válida es visitada, el paso siguiente es ir a un controlador o una
vista, el ir a un controlador solo se hará si es necesario, el controlador es la
parte donde Laravel realiza operaciones con los datos, inserción, listar,
actualización de la base de datos, calculos, ejecutar funciones con los datos,
entre otros. En el controlador es donde está la lógica de un sistema/página web.

El controlador puede acceder al modelo, el modelo son las tablas de la base de
datos reflejadas en archivos php.

Entonces un controlador puede solicitar al modelo que le traiga todos los
usuarios registrados en el sistema para, el controlador los recibe de vuelta y
ahora puede mandarlos a una vista para que sean mostrados en una página simple.

La segunda opción es ir a una vista directamente, una vista es una pagina simple
donde se muestran textos, imagenes, videos, etc, sin interactuar con otros
elementos del sistema, sin consultas ni nada.

Otro elemento del paradigma de Laravel son los Middlewares, que no es mas que un
filtro. Imaginemos que tenemos un panel de administración del sistema, y no
queremos que todos los usuarios puedan acceder a ese panel, si no solo usuarios
con permisos adecuados, entonces ahí aparecen los middlewares y sus
funcionalidades. Las rutas y los controladores pueden acceder a los middlewares.

===============
Características
===============

-Sistema de ruteo, también RESTful3
-Blade, Motor de plantillas4​
-Peticiones Fluent
-Eloquent ORM7
-Basado en Composer
-Soporte para el caché
-Soporte para MVC
-Usa componentes de Symfony
-Adopta las especificaciones PSR-212​ y PSR-4

=================================================================
Instalación de paquetes necesarios para la instalación de Laravel
=================================================================

**Importante** Esta guía fue probada en GNU/Linux Debian 9 Stretch
usando las siguientes versiones:

Instalar Apache:

# apt-get install apache2 

-----

Instalar PHP y extras para apache:

# apt-get install php7.0

# aptitude install php7.0-gd php7.0-mysql libapache2-mod-php7.0 php-zip php7.0-mbstring php7.0-xml php7.0-intl php-symfony-intl php7.0-libsodium

# aptitude install php-symfony-config php-symfony-dependency-injection php-symfony-expression-language php-symfony-yaml php-symfony-browser-kit php-libsodium php-symfony-http-kernel php-uuid

-----

Instalar Mysql para usarlo en un futuro como motor de base de datos:

# apt-get install mysql-server

================================
Para seguir necesitamos composer
================================

Composer es un manejador de dependencias, no un gestor de paquetes. Pero es
cierto que trata con paquetes y librerías, la instalación siempre es local para
cualquier proyecto, las librerías se instalan en un directorio por defecto
(normalmente es /vendor). Composer es capaz de instalar las librerías que
requiere tu proyecto con las versiones que necesiten. ¿Y si mis librerías
dependen de otras? También es capaz de resolver eso y descargar todo lo
necesario para que funcione y así quitarnos del dolor de cabeza de hacer todo
eso de forma manual.

=================================
¿Qué problemas resuelve Composer?
=================================

Tienes un proyecto que depende de ciertas librerías desarrolladas por terceros,
y a su vez, éstas librerías también dependen de otras (tú no tienes porqué
conocer estas librerías) lo que hace Composer en este caso es averiguar que
librerías deben instalarse; es decir, resuelve todas las dependencias indirectas
y descarga automáticamente la versión correcta de cada paquete.

Descargamos composer:

$ php -r "readfile('https://getcomposer.org/installer');" | php

El comando anterior nos descarga el fichero "composer.phar"

-----

Movemos composer a /usr/local/bin, lo cual nos permitirá que este disponible
desde donde sea que lo necesitemos:

# mv composer.phar /usr/local/bin/composer

-----

Comprobamos la instalación con el siguiente comando:

$ composer

======================
Instalación de Laravel
======================

Laravel utiliza Composer para manejar las dependencies. entonces, antes de usar
Laravel, hay que tener instalado Composer en nuestra máquina.

Primero descargamos el instalador de Laravel vía Composer

$ composer global require "laravel/installer=~1.1"

La salida de este comando:

Changed current directory to /home/user/.config/composer
./composer.json has been created
Loading composer repositories with package information
Updating dependencies (including require-dev)
Package operations: 10 installs, 0 updates, 0 removals
  - Installing symfony/process (v3.4.6): Downloading (100%)         
  - Installing psr/log (1.0.2): Downloading (100%)         
  - Installing symfony/debug (v3.4.6): Downloading (100%)         
  - Installing symfony/polyfill-mbstring (v1.7.0): Downloading (100%)         
  - Installing symfony/console (v3.4.6): Downloading (100%)         
  - Installing guzzlehttp/promises (v1.3.1): Downloading (100%)         
  - Installing psr/http-message (1.0.1): Downloading (100%)         
  - Installing guzzlehttp/psr7 (1.4.2): Downloading (100%)         
  - Installing guzzlehttp/guzzle (6.3.0): Downloading (100%)         
  - Installing laravel/installer (v1.3.4): Downloading (100%)         
symfony/polyfill-mbstring suggests installing ext-mbstring (For best performance)
symfony/console suggests installing symfony/event-dispatcher ()
symfony/console suggests installing symfony/lock ()
Writing lock file
Generating autoload files

Nos dice el directorio donde va a ser instalado laravel luego prosige con la
instalación.

Luego de la instalación, comprobamos la ruta donde está laravel con:

$ cd .config/composer/vendor/bin

Si navegamos bien hacia ese directorio, entonces seguimos, agregamos al final
del .bashrc lo siguiente:

PATH=$PATH:~/.config/composer/vendor/bin

Aplicamos los cambios con el siguiente comando:

$ source .bashrc

El primer comando el una comprobación corta, el segundo es completa y larga,
recomendado el primero.

Creamos un proyecto de laravel para probar:

$ laravel new nombre_del_proyecto

===============================================
Otra forma de generar el proyecto, vía composer
===============================================

En caso de que el comando anterior no funcione porque se va a quejar porque el
php instalado no es superior al 7.2 entonces probar:

$ composer create-project --prefer-dist laravel/laravel mysite "5.4.*"

Con el comando anterior lo que estamos declarando que que cree el proyecto
"mysite" y que se use la ultima actualización de la versión 5.4 de Laravel, que
es compatible con el php7.0 que está instalado.

Ahora vamos a correr el servidor local de desarrllo usando el script Artisan.

Este comando inicia el servidor de desarrllo en http://localhost:8000:

Entramos en el dirctorio del proyecto y corremos el servidor de desarrollo:

$ php artisan serve

Si corre sin problemas podemos visitar: localhost:8000/ y visualizar Laravel en
letras grandes.

=================================================================
En la siguiente sección instalaremos Laravel en su última versión
=================================================================

**Importante** Esta guía fue probada usando la versión 7.2 de php,
Composer 1.6.3, Laravel Installer 2.0, Laravel Framework 5.6.11 en
GNU/Linux Debian 9 Stretch.

$ sudo apt-get install apt-transport-https lsb-release ca-certificates

$ sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg

$ echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list

$ sudo apt-get update

==================================
Instalación de paquetes necesarios
==================================

Buscamos la versión de php disponible en el repositorio.

$ aptitude search search php

-----

Instalamos la versión disponible del paquete

$ sudo apt-get install php7.2-cli

-----

Verificar la versión de php que se instaló.

$ php -v

-----

Instalar Apache:

# apt-get install apache2

-----

Instalar dependencias extras necesarias:

# aptitude install php7.2-gd php7.2-mysql libapache2-mod-php7.2 php-zip php7.2-mbstring php7.2-xml php7.2-intl

# aptitude install php-symfony-config php-symfony-dependency-injection php-symfony-expression-language php-symfony-yaml php-symfony-browser-kit php-libsodium php-symfony-http-kernel php-uuid

-----

Instalar Mysql para usarlo en un futuro como motor de base de datos

# apt-get install mysql-server

-----

Descargamos composer:

$ php -r "readfile('https://getcomposer.org/installer');" | php

El comando anterior nos descarga el fichero "composer.phar"

-----

Movemos composer a /usr/local/bin, lo cual nos permitirá que este disponible
desde donde sea que lo necesitemos:

# mv composer.phar /usr/local/bin/composer

-----

Comprobamos la instalación con el siguiente comando:

$ composer

======================
Instalación de Laravel
======================

Instalar composer

-----

Instalar Laravel

$ composer global require "laravel/installer"

-----

Luego de la instalación, comprobamos la ruta donde está laravel con:

$ cd .config/composer/vendor/bin

-----

Si navegamos bien hacia ese directorio, entonces seguimos, agregamos al final
del .bashrc lo siguiente:

PATH=$PATH:~/.config/composer/vendor/bin

-----

Aplicamos los cambios con el siguiente comando:

$ source .bashrc

El primer comando es para una comprobación corta, el segundo es completa y
larga, recomendado el primero.

-----

Creamos un proyecto de laravel para probar:

$ laravel new mysite

Luego de la generación del proyecto e instalación de dependendencias

-----

Entramos en el dirctorio del proyecto y corremos el servidor de desarrollo:

$ php artisan serve

Si corre sin problemas podemos visitar: localhost:8000/ y visualizar Laravel en
letras grandes.

===============================================
Otra forma de generar el proyecto, vía composer
===============================================

Otra forma de generar el proyecto es usando composer, y especificando versiones:

$ composer create-project --prefer-dist laravel/laravel mysite

-----

Luego de la generación del proyecto e instalación de dependendencias

Entramos en el dirctorio del proyecto y corremos el servidor de desarrollo:

$ php artisan serve

===========
Tips/Extras
===========

Para comprobar la versión de Laravel instalada entramos en el directorio de un
proyecto creado:

$ php artisan --version

-----

Para cambiar el puerto donde se esta sirviendo el proyecto:
	
$ php artisan serve --port=9000

-----

Para cambiar la ip y el puerto donde se esta sirviendo el proyecto:

$ php artisan serve --host=192.168.0.100 --port=8000

-----

Si se va a servir el proyecto por una url diferente a localhost, algunas cosas
como las imágenes puede ser que sigan siendo servidas por localhost por tanto se
puede configurar la variable APP_URL en el archivo .env que está oculto en el
directorio raíz del proyecto:

#APP_URL=http://localhost
APP_URL=http://192.168.0.100

Cuando se clona un proyecto de un repositorio, lo mas común es que se omita la
carpeta /vendor que contiene los paquetes/librerías requeridas por el proyecto,
entonces las instalamos con:

$ composer install

===================================
Estructura del proyecto con Laravel
===================================

Vamos a comentar los principales directorios de la estructura de Laravel para
ello me he ayudado de la documentación de la estructura en español de Laravel,
donde puedes encontrar información más detallada:

app: contiene los modelos, y el código base de nuestra aplicación, incluirá
los directorios Console, Http y Providers.

resources/views: contiene las vistas, donde usaremos el motor de plantillas Blade.

app/Http/Controllers: aquí será donde se definirán los controladores.

app/Http/routes.php: para la definición de las rutas.

app/config/app.php: contiene configuración general de la aplicación.

public: carpeta pública desde dónde se inicia el proceso de ejecución de una
aplicación Laravel.

================================================
Actualizar proyectos de Laravel luego de un pull
================================================

$ composer install

$ npm install

$ composer dumpautoload

$ php artisan migrate

===========================
Limpiar la cache en Laravel
===========================

Ejecute el siguiente comando para borrar la memoria caché de la aplicación
Laravel.

$ php artisan cache:clear

==============================================================
Eliminar rastros de la configuración de un proyecto en Laravel
==============================================================

Elimina rastros de la configuración del sistema y las carga de nuevo, es decir,
es como si borraras los .pyc en proyectos de python.

$ php artisan config:cache

================================================
Borrar la caché de ruta de su aplicación Laravel
================================================

Para borrar el caché de ruta de su aplicación Laravel, ejecute el siguiente
comando

$ php artisan route:clear

=============================
Borrar caché de configuración
=============================

Puede usar config:clear para borrar la caché de configuración de la aplicación
Laravel.

$ php artisan config:clear

=================================
Borrar caché de vistas compiladas
=================================

Además, es posible que deba borrar los archivos de vista compilados de su
aplicación Laravel. Para borrar los archivos de vista compilados, ejecute el
siguiente comando desde la terminal.

$ php artisan view:clear

=================================
Configurar Laravel con postgresql
=================================

Configurar base de datos de postgresql en el archivo .env:

DB_CONNECTION=pgsql
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=nombre_base_de_datos
DB_USERNAME=usuario_base_de_datos
DB_PASSWORD=contrasena_base_de_datos

=============================
Configurar Laravel con sqlite
=============================

Instalar el paquete de sqlite para php.

# apt install php7.3-sqlite3

-----

Crear un archivo database.sqlite en la ruta my_project/database.

my_project/database$ touch database.sqlite

-----

Configurar el fichero .env, debemos poner la ruta absoluta de la db.

DB_CONNECTION=sqlite
APP_URL=http://127.0.0.1
DB_PORT=3306
DB_DATABASE=/home/user/my_project/database/database.sqlite
DB_USERNAME=homestead
DB_PASSWORD=secret

-----

Una vez configurada el gestor de base de datos, realizamos las migraciones.

$ php artisan migrate

-----

Levantar el servidor de desarrollo.

$ php artisan serve

===========================
Comandos de artisan y otros
===========================

Para conocer el listado completo de los comandos disponibles ejecutamos en
consola, en el directorio raíz de un proyecto de Laravel.

$ php artisan list

-----

Sacar la aplicación del modo de mantenimiento.

$ php artisan up

-----

Poner la aplicación en modo de mantenimiento.

$ php artisan down

-----

Para ver el listado completo de rutas, Como resultado nos mostrará un listado de
todas las rutas de la aplicación con la información sobre el método HTTP, la
URI, la acción, el nombre y los middleware definidos para cada ruta, con lo
cual, entre otras cosas, podemos verificar que todas las rutas de nuestra
aplicación están bien definidas.

php artisan route:list

-----

Mismo que el anterior pero más compacta la información.

php artisan route:list -c

-----

$ php artisan migrate:refresh

-----

Omite los métodos down o los rollbacks eliminando todas las tablas para luego
ejecutar los métodos up.

$ php artisan migrate:fresh

-----

El comando dump-autoload actualiza la información del cargador automático de
clases. Este comando es útil cuando añades nuevas clases y no quieres ejecutar
el comando install o update.

$ composer dumpautoload

-----

Con este comando Laravel compilará todos los paquetes que se encuentran en
node_modules y unificará los archivos que se encuentran en el directorio
resources/js y resources/sass a los archivos app.js y app.css respectivamente.

$ npm run dev

-----

Con este comando Laravel compilará todos los paquetes que se encuentran en
node_modules y unificará los archivos que se encuentran en el directorio
resources/js y resources/sass a los archivos app.js y app.css respectivamente.

$ npm run prod

-----

npm run dev combina todos sus componentes de Vue y otros archivos JavaScript en
un archivo combinado compatible con el navegador.

npm run watch hace lo mismo, pero luego permanece activo y "observa" las
actualizaciones de sus archivos .vue y .js. Si detecta un cambio, reconstruirá
el archivo compatible con el navegador para que pueda actualizar la página. 

$ npm run watch

Diferencias entre run dev y run prod
====================================

run dev: Compilar para desarrollo, los archivos resultantes mantienen el código
fuente desminificados. Las herramientas usadas en el navegador identifican los
objetos y componentes para poder depurar el código.

run prod -> compilar para producción, los archivos resultantes estan
minificados. Las herramientas de desarrollo usadas en el navegador no pueden
acceder a los componentes u objetos por lo que es complicado poder interactuar
con ellos a través del navegador.

===============
Seed y Seeders
===============

Una manera de cargar datos en la base de datos es utilizando los Seeders de
Laravel.

Laravel incluye un método simple para sembrar su base de datos con datos de
prueba utilizando clases semilla (Seed). Todas las clases de semillas se
almacenan en el directorio database/seeds. Las clases de semillas pueden tener
el nombre que desee, pero probablemente deberían seguir alguna convención
razonable, como nombretablaSeeder, etc. De manera predeterminada, se define una
clase DatabaseSeeder para usted. Desde esta clase, puede utilizar el método de
llamada para ejecutar otras clases semilla, lo que le permite controlar el orden
de siembra.

-----

Se puede aplicar un seeder de maner individual con el siguiente comando:

$ php artisan db:seed --class NombreDelSeeder

=============================================
Descargue y cargue bases de datos rápidamente
=============================================

Usando el paquete laravel-db-snapshots

Disponible desde > https://github.com/spatie/laravel-db-snapshots

Este paquete proporciona comandos Artisan para descargar y cargar rápidamente
bases de datos en una aplicación de Laravel.

Crear un dump

$ php artisan snapshot:create my-first-dump

Nos creara un archivo "my-first-dump.sql" en la ruta project/database/snapshots

-----

Crear otro dump

$ php artisan snapshot:create my-second-dump

-----

Cargar el primer dump

$ php artisan snapshot:load my-first-dump

-----

Cargar el último dump

$ php artisan snapshot:load --latest

-----

Listar todas las snapshots

$ php artisan snapshot:list

========================================
Script en bash para proyectos ya creados
========================================

#!/bin/bash

composer install

composer dumpautoload

npm install

php artisan migrate:fresh

echo " --- Regeneradas las tablas de la base de datos ---"

php artisan migrate

echo " --- Realizadas migraciones a la base de datos ---"

php artisan db:seed

echo "--- Guardados datos en la base de datos ---"

echo "--- Listo!!! ---"

====================================
Estructura de un proyecto en Laravel
====================================

Nota: Probado en Laravel 5

Todos los proyectos nuevos en Laravel 5.1 tienen la siguiente estructura de directorios:

app/
bootstrap/
config/
database/
public/
resources/
storage/
tests/
vendor/
.env
.env.example
.gitattributes
.gitignore
artisan
composer.json
composer.lock
gulpfile.js
package.json
phpspec.yml
phpunit.xml
readme.md
server.php

A continuación describiremos los directorios y archivos más importantes para que
nos ayuden a entender más el funcionamiento del framework.

=================
El directorio app
=================

App es usado para ofrecer un hogar por defecto a todo el código personal de tu
proyecto. Eso incluye clases que puedan ofrecer funcionalidad a la aplicación,
archivos de configuración y más. Es considerado el directorio más importante de
nuestro proyecto ya que es en el que más trabajaremos.

El directorio app tiene a su vez otros subdirectorios importantes pero uno de
los más utilizados es el directorio Http en el cuál ubicaremos nuestros
Controllers, Middlewares y Requestsen sus carpetas correspondientes, además
dentro del subdirectorio Http encontremos también el archivo routes.php donde
escribiremos las rutas de la aplicación.

A nivel de la raíz del directorio app encontraremos el modelo User.php, los
modelos comunmente se ubicarán a nivel de la raíz de la carpeta app aunque igual
es posible estructurarlos de la forma que queramos, por ejemplo, en una carpeta
llamada Models.

====================
El directorio config
====================

La configuración tanto para el framework como para tu aplicación se mantiene en
este directorio. La configuración de Laravel existe como un conjunto de archivos
PHP que contienen matrices clave-valor. Entre los archivos más usados del
directorio config se encuentran:

app.php : En este archivo nos puede interesar configurar el lenguaje de nuestra
aplicación, la zona horaria, los providers y aliases de las clases más comunes.

database.php : En este archivo podemos configurar principalmente el motor de
base de datos al cuál deseamos conectarnos.

======================
El directorio database
======================

Aquí se encontraran los archivos relacionados con el manejo de la base de datos.

Dentro de este directorio se encuentran los subdirectorios:

factories : Aquí escribiremos nuestros model factories.

migrations : Todas las migraciones que creamos se ubican en este subdirectorio.

seeds : Contiene todas las clases de tipo seed.

====================
El directorio public
====================

Dentro de este directorio colocaremos todos los recursos estáticos de nuestra
aplicación, es decir, archivos css, js, imágenes y fuentes.

Es recomendable crear una carpeta por cada tipo de recurso.

=======================
El directorio resources
=======================

Dentro de este directorio se encuentran los subdirectorios:

assets : Aquí se ubican todos los archivos less de nuestra aplicación (útil para
desarrolladores front-end).

lang : Aquí se encuentran todos los archivos de internacionalización, es decir,
los archivos para poder pasar nuestro proyecto de un idioma a otro.

Normalmente habrá una carpeta por cada idioma, ejemplo:
en : idioma inglés
es : idioma español

views : Aquí ubicaremos nuestras vistas en formato php o php.blade, es
recomendable crear una carpeta por cada controlador, además agregar una carpeta
templates para las plantillas. Una plantilla es una vista general, que tiene
segmentos que pueden ser reemplazados mediante la herencia de plantillas.

=====================
El directorio storage
=====================

Cuando Laravel necesita escribir algo en el disco, lo hace en el directorio
storage. Por este motivo, tu servidor web debe poder escribir en esta ubicación.
Aquí podemos encontrar otros directorios entre los cuales el más relevante es el
subdirectorio framework, es ahí donde se almacena el cache y las vistas
compiladas.

===================
El directorio tests
===================

Aquí escribiremos los archivos de pruebas que serán ejecutadas posteriormente
por phpunit.

==============================
El archivo .env y .env.example
==============================

El archivo .env no existe cuando instalamos laravel, en este archivo se
configurará el modo en que se ejecuta nuestra aplicación, por defecto será el
modo debug, además podemos configurar la conexión a la base de datos y la
conexión con el servidor de correo electronico. El archivo .env lo creamos
copiando el archivo .env.example y renombrando la copia como .env.

Por motivos de seguridad de la base de datos el archivo .env nunca se sube
cuando hacemos un push en nuestro repositorio. Es por eso que aparece escrito
dentro del archivo .gitignore en la raíz de nuestro proyecto.

=======================
El archivo package.json
=======================

Es el responsable de almacenar el nombre de las dependencias instaladas
catalogándolas principalmente en dos tipos: dependencias de desarrollo y
dependencias de la aplicación.

=======
Fuentes
=======

-https://tecadmin.net/clear-cache-laravel-5/
-https://solibeth.net/aprende-usar-seed-en-laravel