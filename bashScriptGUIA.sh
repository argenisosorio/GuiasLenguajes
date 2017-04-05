#############################################
##### Programación shell-script (bash) ######
#############################################

--- ¿Qué es un "Script"? ---

Es un archivo que contiene código escrito en determinado lenguaje de programación que el sistema usa para determinada tarea.
No es necesario que tenga una entrada externa ni interfaz gráfica, pero sí que provoque una salida de datos procesados
(por más de que el usuario no los vea).

El lenguaje usado por Bash está definido por su propio intérprete y combina la sintaxis de otros Shells, como el Korn Shell (ksh) o el C Shell (csh).
Muchos de los comandos que usualmente se usan en la consola también pueden usarse en los scripts, salvo aquellos que pertenecen estrictamente a una
distribución en particular.

--- Estructura de un Script ---

Para empezar debemos contar con un editor de texto, los archivos que guardamos con extensión .sh podrán ser ejecutados (o interpretados) por la consola
siempre y cuando la primera línea sea la siguiente:

#!/bin/bash

Esto le dice al sistema que deberá usar la consola para ejecutar el archivo. Además, el carácter # permite escribir comentarios.

echo // muestra un mensaje en pantalla, en este caso el típico "Hola Mundo". Si lo guardamos y ejecutamos con la consola veremos el resultado.

Bash (y otros shells) permiten programar scripts
--Bash (Bourne again shell) es un programa informático cuya función consiste en interpretar órdenes.
Está basado en la shell de Unix.

Script o programa shell: Fichero de texto conteniendo comandos externos e internos
que se ejecutan línea por línea, el programa puede contener, además de comandos
variables, constructores lógicos (if...then, AND, OR, etc.) y lazos (while, for, etc.)
funciones comentarios

--- Ejecución de un script ---

Los scripts deben empezar por el simbolo #! seguido del programa a usar para interpretar el script:

#!/bin/bash // Script de bash
#!/bin/sh // Script de shell
#!/usr/bin/perl // Script de perl

----------------------------

#Ejemplo de programa en bash para imprimir valores de variables
#!/bin/bash
VAL=10
VAL2=20
echo $VAL
echo $VAL2

----------------------------

Guardamos el script, ejemplo: prueba.sh, no es necesario ponerle
la extensión ya que la cabecera del script especifíca que programa
lo interpretará

Ejecución:

sh prueba.sh // Ejecutar un programa con bash.

bash prueba.sh // Ejecutar un programa con bash.

./script.sh // Otra manera de ejecutar el script.

sh prueba // Ejecutar un programa con bash, script guardado sin extension.

------------------------

#Ejemplo de programa en bash para ejecutar aplicaciones instaladas en el SO.
#!/bin/bash
#val=10
val='##### Abriendo Meld #####'
echo $val
/usr/bin/meld

------------------------

#Ejemplo de programa en bash que crea un fichero en el directorio en que se ejecuta.
#!/bin/bash
touch FFF.txt

------------------------

# Ejemplo de programa en bash que crea un fichero en un directorio específico.
#!/bin/bash
touch /home/aosorio/FFF.txt

------------------------

#Crear una carpeta, entrar en la carpeta y crear un fichero dentro.
#!/bin/bash
mkdir proyecto &&
cd proyecto &&
touch FFF.txt

------------------------

#Comprimir un directorio con un script de bash.
#!/bin/bash
DIRS="proyecto"
tar -cvf backup.tar $DIRS

------------------------

#A Simple Bash Example
#!/bin/bash  
echo "This is a shell script"  
ls -lah
echo "I am done running ls"  
SOMEVAR='text stuff'
echo "$SOMEVAR"

------------------------

#Usando una funcion, y viendo el funcionamiento de variables locales y globales.
#!/bin/bash
HOLA=Hola_global
function hola {
    local HOLA=Mundo_local
    echo $HOLA
}
echo $HOLA
hola
echo $HOLA

-----------------------

#Abrir un fichero específico con el editor gedit
#!/bin/bash
gedit /home/user/try.txt

-----------------------

#Llamado de una Funcion
#!/bin/bash
a='Estaba la pájara pinta'
function Imprimir {
    local a='sentada en un verde limón.'
    echo $a
}
echo $a
Imprimir
#echo $a

-----------------------

#!/bin/bash
#Capturar dato del teclado y asignarlo a una variable usando la funcion read.
#Pedir el dato al usuario
echo 'Introduzca un valor para la variable var:'
#Capturar el dato del teclado y guardarlo en la variable var
read var
#Imprimir el valor de la variable var
echo 'El valor de la variable var es' $var

-----------------------

#!/bin/bash
#Pedir varios datos y luego mostrarlos, ejemplo de concatenación
echo 'Introduzca el día con doble dígito:'
read dia
echo 'Introduzca el mes con doble dígito:'
read mes
echo 'Introduzca el anio con 4 dígitos:'
read anio
echo 'la fecha completa es:' $dia'-'$mes'-'$anio

-----------------------

#!/bin/bash
#Pedir datos al usuario para cambiar la fecha manualmente
echo 'Introduzca el día con doble dígito:'
read dia
echo 'Introduzca el mes con doble dígito:'
read mes
echo 'Introduzca el anio con 4 dígitos:'
read anio
sudo date --set $anio-$mes-$dia

-----------------------