### Guía Python by dM ###

#Comentarios de línea en Python

""" Comentarios de 
Múltiple Línea """

''' Comentarios de 
Múltiple Línea '''

# CTRL + L //Limpiar Pantalla
# CTRL + SHIFT + L //Limpiar Pantalla

# exit() //Para salir de la consola de Python

# import os // Librería del clear, se coloca al principio del .py
# os.system('clear') //Nos permite limpiar la consola en Python

#Para ejecutar un archivo.py hay que situarse en la carpeta donde esta ubicado el archivo y ejecutar en Terminal: python nombredelarchivo.py

#Python distingue mayúsculas de minúsculas, Hola es un identificador y hola es otro identificador

#Se usa el punto decimal (.) en lugar de coma (,) para representar valores no enteros, es la notación que utiliza Python

'''Palabras Reservadas en Python:

and        del       from     not      while
as         elif      global   or       with
assert     else      if       pass     yield
break      except    import   print
class      exec      in       raise
continue   finally   is       return
def        for       lambda   try

'''

#Expresiones booleanas de comparación en Python

'''Expresión  ---  Significado

   a == b          a es igual a b

   a != b          a es distinto de b

   a < b           a es menor que b

   a <= b          a es menor o igual que b

   a > b           a es mayor que b

   a >= b          a es mayor o igual que b

Ejemplos:

6==6
True

6!=6
False

6>6
False

6>=6
True

6>4
True

6<4
False

6<=4
False

4<6
True

'''

**********OPERADORES LÓGICOS**********

'''Expresión --- Significado

a and b   --- El resultado es True solamente si a es True y b es True de lo contrario el resultado es False
a or b    --- El resultado es True si a es True o b es True de lo contrario el resultado es False
not a     --- El resultado es True si a es False de lo contrario el resultado es False

Ejemplos:
>>> 5>2 and 5>3
True
>>> 5>2 and 5>6
False

>>> 5>2 or 5>3
True
>>> 5>2 or 5>6
True
>>> 5>8 or 5>6
False

>>> 5>8
False
>>> not (5>8)
True
>>> 5>2
True
>>> not (5>2)
False
'''

**********OPERCIONES MATEMÁTICAS**********

#Python permite utilizar las operaciones  +  -  *  /  (división entera) y ** (potenciación)

5*7
35

2+3*7
23

(2+3)*7
35

10/5
2

5**2
25

a = 26
b = 11.3
c = 5
d = 3.5

#SUMA
print a + b
37.3

#RESTA
print c - a
-21

#MULTIPLICACION
print d * c
17.5

#EXPONENTE
print c ** 2
25

#DIVISION
#El resultado sera un entero
#Asi los datos tengan decimales y el resultado real tenga decimales Ejemplo: 0.1923
#Toma unicamente la parte izquerda del punto decimal 
print c / a
0

#DIVISION
#Convierte lo que esta en parentesis a flotante o real
print float(c) / a
0.192307692308

#DIVISION ENTERA 
print 7 / 2
3

#MODULO
print 7%3

**********VARIABLES**********

a = 2 #Declaramos (a) y le asignamos un valor (INT) entero

a = 2L #La (L) al final significa que sera variable de tipo LONG, numeros muy grandes que ocupan mas memoria del sistema

a = "casa" ##Declaramos (a) y le asignamos una cadena de caracteres

print a #Imprime el valor de (a)
a #Imprime el valor de (a) directamente, si esta cargada 

**********print**********

#Imprimer por pantalla el contenido entre las comillas simples o dobles: ('') o ("")

print 'Troya es madre de todos, peleen por ella' # Comillas Simples
Troya es madre de todos, peleen por ella

print 'La ciencia exacta no es una ciencia exacta' # Comillas Simples
La ciencia exacta no es una ciencia exacta

print "Anote su metodo Mr Borden, describalo por completo" # Comillas Dobles
Anote su metodo Mr Borden, describalo por completo

print "Hola como estan" # Comillas Dobles
Hola como estan

print "Hola \ncomo estan" # \n Permite hacer un salto de linea dentro de la cadena
Hola
como estan

print "Hola \t como estan" # \t Permite hacer una tabulacion
Hola 	 como estan

print "Hola \n\tcomo estan" # \n\t Salto de Linea y tabulacion al mismo tiempo
Hola 
	como estan

