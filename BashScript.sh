#############################################
##### Programación shell-script (bash) ######
#############################################

##### ¿Qué es un "Script"? #####

Es un archivo que contiene código escrito en determinado lenguaje de programación que el sistema usa para determinada tarea.
No es necesario que tenga una entrada externa ni interfaz gráfica, pero sí que provoque una salida de datos procesados
(por más de que el usuario no los vea).

El lenguaje usado por Bash está definido por su propio intérprete y combina la sintaxis de otros Shells, como el Korn Shell (ksh) o el C Shell (csh).
Muchos de los comandos que usualmente se usan en la consola también pueden usarse en los scripts, salvo aquellos que pertenecen estrictamente a una
distribución en particular.

##### Estructura de un Script #####

Para empezar debemos contar con un editor de texto, los archivos que guardamos con extensión .sh podrán ser ejecutados (o interpretados) por la consola
siempre y cuando la primera línea sea la siguiente:

#!/bin/bash

Esto le dice al sistema que deberá usar la consola para ejecutar el archivo. Además, el carácter

# Permite escribir comentarios.

echo // muestra un mensaje en pantalla, en este caso el típico "Hola Mundo". Si lo guardamos y ejecutamos con la consola veremos el resultado.

Bash (y otros shells) permiten programar scripts
--Bash (Bourne again shell) es un programa informático cuya función consiste en interpretar órdenes.
Está basado en la shell de Unix.

Script o programa shell: Fichero de texto conteniendo comandos externos e internos
que se ejecutan línea por línea, el programa puede contener, además de comandos
variables, constructores lógicos (if...then, AND, OR, etc.) y lazos (while, for, etc.)
funciones comentarios

##################################
##### Ejecución de un script #####
##################################

Los scripts deben empezar por el simbolo #! seguido del programa a usar para interpretar el script:

#!/bin/bash // Script de bash
#!/bin/sh // Script de shell
#!/usr/bin/perl // Script de perl

#Ejemplo de programa en bash para imprimir valores de variables
#!/bin/bash
VAL=10
VAL2=20
echo $VAL
echo $VAL2

Guardamos el script, ejemplo: prueba.sh, no es necesario ponerle
la extensión ya que la cabecera del script especifíca que programa
lo interpretará

Ejecución:

sh prueba.sh // Ejecutar un programa con bash.

bash prueba.sh // Ejecutar un programa con bash.

./script.sh // Otra manera de ejecutar el script.

sh prueba // Ejecutar un programa con bash, script guardado sin extension.

#######################
##### Comentarios #####
#######################

#!/bin/bash
#Comentario de varias lineas
<<COMMENT1
comentario 1
comentario 2
comentario 3
echo -e "linea 1 \n"
echo "Linea 2"
COMMENT1

#!/bin/bash
#Comentario de varias lineas
: '
Solo para comentar cadenas, no variables ni expresiones ni condicionales.
'

##### Operadores de compacion #####

-eq equal to
-ne not equal to
-lt less than
-le less than or equal to
-gt greater than
-ge greater than or equal to

##### Operaciones con archivos #####

-s  file exists and is not empty
-f  file exists and is not a directory
-d  directory exists
-x  file is executable
-w  file is writable
-r  file is readable

##### Salto de línea #####

#!/bin/bash
#Salto de línea
echo -e "linea 1 \n"
echo "Linea 2"

#####################
##### Funciones #####
#####################

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

##################################
##### Pedir datos al usuario #####
##################################

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

#!/bin/bash
#Pedir datos al usuario para cambiar la hora manualmente
echo 'Introduzca la hora con doble dígito:'
read hora
echo 'Introduzca el minuto con doble dígito:'
read minuto
sudo date --set $hora:$minuto:00

###################################
##### Operaciones aritmeticas #####
###################################

#!/bin/sh
#Operaciones aritmeticas
num1=10
num2=5
suma=$((num1+num2))
echo $suma

num1=10
num2=5
resta=$((num1-num2))
echo $resta

num1=10
num2=5
multiplicacion=$((num1*num2))
echo $multiplicacion

num1=10
num2=5
division=$((num1/num2))
echo $division

#######################
##### If and Else #####
#######################

#!/bin/bash
#Pedir un dato y compararlo con el condicional
echo 'Introduzca un número:'
read count
if [ $count -eq 100 ]
then
  echo "Count is 100"
fi

----------------------

#!/bin/bash
#Pedir un dato y compararlo con varios condicionales
echo 'Introduzca un número:'
read cuenta
if [ $cuenta -eq 100 ]
then
  echo "cuenta es 100"
elif [ $cuenta -gt 100 ]
then
  echo "cuenta es mayor que 100"
else
  echo "cuenta es menor que 100"
fi

############################
##### == and && and or #####
############################

#!/bin/bash
#Comparación de cadenas con if y else
echo 'Introduzca el usuario:'
read usuario
if [ $usuario == "admin" ]
then
  echo "Bienvenido"
else
  echo "Usuario incorrecto"
fi

----------------------

#!/bin/bash
#Comparación de cadenas con if y else
echo 'User:'
read user
echo 'Password:'
read pass
if [ $user == "admin" ] && [ $pass == 123456 ]
then
  echo "Welcome"
else
  echo "User or pass incorrect"
fi

----------------------

#!/bin/bash
# Uso de or
#Comparación de cadenas con if y else
echo 'User:'
read user
if [ $user == "admin" ] || [ $user == "admin1" ]
then
  echo "Welcome"
else
  echo "User or pass incorrect"
fi

----------------------

#!/bin/sh
#Pedir la edad para probar las comparaciones
echo "Please enter your age:"
read AGE
if [ "$AGE" -lt 20 ] || [ "$AGE" -ge 50 ]; then
  echo "Sorry, you are out of the age range."
