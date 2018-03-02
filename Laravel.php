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

// Instalar PHP:

# apt-get install php5 php5-gd php5-mysql

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

$ composer global require "laravel/installer"

// La salida de este comando:

Changed current directory to /home/aosorio/.config/composer
Using version ^2.0 for laravel/installer
./composer.json has been created
Loading composer repositories with package information
Updating dependencies (including require-dev)
Package operations: 11 installs, 0 updates, 0 removals
  - Installing symfony/process (v3.4.5): Downloading (100%)         
  - Installing symfony/filesystem (v3.4.5): Downloading (100%)         
  - Installing symfony/polyfill-mbstring (v1.7.0): Downloading (100%)         
  - Installing psr/log (1.0.2): Downloading (100%)         
  - Installing symfony/debug (v3.4.5): Downloading (100%)         
  - Installing symfony/console (v3.4.5): Downloading (100%)         
  - Installing guzzlehttp/promises (v1.3.1): Downloading (100%)         
  - Installing psr/http-message (1.0.1): Downloading (100%)         
  - Installing guzzlehttp/psr7 (1.4.2): Downloading (100%)         
  - Installing guzzlehttp/guzzle (6.3.0): Downloading (100%)         
  - Installing laravel/installer (v2.0.1): Downloading (100%)         
symfony/console suggests installing symfony/event-dispatcher ()
symfony/console suggests installing symfony/lock ()
Writing lock file
Generating autoload files

// Nos dice el directorio donde va a ser instalado laravel
// luego prosige con la instalación.

// Luego de la instalación, comprobamos la ruta donde está laravel con:

$ cd .composer/vendor/bin

ó

$ cd .config/composer/vendor/bin

// Si nos lleva sin error a alguno de los dos directorios, es que se instalo Laravel y
// esa es la ruta correcta de su ejecutable.

// Agregamos al final del .bashrc lo siguiente si funcionó la opcion 1 y guardamos:

PATH=$PATH:~/.composer/vendor/bin

// En mi caso, la ruta es diferente, es la 2
// entonces, agregamos al final del .bashrc:

PATH=$PATH:~/.config/composer/vendor/bin

// Aplicamos los cambios con el siguiente comando:

$ source .bashrc

// Actualizamos el composer:

$ composer global update

// Creamos un proyecto de laravel para probar:

$ laravel new nombre_del_proyecto