print""" 
Linea 1
Linea 2
Linea 3
Linea 4
"""
#Imprime el texto entre las triples comillas respetando saltos de linea y tabulaciones 

Linea 1
Linea 2
Linea 3
Linea 4


**********FUNCIÓN**********

def funcion(): #Declaramos el nombre de la Función
	print "Esto es una funcion" #Contenido de la Función
	print "Rictusempra y Sectusempra" #Contenido de la Función

funcion() #Invocación de la Función

**********FUNCIÓN con parámetros**********

#---Función con un parámetro:
def funcion(alguien): #Podemos pasar un parametro a la función
	print "Hola",alguien,"!" 
funcion("Argenis") #Llamamos la función y le pasamos una cadena como parámetro 

#---Función con mas de un parámetro:
def funcion(nombre,apellido):
	print "Hola",nombre,apellido,"!" 
funcion("Argenis","Osorio")

#---Función de suma con declaración de variables:
def prueba(): 
	num = 1
	num2 = 2 
	suma = num+num2
	print"La suma es",suma
prueba()

#---tro Ejemplo:
def prueba(): 
	num = 10
	print num * 3 #El resultado es 30
prueba()

#---otro Ejemplo:
def prueba(): 
	x = [1, 2, 3, 4]
	print x #Imprime: [1, 2, 3, 4]
prueba()
    
#---Ejemplo de Función Matemática:
def cuadrado(num): #Calcula el cuadrado de un número dado
	print num*num

cuadrado(5) #Para invocarala y darle el valor a calcular (5 por ejemplo)

#---Otro ejemplo de Función Matemática:
def cuadrado2(): #Creamos una nueva función
	n = input("Ingrese un número: ") #Pedira al usuario que introduzca un número
	cuadrado(n) #Pasara el valor introducido a la funcion matematica declarada anteriormente (Cuadrado de un número)

cuadrado2() #Ejecutara la función, nos pedira un numero, realizara los calculos y mostrara el resultado 

#---EJEMPLO de Función y Cálculo

# input : Devuelve el valor ingresado por teclado tal como se lo digita (en particular sirve para ingresar valores numéricos)

# raw_input : Devuelve lo ingresado por teclado como si fuera un texto.

#Este programa convierte millas, pies , pulgadas y kilometros a metros
def main():       
	print "Este programa convierte millas, pies, pulgadas y kilometros a metros"
	millas = input("Cuantas millas?: ")
	pies = input("Cuantos pies?: ")
	pulgadas = input("Cuantas pulgadas?: ")
	km = input("Cuantas kilometros?: ")
        metros = 1609.344 * millas
	metros2 = 0.3048 * pies
	metros3 = 0.0254 * pulgadas 
	metros4 = 1000 * km	
	print millas, "millas son:",metros,"metros"
	print pies, "pies son:",metros2,"metros"
	print pulgadas, "pulgadas son:",metros3,"metros"
	print km, "kilometros son:",metros4,"metros"
main()

#Llevar horas a minutos y segundos
def funcion ():
	print "Llevar horas a minutos y segundos"
	horas = input("Cantidad de horas: ")	
	minutos = 60 * horas 
	segundos = 3600 * horas 
	print horas, "horas " "son", minutos, "minutos"
	print horas, "horas " "son", segundos, "Segundos"
funcion()

**********CONCATENACIÓN**********

print "Un divertido "+"programa "+"de "+ "radio"
Un divertido programa de radio

#Multiplicando cadenas
print 3 * "programas "
programas programas programas 

#Ejemplo
def prueba(): 
	nombre="Christopher"
	print nombre+" Robinson" #Imprime: Christopher Robinson
	print nombre * 3 #Imprime: #Imprime: ChristopherChristopherChristopher
prueba()

#Otro Ejemplo
def prueba(): 
	nom = raw_input ("Ingrese un Nombre: ") #Nos pedirá un Nombre
	ape = raw_input ("Ingrese un apellido: ") #Nos pedirá un Apellido

	print "El nombre completo es",nom,ape,"!" #Imprime: El nombre completo es Argenis Osorio !
	print "El nombre completo es",nom+ape,"!" #Imprime: El nombre completo es ArgenisOsorio !
prueba()

**********FOR**********

def prueba(): 
	n1 = 0	
	n2 = 10
	for x in range(n1, n2):
		print x #Imprime números del 0 hasta el 1 usando el cilco repetitivo 
		#print x+x
