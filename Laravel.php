##### Guía del Framework Laravel by dM #####

####################################
##### ¿Como funciona Laravel? ######
####################################

1) Un usuario ingresa a una página o sistema web creado con Laravel, a ese ingreso se
le llama "solicitud" o "petición".

2) Esa "solicitud" o "petición" llega a un archivo llamado rutas, las rutas es un archivo
donde especificamos que rutas o direcciones url están disponible en un sistema/página web.

Por ejemplo si yo tengo una página llamada misitio.com y puedo acceder a "misitio.com/registro"
donde muestra un formulario para registrarse, "/registro" es una ruta.
por tanto se debe definir en ese archivo donde están las rutas. si intento
acceder a "misitio.com/prueba" y me da error, eso quiere decir que esa ruta no existe o no ha sido
especificada en el archivo de rutas.

Si una ruta declarada en las rutas es visitada, es posible que luego de pasar por las rutas ahora
vaya a un controlador, esto solo si es necesario, el controlador es la parte donde el framework realiza
operaciones con los datos, inserción, lista, actualización de la base de datos, calculos con los datos.

##################################
##### Instalación de Laravel #####
##################################

Importante: Esta guía fue probada usando la versión 7.0 de php, Composer 1.6.3, Laravel Installer 1.5.0, Laravel Framework 5.4.36 en GNU/Linux Debian 9 Stretch.

Laravel es un framework de código abierto para desarrollar aplicaciones y servicios web con
PHP 5 y PHP 7. Su filosofía es desarrollar código PHP de forma elegante y simple, evitando
el "código espagueti". Fue creado en 2011 y tiene una gran influencia de frameworks como
Ruby on Rails, entre otros...

Gran parte de Laravel está formado por dependencias, especialmente de Symfony, esto implica
que el desarrollo de Laravel dependa también del desarrollo de sus dependencias.

##### Características #####

-Sistema de ruteo, también RESTful3
-Blade, Motor de plantillas4​
-Peticiones Fluent
-Eloquent ORM7
-Basado en Composer
-Soporte para el caché
-Soporte para MVC
-Usa componentes de Symfony
-Adopta las especificaciones PSR-212​ y PSR-4

##### Instalación de paquetes necesarios #####

// Instalar Apache:

# apt-get install apache2 

// Instalar PHP y extras para apache:

# apt-get install php7.0

# aptitude install php7.0-gd php7.0-mysql libapache2-mod-php7.0 php-zip php7.0-mbstring php7.0-xml php7.0-intl php-symfony-intl php7.0-libsodium

# aptitude install php-symfony-config php-symfony-dependency-injection php-symfony-expression-language php-symfony-yaml php-symfony-browser-kit php-libsodium php-symfony-http-kernel php-uuid

// Instalar Mysql para usarlo en un futuro como motor de base de datos:

# apt-get install mysql-server

##### Para seguir necesitamos composer #####

Composer es un manejador de dependencias, no un gestor de paquetes. Pero es cierto
que trata con paquetes y librerías, la instalación siempre es local para cualquier
proyecto, las librerías se instalan en un directorio por defecto (normalmente es /vendor).
Composer es capaz de instalar las librerías que requiere tu proyecto con las versiones
que necesiten. ¿Y si mis librerías dependen de otras? También es capaz de resolver eso
y descargar todo lo necesario para que funcione y así quitarnos del dolor de
cabeza de hacer todo eso de forma manual.

--- ¿Qué problemas resuelve Composer? ---

Tienes un proyecto que depende de ciertas librerías desarrolladas por terceros, y a su
vez, éstas librerías también dependen de otras (tú no tienes porqué conocer estas librerías)
lo que hace Composer en este caso es averiguar que librerías deben instalarse; es decir, resuelve
todas las dependencias indirectas y descarga automáticamente la versión correcta de cada paquete.

// Descargamos composer:

$ php -r "readfile('https://getcomposer.org/installer');" | php

// El comando anterior nos descarga el fichero "composer.phar"

// Movemos composer a /usr/local/bin, lo cual nos permitirá que este disponible
// desde donde sea que lo necesitemos:

# mv composer.phar /usr/local/bin/composer

// Comprobamos la instalación con el siguiente comando:

$ composer

##### Instalación de Laravel #####

Laravel utiliza Composer para manejar las dependencies. entonces,
antes de usar Laravel, hay que tener instalado Composer en nuestra máquina.

Primero descargamos el instalador de Laravel vía Composer

$ composer global require "laravel/installer=~1.1"

// La salida de este comando:

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

// Nos dice el directorio donde va a ser instalado laravel
// luego prosige con la instalación.

// Luego de la instalación, comprobamos la ruta donde está laravel con:

