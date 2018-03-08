 ##### Guía del Framework Laravel by dM #####


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

# aptitude install php7.0-gd php7.0-mysql libapache2-mod-php7.0 php-zip

// Instalar Mysql:

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

// Actualizamos el composer:

$ composer self-update

ó

$ composer global update

// El primer comando el una comprobación corta, el segundo es completa y larga, recomendado el primero.

// Creamos un proyecto de laravel para probar:

$ laravel new nombre_del_proyecto

// En caso de que el comando anterior no funcione porque se va a quejar porque el php
instalado no es superior al 7.3 entonces probar:

$ composer create-project --prefer-dist laravel/laravel mysite "5.5.*"

// Con el comando anterior lo que estamos declarando que que cree el proyecto "mysite"
// y que se use la ultima actualización de la versión 5.5 de Laravel, que es compatible con
// el php7.0 que está instalado.

// Entramos en el dirctorio del proyecto y corremos el servidor de desarrollo:

$ php artisan serve

// Si corre sin problemas podemos visitar: localhost:8000/

// Para cambiar el puerto donde se esta sirviendo el proyecto:

$ php artisan serve --port=9000