prueba()

#---Secuencia a mano
def prueba(): 
	for x in [1, 3, 9, 27]:
		print x #Imprimirá los los números 1, 3, 9 y 27
prueba()

**********IF**********

#Introducir la nota, el programa calcula si APROBO o SUSPENDIO XD
nota = input ("Escriba la nota: ")

if nota == 1:
	print "*****Cambiese de carrera*****"
if nota < 10:
	print "*****SUPENDIO! bruto*****"
if nota == 10:
	print "*****APROBO! DE LECHE*****"
if nota > 10:
	print "*****APROBO! parece que chuleteandose*****"
if nota == 20:
	print "*****NO INVENTE! que usted nunca ha sacado 20*****"

**********IF ELSE**********

usuario = raw_input ("USUARIO: ")
if usuario == "canaima":
	print "*****ACCESO CONCEDIDO*****"
else:
	print "*****ACCESO DENEGADO*****"

#---Con números
password = input ("CONTRASENA: ")

if password == 19592165:
	print "*****ACCESO CONCEDIDO*****"
else:
	print "*****USUARIO DENEGADO*****"

#---Con (not) negacion
x = input("Ingrese un numero: ")
if x > 0:
	print "Numero positivo"
if not (x > 0):
	print "Numero no positivo"

**********ELIF**********

x = input("Ingrese un numero: ")
if x > 0:
	print "Numero positivo"
elif x == 0:
	print "Igual a 0"
else:
	print "Numero negativo"

#---Con (for) 
i = input("Cuantos numeros quiere procesar?: ")
for j in range(0,i):
	x = input("Ingrese un numero: ")
	if x > 0:
	     	print "Numero positivo"
	elif x == 0:
	     	print "Igual a 0"
	else:
		print "Numero negativo"

**********WHILE**********

numero = input("Escriba un numero negativo: ")
while numero > 0:
    print "Ha escrito un numero positivo! Intentelo de nuevo"
    numero = input("Escriba un numero negativo: ")
print "Gracias por su colaboracion"

#---Otro Ejemplo
Datos = "Si"
while Datos == "Si":
	x = input("Ingrese un numero: ")
	if x > 0:
		print "Numero positivo"
	elif x == 0:
		print "Igual a 0"
	else:
		print "Numero negativo"
	Datos = input("Quiere seguir? S o N: ")

#---Ciclo con Centinela
#Uso de un valor distinguido Ejemplo (*) si se lee, le indica al programa que el usuario desea salir del ciclo
x = input ("Ingrese un numero ("*" para terminar): ")
while x <> "*":
        if x > 0:
            print "Numero positivo"
        elif x == 0:
            print "Igual a 0"
        else:
            print "Numero negativo"	
	x = input ("Ingrese un numero ("*" para terminar): ")

#---Usando break para salir del ciclo
while True:
	x = input("Ingrese un numero '*' para terminar: ")
        if x == '*':
        	break
        elif x > 0:
        	print "Numero positivo"
        elif x == 0:
        	print "Igual a 0"
        else:
		print "Numero negativo"

**********LISTAS**********		

#lista = [2,"tres",True,["uno",10]] #Cada elemento de la lista contiene un indice, desde el 0,1,2...

#print lista

#********************

#acceder = lista [0]
#acceder = lista [1]
#acceder = lista [2] Accede al elemento en la posicion 2 de mi lista

#print acceder

#********************

#acceder = lista [3][0] accedo al tercer elemento y dentro del tercero accedo al elemento 0 de la sublista

#print acceder

#********************

#lista [1] = 4 cambiar el valor del elemento en la posicion 1 por un entero
#lista [1] = "casa" cambiar el valor del elemento en la posicion 1 por una cadena

#print lista

#********************

#lista = ["casa","carro","perro","gato","ventana","puerta"] Nueva lista

#lista2 = lista[0:3] Imprmir elementos desde la lista desde el 0 hasta la posicion 3

#print lista2

#********************

#lista = ["casa","carro","perro","gato","ventana","puerta"] 

#lista[0:1] = 5,6 Sustituir valores en las posiciones

#print lista


**********VARIABLE GLOBAL**********	

a = 5

def function():
	global a
	a = 42
	print a

def function2():
	print myglobal


print a
function()
#function2()