$ cd .config/composer/vendor/bin

// Si navegamos bien hacia ese directorio, entonces seguimos, agregamos al final del .bashrc lo siguiente:

PATH=$PATH:~/.config/composer/vendor/bin

// Aplicamos los cambios con el siguiente comando:

$ source .bashrc

// El primer comando el una comprobación corta, el segundo es completa y larga, recomendado el primero.

// Creamos un proyecto de laravel para probar:

$ laravel new nombre_del_proyecto

##### Otra forma de generar el proyecto, vía composer #####

// En caso de que el comando anterior no funcione porque se va a quejar porque el php
instalado no es superior al 7.2 entonces probar:

$ composer create-project --prefer-dist laravel/laravel mysite "5.4.*"

// Con el comando anterior lo que estamos declarando que que cree el proyecto "mysite"
// y que se use la ultima actualización de la versión 5.4 de Laravel, que es compatible con
// el php7.0 que está instalado.

// Ahora vamos a corre el servidor local de desarrllo usando el script Artisan.

// Este comando inicia el servidor de desarrllo en http://localhost:8000:

// Entramos en el dirctorio del proyecto y corremos el servidor de desarrollo:

$ php artisan serve

// Si corre sin problemas podemos visitar: localhost:8000/ y visualizar Laravel en letras grandes.

#############################################################################
##### En la siguiente sección instalaremos Laravel en su última versión #####
#############################################################################

Importante: Esta guía fue probada usando la versión 7.2 de php, Composer 1.6.3, Laravel Installer 2.0, Laravel Framework 5.6.11 en GNU/Linux Debian 9 Stretch.

$ sudo apt-get install apt-transport-https lsb-release ca-certificates
$ sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
$ echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list
$ sudo apt-get update

##### Instalación de paquetes necesarios #####

$ sudo apt-get install php7.2-cli

// Verificar la versión de php que se instaló.

$ php -v

// Instalar Apache:

# apt-get install apache2

// Instalar dependencias extras necesarias:

# aptitude install php7.2-gd php7.2-mysql libapache2-mod-php7.2 php-zip php7.2-mbstring php7.2-xml php7.2-intl

# aptitude install php-symfony-config php-symfony-dependency-injection php-symfony-expression-language php-symfony-yaml php-symfony-browser-kit php-libsodium php-symfony-http-kernel php-uuid

// Instalar Mysql para usarlo en un futuro como motor de base de datos

# apt-get install mysql-server

// Descargamos composer:

$ php -r "readfile('https://getcomposer.org/installer');" | php

// El comando anterior nos descarga el fichero "composer.phar"

// Movemos composer a /usr/local/bin, lo cual nos permitirá que este disponible
// desde donde sea que lo necesitemos:

# mv composer.phar /usr/local/bin/composer

// Comprobamos la instalación con el siguiente comando:

$ composer

##### Instalación de Laravel #####

$ composer global require "laravel/installer"

// Luego de la instalación, comprobamos la ruta donde está laravel con:

$ cd .config/composer/vendor/bin

// Si navegamos bien hacia ese directorio, entonces seguimos, agregamos al final del .bashrc lo siguiente:

PATH=$PATH:~/.config/composer/vendor/bin

// Aplicamos los cambios con el siguiente comando:

$ source .bashrc

// El primer comando el una comprobación corta, el segundo es completa y larga, recomendado el primero.

// Creamos un proyecto de laravel para probar:

$ laravel new mysite

// Luego de la generación del proyecto e instalación de dependendencias
// Entramos en el dirctorio del proyecto y corremos el servidor de desarrollo:

$ php artisan serve

##### Otra forma de generar el proyecto, vía composer #####

// Si corre sin problemas podemos visitar: localhost:8000/ y visualizar Laravel en letras grandes.

// Otra forma de generar el proyecto es usando composer, y especificando versiones:

$ composer create-project --prefer-dist laravel/laravel mysite

// Luego de la generación del proyecto e instalación de dependendencias
// Entramos en el dirctorio del proyecto y corremos el servidor de desarrollo:

$ php artisan serve

#######################
##### Tips/Extras #####
#######################

// Para cambiar el puerto donde se esta sirviendo el proyecto:
	
$ php artisan serve --port=9000

// Para cambiar la ip y el puerto donde se esta sirviendo el proyecto:

$ php artisan serve --host=192.168.0.100 --port=8000

// Para comprobar la versión de Laravel instalada:

$ php artisan --version

// Cuando se clona un proyecto de un repositorio, lo mas común es que se omita la carpeta /vendor
// que contiene los paquetes/librerías requeridas por el proyecto, entonces las instalamos con:

$ composer install