Crafting application...
Loading composer repositories with package information
Installing dependencies (including require-dev) from lock file
Your requirements could not be resolved to an installable set of packages.

  Problem 1
    - This package requires php >=7.1.3 but your PHP version (5.6.30) does not satisfy that requirement.
  Problem 2
    - Installation request for doctrine/inflector v1.3.0 -> satisfiable by doctrine/inflector[v1.3.0].
    - doctrine/inflector v1.3.0 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 3
    - Installation request for dragonmantank/cron-expression v2.0.0 -> satisfiable by dragonmantank/cron-expression[v2.0.0].
    - dragonmantank/cron-expression v2.0.0 requires php >=7.0.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 4
    - Installation request for laravel/framework v5.6.7 -> satisfiable by laravel/framework[v5.6.7].
    - laravel/framework v5.6.7 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 5
    - Installation request for swiftmailer/swiftmailer v6.0.2 -> satisfiable by swiftmailer/swiftmailer[v6.0.2].
    - swiftmailer/swiftmailer v6.0.2 requires php >=7.0.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 6
    - Installation request for symfony/console v4.0.5 -> satisfiable by symfony/console[v4.0.5].
    - symfony/console v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 7
    - Installation request for symfony/css-selector v4.0.5 -> satisfiable by symfony/css-selector[v4.0.5].
    - symfony/css-selector v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 8
    - Installation request for symfony/debug v4.0.5 -> satisfiable by symfony/debug[v4.0.5].
    - symfony/debug v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 9
    - Installation request for symfony/event-dispatcher v4.0.5 -> satisfiable by symfony/event-dispatcher[v4.0.5].
    - symfony/event-dispatcher v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 10
    - Installation request for symfony/finder v4.0.5 -> satisfiable by symfony/finder[v4.0.5].
    - symfony/finder v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 11
    - Installation request for symfony/http-foundation v4.0.5 -> satisfiable by symfony/http-foundation[v4.0.5].
    - symfony/http-foundation v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 12
    - Installation request for symfony/http-kernel v4.0.5 -> satisfiable by symfony/http-kernel[v4.0.5].
    - symfony/http-kernel v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 13
    - Installation request for symfony/process v4.0.5 -> satisfiable by symfony/process[v4.0.5].
    - symfony/process v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 14
    - Installation request for symfony/routing v4.0.5 -> satisfiable by symfony/routing[v4.0.5].
    - symfony/routing v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 15
    - Installation request for symfony/translation v4.0.5 -> satisfiable by symfony/translation[v4.0.5].
    - symfony/translation v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 16
    - Installation request for symfony/var-dumper v4.0.5 -> satisfiable by symfony/var-dumper[v4.0.5].
    - symfony/var-dumper v4.0.5 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 17
    - Installation request for doctrine/instantiator 1.1.0 -> satisfiable by doctrine/instantiator[1.1.0].
    - doctrine/instantiator 1.1.0 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 18
    - Installation request for nunomaduro/collision v2.0.0 -> satisfiable by nunomaduro/collision[v2.0.0].
    - nunomaduro/collision v2.0.0 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 19
    - Installation request for phpdocumentor/reflection-docblock 4.3.0 -> satisfiable by phpdocumentor/reflection-docblock[4.3.0].
    - phpdocumentor/reflection-docblock 4.3.0 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 20
    - Installation request for phpunit/php-code-coverage 6.0.1 -> satisfiable by phpunit/php-code-coverage[6.0.1].
    - phpunit/php-code-coverage 6.0.1 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 21
    - Installation request for phpunit/php-timer 2.0.0 -> satisfiable by phpunit/php-timer[2.0.0].
    - phpunit/php-timer 2.0.0 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 22
    - Installation request for phpunit/php-token-stream 3.0.0 -> satisfiable by phpunit/php-token-stream[3.0.0].
    - phpunit/php-token-stream 3.0.0 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 23
    - Installation request for phpunit/phpunit 7.0.2 -> satisfiable by phpunit/phpunit[7.0.2].
    - phpunit/phpunit 7.0.2 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 24
    - Installation request for phpunit/phpunit-mock-objects 6.0.1 -> satisfiable by phpunit/phpunit-mock-objects[6.0.1].
    - phpunit/phpunit-mock-objects 6.0.1 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 25
    - Installation request for sebastian/comparator 2.1.3 -> satisfiable by sebastian/comparator[2.1.3].
    - sebastian/comparator 2.1.3 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 26
    - Installation request for sebastian/diff 3.0.0 -> satisfiable by sebastian/diff[3.0.0].
    - sebastian/diff 3.0.0 requires php ^7.1 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 27
    - Installation request for sebastian/environment 3.1.0 -> satisfiable by sebastian/environment[3.1.0].
    - sebastian/environment 3.1.0 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 28
    - Installation request for sebastian/exporter 3.1.0 -> satisfiable by sebastian/exporter[3.1.0].
    - sebastian/exporter 3.1.0 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 29
    - Installation request for sebastian/global-state 2.0.0 -> satisfiable by sebastian/global-state[2.0.0].
    - sebastian/global-state 2.0.0 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 30
    - Installation request for sebastian/object-enumerator 3.0.3 -> satisfiable by sebastian/object-enumerator[3.0.3].
    - sebastian/object-enumerator 3.0.3 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 31
    - Installation request for sebastian/object-reflector 1.1.1 -> satisfiable by sebastian/object-reflector[1.1.1].
    - sebastian/object-reflector 1.1.1 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 32
    - Installation request for sebastian/recursion-context 3.0.0 -> satisfiable by sebastian/recursion-context[3.0.0].
    - sebastian/recursion-context 3.0.0 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 33
    - Installation request for theseer/tokenizer 1.1.0 -> satisfiable by theseer/tokenizer[1.1.0].
    - theseer/tokenizer 1.1.0 requires php ^7.0 -> your PHP version (5.6.30) does not satisfy that requirement.
  Problem 34
    - laravel/framework v5.6.7 requires php ^7.1.3 -> your PHP version (5.6.30) does not satisfy that requirement.
    - laravel/tinker v1.0.3 requires illuminate/console ~5.1 -> satisfiable by laravel/framework[v5.6.7].
    - Installation request for laravel/tinker v1.0.3 -> satisfiable by laravel/tinker[v1.0.3].

Application ready! Build something amazing.

// En caso de que el comando anterior no funcione probar:

$ composer create-project laravel/laravel nombre_del_proyecto --prefer-dist

ó

$ composer create-project --prefer-dist laravel/laravel nombre_proyecto version_laravel