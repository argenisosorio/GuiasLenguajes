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

// Instalar Apache.

# apt-get install apache2 

// Instalar PHP.

# apt-get install php5 php5-gd php5-mysql

// Instalar Mysql.

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

// Descargamos composer

$ php -r "readfile('https://getcomposer.org/installer');" | php

El comando anterior nos descarga el fichero "composer.phar"

// Movemos composer a /usr/local/bin, lo cual nos permitirá que este disponible
// desde donde sea que lo necesitemos.

# mv composer.phar /usr/local/bin/composer

// Comprobamos la instalación con el siguiente comando:

$ composer

##### Instalación de Laravel #####

$ composer global require "laravel/installer"

// Ahora debemos modificar el PATH para que pueda reconocer los comandos de Laravel y esto
se hace modificando el archivo .profile, para hacerlo ejecutamos el siguiente comando en la consola:

# sudo nano .profile

// Al abrirse el editor nos dirigimos hasta el final y agregamos lo siguiente:

PATH="$PATH:~/.composer/vendor/bin"

// Guardamos y luego actualizamos composer.

$ composer global update