elif [ "$AGE" -ge 20 ] && [ "$AGE" -lt 30 ]; then
  echo "You are in your 20s"
elif [ "$AGE" -ge 30 ] && [ "$AGE" -lt 40 ]; then
  echo "You are in your 30s"
elif [ "$AGE" -ge 40 ] && [ "$AGE" -lt 50 ]; then
  echo "You are in your 40s"
fi

#################
##### Cases #####
#################

#!/bin/sh
#Pide un número y revisa si existe el caso
echo "Enter a number between 1 and 10. "
read NUM
case $NUM in
  1) echo "one" ;;
  2) echo "two" ;;
  3) echo "three" ;;
  4) echo "four" ;;
  5) echo "five" ;;
  6) echo "six" ;;
  7) echo "seven" ;;
  8) echo "eight" ;;
  9) echo "nine" ;;
  10) echo "ten" ;;
  *) echo "INVALID NUMBER!" ;;
esac

------------------------

#!/bin/sh
#Probando elección de los usuarios
echo "¿Desea realizar una suma o una resta?"
echo "1 = Suma"
echo -e "2 = Resta"
echo "Introduzca su opción:"
read var

case $var in
  1) echo "Sumando" ;;
  2) echo "Restando" ;;
  *) echo "INVALID NUMBER!" ;;
esac

#!/bin/sh
#Probando elección de los usuarios, y usando operaciones aritmeticas
echo "¿Desea realizar una suma o una resta?"
echo "1 = Suma"
echo "2 = Resta"
echo "3 = Multiplicación"
echo "4 = Division"
echo "Introduzca su opción:"
read var

case $var in
  1)
    num1=10
    num2=5
    suma=$((num1+num2))
    echo $suma
    ;;
  2)
    num1=10
    num2=5
    resta=$((num1-num2))
    echo $resta
    ;;
  3)
    num1=10
    num2=5
    multiplicacion=$((num1*num2))
    echo $multiplicacion
    ;;
  4)
    num1=10
    num2=5
    division=$((num1/num2))
    echo $division
    ;;
  *)
    echo "INVALID NUMBER!"
    ;;
esac

##########################
##### Otros ejemplos #####
##########################

#A Simple Bash Example
#!/bin/bash  
echo "This is a shell script"  
ls -lah
echo "I am done running ls"  
SOMEVAR='text stuff'
echo "$SOMEVAR"

----------------------

#Ejemplo de programa en bash para ejecutar aplicaciones instaladas en el SO.
#!/bin/bash
#val=10
val='##### Abriendo Meld #####'
echo $val
/usr/bin/meld

----------------------

#Ejemplo de programa en bash que crea un fichero en el directorio en que se ejecuta.
#!/bin/bash
touch FFF.txt

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

----------------------

#Abrir un fichero específico con el editor gedit
#!/bin/bash
gedit /home/user/try.txt
----------------------

#!/bin/bash
#Cambiar la fecha y/u hora manualmente
echo -e '\n#####################################################'
echo '# Script para cambiar la fecha y/u hora manualmente #'
echo -e '#####################################################\n'
echo "1 = Fecha"
echo "2 = Hora"
echo -e "\nIntroduzca su opción:"
read var

case $var in
  1)
    #Pedir datos al usuario para cambiar la fecha manualmente
    echo 'Introduzca el día con doble dígito:'
    read dia
    echo 'Introduzca el mes con doble dígito:'
    read mes
    echo 'Introduzca el anio con 4 dígitos:'
    read anio
    #echo -e "La fecha y hora es:"
    sudo date --set $anio-$mes-$dia
    echo -e "\n¡Listo!\n"
    ;;
  2)
    #Pedir datos al usuario para cambiar la hora manualmente
    echo 'Introduzca la hora con doble dígito:'
    read hora
    echo 'Introduzca el minuto con doble dígito:'
    read minuto
    #echo -e "La fecha y hora es:"
    sudo date --set $hora:$minuto:00
    echo -e "\n¡Listo!\n"
    ;;
  *)
    echo "¡Opción inválida!"
    ;;
esac

-----

#!/bin/bash
<<COMMENT1
Script para descargar un archivo del servidor remoto con wget
en una ruta específicada, además pide el último octeto de la ip y
descomprime el archvivo descargado.
COMMENT1

#Pedir el último octeto de la ip
echo 'Último octeto de 192.168.0.?:'
read oct

# Navegar hasta la ruta donde se va a descargar el fichero.
cd /home/user/tmp/

# Descargar con wget el fichero.
wget -c 192.168.0.$oct/share/x.zip

# Descomprimir el archivo descarcago en la ruta especificada.
unzip /home/aosorio/tmp/x.zip

# Imprimir por pantalla que finalizó la descarga
echo -e '\n¡Descarga finalizada, el fichero fue descomprimido!\n'

-----

#!/bin/bash
# Ejemplo de como colorear los prints en bash.
# List colors
# No Color | 0m
# Black | 0;30
# Dark Gray | 1;30
# Red | 0;31
# Light Red | 1;31
# Green |0;32
# Light Green | 1;32
# Brown/Orange | 0;33
# Yellow | 1;33
# Blue | 0;34
# Light Blue | 1;34
# Purple | 0;35
# Light Purple | 1;35
# Cyan | 0;36
# Light Cyan | 1;36
# Light Gray | 0;37
# White | 1;37
NOCOLOR='\033[0m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
echo 'my text solo'
printf "${YELLOW}xxxx \n"
printf "${BLUE}yyyy \n"
printf "${RED}zzzz \n${NOCOLOR}"
printf "my text solo \n"