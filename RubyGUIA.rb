#### Guía Ruby by dM ####

#Instalación en Debian:
 aptitude install ruby 

#Abrir consola de ruby: abrimos un terminal y escribimos:
 irb # Interactive Ruby Shell

Ctrl + D # Salir de la Consola

ruby -v # Para saber mi version de Ruby

**********Creando un archivo**********

#Los archivos o los programas de ruby se guardan con la 
#extencion (.rb)

#Crear un archivo ejemplo.rb y dentro escribimos:

print "Hola Ruby"
puts "Hola Ruby 2"
(gets)

#Guardamos como ejemplo.rb y para ejecutarlo hacemos un:

ruby ejemplo.rb #Se debe estar en el directorio del archivo o en su defecto
#le pasamos la ruta del archivo--> ruby /home/user/ejemplo.rb

**********Comentarios en ruby********* 

# Comentario de una línea

=begin
	Comentario de 
	varias lineas
=end

**********VARIABLES**********

#Se pueden declarar variables sin especificar el tipo de dato que va a almacenar, similar a Python

mi_num = 25

mi_booleano = true

mi_booleano = false

mi_string = "Ruby"

**********Operaciones básicas**********

#Ruby permite hacer operaciones aritmeticas

2 + 2

2 - 2

2 * 2

2 / 2

2 ** 2

**********Imprimir por pantalla**********

puts "¿Qué gusto tiene la sal?" #Agrega una linea en blanco al final, como un fin de linea

print "Salado" #Imprime el texto normalmente, sin fin de linea como  con puts

**********Usando métodos**********

"Argenis Osorio".length #Nos sirve para contar la cantidad de caracteres de una cadena, como el metodo de JavaScript
#14

"Argenis Osorio".reverse #Nos mostrara el reverso de la cadena que escribimos
#"oirosO sinegrA" 

puts "Argenis Osorio".upcase #Nos mostrara la cadena que escribimos en mayusculas
#"ARGENIS OSORIO"

puts "Argenis Osorio".downcase #Nos mostrara la cadena que escribimos en minusculas
#"argenis osorio""

nombre = "Argenis".downcase.reverse.upcase #Usamos 3 metodos en en una sola linea de codigo
# Convertimos la cadena a minusculas, luego la volteamos y hacemos que se transforme en mayusculas
#"SINEGRA"

**********Capturando datos**********

# (gets) es el método de Ruby que obtiene datos de parte de los usuarios. 
# Cuando se obtienen datos, Ruby agrega automáticamente una línea en blanco (o línea nueva) después de esos datos; 
# chomp elimina esa línea adicional.

print "¿Cuál es tu nombre?" #Pedimos por pantalla al usuario que introduzca un dato
nombre = gets.chomp #Almacenamos el dato en una variable (nombre)

----------

print "¿Cuál es tu Nombre?" 
nombre = gets.chomp

print "¿Cuál es tu Apellido?" 
apellido = gets.chomp

print "¿Cuál es tu Ciudad?"
ciudad = gets.chomp


**********Mostrando el valor de una variable**********

nombre = "Argenis" #Declaramos una variable y le asignamos una cadena
puts "#{nombre}!" #Imprimimos el valor de la variable declarada y cargada
puts "¡Tu nombre es #{nombre}!" #Imprimimos una cadena y a su vez el valor de la variable cargada

********** if **********

if num_usuario < 0
	puts "¡Elegiste un entero negativo!"
elsif num_usuario > 0
	puts "¡Elegiste un entero positivo!"
else
	puts "¡Elegiste cero!"
end

print "Entero, por favor: "
num_usuario = Integer(gets.chomp)

if num_usuario < 0
  puts "¡Elegiste un entero negativo!"
elsif num_usuario > 0
  puts "¡Elegiste un entero positivo!"
else
  puts "¡Elegiste cero!"
end






*****************************
*****************************
*****************************
*****************************
*****************************
*****************************
*****************************
*****************************
