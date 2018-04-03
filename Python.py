### Guía Python by dM ###

#########################
##### Zen of Python #####
#########################

>>> import this
The Zen of Python, by Tim Peters

"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

####################################
##### Estándares de Desarrollo #####
####################################

Los estándares de desarrollo constituyen las normas o patrones de referencia que se deben implementar en el desarrollo de
aplicaciones de software. Entre los estándares de desarrollo más comunes se encuentran: normas de codificación, normas y
esquemas de seguridad, estándares de interfaz u/s, entre otros.

##### Normas de Codificación #####

Para el desarrollo de un sistema se pueden implementar algunos estándares básicos para su codificación, los cuales contemplan lo
establecido en la PEP-8 --> https://www.python.org/dev/peps/pep-0008/

Algunos puntos importantes que encontramos en el PEP8 son los siguientes:

-Use sangría de 4 espacios, sin tabulaciones.

-Las líneas no deberían sobrepasar los 79 caracteres.

-Use líneas en blanco para separar funciones y clases, también para grandes bloques de código dentro de funciones.

-Cuando sea posible, coloque los comentarios aparte del código de tal manera que en esa línea sólo haya comentarios.

-Use cadenas de documentación (docstrings)

-Use espacios a los lados de los operadores y después de comas, pero no directamente dentro de constructos
con paréntesis. Ej: a = f(1, 2) + g(3, 4)

-Nombre sus clases y funciones de forma consistente, como convención se utiliza CamelCase para las clases y
minúsculas_con_guion_bajo para funciones y métodos. Siempre utilice self como el nombre para el primer argumento de un método.

-No use codificaciones de caracteres lujosas si su código pretende ser utilizado en el ámbito internacional.
Se prefiere que utilicen UTF-8. Tomar en cuenta el PEP-0263 colocando la directiva para codificación
UTF-8 (# -*- coding: utf-8 -*-) a los archivos .py

##### Estándares para la documentación del código fuente #####

-La utilización de docstrings permite generar automáticamente documentación, como alternativas a utilizar para generar la
documentación del proyecto tenemos doxygen o Sphinx.

Cabecera para los scripts de Python, indica al compilador o editor que se trata de un fichero python
La segunda linea da codificación UTF-8 al programa:

#!/usr/bin/env python
# -*- coding: utf-8 -*-

A veces solo es necesario usar la segunda línea:

# -*- coding: utf-8 -*-

---

# Comentarios de línea en Python

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

##### Palabras Reservadas en Python #####

and        del       from     not      while
as         elif      global   or       with
assert     else      if       pass     yield
break      except    import   print
class      exec      in       raise
continue   finally   is       return
def        for       lambda   try


##### Expresiones booleanas de comparación en Python #####

Expresión  ---  Significado

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

##############################
##### OPERADORES LÓGICOS #####
##############################

Expresión --- Significado

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

##################################
##### OPERCIONES MATEMÁTICAS #####
##################################

# Python permite utilizar las operaciones  +  -  *  /  (división entera) y ** (potenciación)

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

# SUMA
print a + b
37.3

# RESTA
print c - a
-21

# MULTIPLICACION
print d * c
17.5

# EXPONENTE
print c ** 2
25

# DIVISION
#El resultado sera un entero
#Asi los datos tengan decimales y el resultado real tenga decimales Ejemplo: 0.1923
#Toma unicamente la parte izquerda del punto decimal 
print c / a
0

# DIVISION
#Convierte lo que esta en parentesis a flotante o real
print float(c) / a
0.192307692308

# DIVISION ENTERA 
print 7 / 2
3

# MODULO
print 7%3

# += Suma un valor al valor de la variable y asigna el nuevo valor producto de la suma a la variable
x = 3
x += 2
print x
5

# -= Resta un valor al valor de la variable y asigna el nuevo valor producto de la resta a la variable
x = 10
x -= 2
print x
8

# *= Multiplica un valor por el valor de la variable y asigna el nuevo valor producto de la multiplicación a la variable
x = 10
print x
x *= 2
print x

# /= Divide un valor entre el valor de la variable y asigna el nuevo valor producto de la multiplicación a la variable
x = 10
print x
x /= 2
print x

######################
##### VARIABLES ######
######################

a = 2 #Declaramos (a) y le asignamos un valor (INT) entero

a = 2L #La (L) al final significa que sera variable de tipo LONG, numeros muy grandes que ocupan mas memoria del sistema

a = "casa" ##Declaramos (a) y le asignamos una cadena de caracteres

print a #Imprime el valor de (a)
a #Imprime el valor de (a) directamente, si esta cargada 

#################
##### print #####
#################

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
Hola      como estan

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

###################
##### Función #####
###################

def funcion(): #Declaramos el nombre de la Función
    print "Esto es una funcion" #Contenido de la Función
    print "Rictusempra y Sectusempra" #Contenido de la Función

funcion() #Invocación de la Función

##################################
##### Función con parámetros #####
##################################

#---Función con un parámetro:
def funcion(alguien): #Podemos pasar un parametro a la función
    print "Hola",alguien,"!" 
funcion("Argenis") #Llamamos la función y le pasamos una cadena como parámetro 

#---Función con mas de un parámetro:
def funcion(nombre,apellido):
    print "Hola",nombre,apellido,"!" 
funcion("Argenis","Osorio")

# Simulando que recibe el id y username
def funcion(id,username):
    print "id:",id,"username:",username
funcion(1,"admin")

#---Función de suma con declaración de variables:
def prueba(): 
    num = 1
    num2 = 2 
    suma = num+num2
    print"La suma es",suma
prueba()

#---otro Ejemplo:
def prueba(): 
    num = 10
    print num * 3 #El resultado es 30
prueba()

#---otro Ejemplo:
def prueba(): 
    x = [1, 2, 3, 4]
    print x #Imprime: [1, 2, 3, 4]
prueba()

# Imprimiento un elemento de la lista
def prueba(): 
    x = [1, 2, 3, 4]
    #print x #Imprime: [1, 2, 3, 4]
    print x[2]
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

#Usando las dos funciones
def cuadrado(num): #Calcula el cuadrado de un número dado
    print num*num

def cuadrado2(): #Creamos una nueva función
    n = input("Ingrese un número: ") #Pedira al usuario que introduzca un número
    cuadrado(n) #Pasara el valor introducido a la funcion matematica declarada anteriormente (Cuadrado de un número)

cuadrado2()

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

#########################
##### CONCATENACIÓN #####
#########################

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

###############
##### FOR #####
###############

# -*- coding: utf-8 -*-
def prueba(): 
    n1 = 0    
    n2 = 10
    for x in range(n1, n2):
        print x #Imprime números del 0 hasta el 1 usando el cilco repetitivo
        #print x+x
prueba()

----

#---Secuencia a mano
def prueba(): 
    for x in [1, 3, 9, 27]:
        print x #Imprimirá los los números 1, 3, 9 y 27
prueba()

----

"""
Imprimir un numero x cantidad de veces
"""
# -*- coding: utf-8 -*-
def prueba():
    for i in range(5):
        print("1")
prueba()

----

"""
Imprimir un numero x cantidad de veces
"""
# -*- coding: utf-8 -*-
def prueba(): 
    n1 = 0
    n2 = 9000
    for x in range(n1, n2):
        print x #Imprime números del 0 hasta el 900 usando el cilco repetitivo
        #print x+x
prueba()

##############
##### IF #####
##############

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

###################
##### IF ELSE #####
###################

usuario = raw_input ("USUARIO: ")
if usuario == "canaima":
    print "*****ACCESO CONCEDIDO*****"
else:
    print "*****ACCESO DENEGADO*****"

#---Con números
password = input ("CONTRASENA: ")

if password == 123:
    print "*****ACCESO CONCEDIDO*****"
else:
    print "*****USUARIO DENEGADO*****"

#---Con (not) negacion
x = input("Ingrese un numero: ")
if x > 0:
    print "Numero positivo"
if not (x > 0):
    print "Numero no positivo"

################
##### ELIF #####
################

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

#################
##### WHILE #####
#################

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

##################
##### Listas #####
##################

'''
La lista es un tipo de datos versátil disponible en Python, que puede escribirse
como una lista de valores separados por comas (cosas) entre corchetes.
Lo importante de una lista es que los elementos de una lista
no tienen por qué ser del mismo tipo.
'''

lista = [2,"tres",True,["uno",10]] #Cada elemento de la lista contiene un indice, desde el 0,1,2...
print lista

#********************

#Imprimiendo los elementos de la lista
lista = ["Proyecto1","Proyecto2","Proyecto3",["David","Usain"]]
print lista[0]
print lista[1]
print lista[2]
print lista[3][0]#Accedemos al elemento de la posición tres e imprimimos el subelemento de la posicion 0
print lista[3][1]#Accedemos al elemento de la posición tres e imprimimos el subelemento de la posicion 1

#********************

lista = ["Proyecto1","Proyecto2","Proyecto3",["David","Usain"]]
lista [1] = 4 #cambiar el valor del elemento en la posicion 1 por un entero
lista [1] = "casa" #cambiar el valor del elemento en la posicion 1 por una cadena
print lista

#********************

lista = ["casa","carro","perro","gato","ventana","puerta"] #Nueva lista
lista2 = lista[0:3] #Imprmir elementos desde la lista desde el 0 hasta la posicion 3
print lista2

#********************

lista = ["casa","carro","perro","gato","ventana","puerta"]
lista[0:1] = 5,6 #Sustituir valores en las posiciones
print lista

#********************

#!/usr/bin/env python
# -*- coding: utf-8 -*-
lista = [1,"Dos",3]
buscar = 1
print buscar in lista #Se traduciría como: ¿Buscar esta en la lista?
#Nos devolvería un True porque si está ese valor en la lista

###########################
##### VARIABLE GLOBAL #####
###########################

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

##################
##### Tuplas #####
##################

Una tupla es una secuencia de objetos de Python.
Las tuplas son secuencias, al igual que las listas.
Las diferencias entre tuplas y las listas son, las tuplas
no se pueden actualizar a diferencia de las listas y las
tuplas utilizan paréntesis, mientras que las listas utilizan corchetes.

# Imprimiendo el contenido de una tupla
tupla = (1,True,"hola")
print tupla

# Imprimiendo el contenido de una tupla, posición a posición.
tupla = (1,True,"hola")
print tupla[0]
print tupla[1]
print tupla[2]

########################
##### Diccionarios #####
########################

Los diccionarios en Python son un tipo de estructuras de datos que permite guardar un conjunto
no ordenado de pares clave-valor, siendo las claves únicas dentro de un mismo diccionario
(es decir que no pueden existir dos elementos con una misma clave).
Los diccionarios son estructuras de datos muy extendidos en otros lenguajes de programación.

# -*- coding: utf-8 -*-
#Imprimiendo el contenido del diccionario
diccionario = {
    'Clave1':[
        1,2,3
    ],
    'Clave2':True
}
print diccionario

----

# -*- coding: utf-8 -*-
#Imprimiendo el contenido del diccionario, accedemos a los valores a través de la clave
diccionario = {
    'Clave1':[
        1,2,3
    ],
    'Clave2':True
}
print diccionario['Clave1']
print diccionario['Clave2']

----

# -*- coding: utf-8 -*-
#Imprimiendo el contenido del diccionario, accedemos a los valores a través de la clave que puede
#cualquier tipo de dato, una cadena, un entero, etc, pero no listas ni diccionarios
diccionario = {
    'Clave1':[
        1,2,3
    ],
    'Clave2':True,
    4:"numero"
}
print diccionario['Clave1']
print diccionario['Clave2']
print diccionario[4]

----

# -*- coding: utf-8 -*-
# Imprimir datos de un diccionario por posición
data = {
    "usuarios": [
        {
            "username":"admin",
            "password":123456
        },
        {
            "username":"admin1",
            "password":12345678
        },
    ]
}
print data["usuarios"]
print data["usuarios"][0]["username"]
print data["usuarios"][0]["password"]
print data["usuarios"][1]["username"]
print data["usuarios"][1]["password"]

----

# -*- coding: utf-8 -*-
# Imprimir datos de un diccionario por posición
data = {
  "Fruteria":[
    {
      "Fruta":[
        {
          "Nombre":"Manzana","Cantidad":10
          },
          {
            "Nombre":"Pera","Cantidad":20
          },
          {
            "Nombre":"Naranja","Cantidad":30
          }
      ]
    },
    {
      "Verdura":[
        {
          "Nombre":"Lechuga","Cantidad":80
        },
        {
          "Nombre":"Tomate","Cantidad":15
        },
        {
          "Nombre":"Pepino","Cantidad":50
        }
      ]
    }
  ]
}
print data["Fruteria"][0]["Fruta"][0]["Cantidad"]
print data["Fruteria"][0]["Fruta"][1]["Cantidad"]
print data["Fruteria"][0]["Fruta"][2]["Cantidad"]
print "---"
print data["Fruteria"][0]["Fruta"][0]["Nombre"]
print data["Fruteria"][0]["Fruta"][1]["Nombre"]
print data["Fruteria"][0]["Fruta"][2]["Nombre"]
print "---"
print data["Fruteria"][1]["Verdura"][0]["Cantidad"]
print data["Fruteria"][1]["Verdura"][1]["Cantidad"]
print data["Fruteria"][1]["Verdura"][2]["Cantidad"]

##########################
##### Manejando json #####
##########################

JSON es una notación de objetos, utiliza una sintaxis que nos permite crear objetos de
manera rapida y simple, estos objetos pueden ser utilizados de la manera que queramos y la notación se
utiliza muy comúnmente para crear servicios REST, objetos, e incluso fue adoptada por algunas bases de
datos como lo es MongoDB.

Básicamente es un diccionario de python que guarda objetos.

Para escribir JSON debemos tener en cuenta lo siguiente:
La creación de los objetos JSON implica escribir datos, para ello:

-Los objetos JSON estan rodeados por llaves “{}”
-Los datos estan separados por comas.
-Los datos se escriban en pares, siendo primero el nombre o atributo del mismo y luego el valor del dato.
-Llaves cuadradas [] guardan arreglos, incluyendo otros objetos JSON

El formato JSON tiene la siguiente notación:

{key : value, key2 : value2, key3 : value3,...}

Y también puede ser serializado y multidimensional, por ejemplo:

[{key : value, key2 : value2, key3 : value3, key : { key : value, key2 : value2, key3 : value3} },{key : value, key2 : value2, key3 : value3,...}]

Ejemplo de un objeto JSON que guarda un usuario y password:

# -*- coding: utf-8 -*-
# Imprimir datos de un diccionario
data = {"usuarios":[{"username":"admin","password":123456}]}
print data["usuarios"]
print data

----

# -*- coding: utf-8 -*-
# Imprimir datos de un diccionario
import json
data = {"Fruteria":[{"Fruta":[{"Nombre":"Manzana","Cantidad":10},{"Nombre":"Pera","Cantidad":20}]}]}
print data
print "-----"
#Nos devuelve el string con el JSON
data_string = json.dumps(data)
print data_string

---

# -*- coding: utf-8 -*-
# Decodificar JSON
# Para decodificar un JSON a vamos a hacer uso de la función json_loads(String)
import json
data = {"Fruteria":[{"Fruta":[{"Nombre":"Manzana","Cantidad":10},{"Nombre":"Pera","Cantidad":20}]}]}
data_string = json.dumps(data)
print 'ENCODED:', data_string
decoded = json.loads(data_string)
print 'DECODED:', decoded

---

# -*- coding: utf-8 -*-
# Decodificar JSON
# Imprimir valores del json, por posíción
import json
data = {
  "Fruteria":[
    {
      "Fruta":[
        {
          "Nombre":"Manzana","Cantidad":10
          },
          {
            "Nombre":"Pera","Cantidad":20
          },
          {
            "Nombre":"Naranja","Cantidad":30
          }
      ]
    },
    {
      "Verdura":[
        {
          "Nombre":"Lechuga","Cantidad":80
        },
        {
          "Nombre":"Tomate","Cantidad":15
        },
        {
          "Nombre":"Pepino","Cantidad":50
        }
      ]
    }
  ]
}
#encoded
data_string = json.dumps(data)
#Decoded
decoded = json.loads(data_string)
print "Tenemos "+str(decoded["Fruteria"][0]["Fruta"][0]["Cantidad"])+" Manzanas"
print "Tenemos "+str(decoded["Fruteria"][0]["Fruta"][1]["Cantidad"])+" Peras"
print "Tenemos "+str(decoded["Fruteria"][0]["Fruta"][2]["Cantidad"])+" Naranjas"
print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][0]["Cantidad"])+" Lechugas"
print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][1]["Cantidad"])+" Tomates"
print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][2]["Cantidad"])+" Pepino"

---

# -*- coding: utf-8 -*-
# Decodificar JSON
# Imprimir valores del json, por posíción
import json
data = {
  "Fruteria":[
    {
      "Fruta":[
        {
          "Nombre":"Manzana","Cantidad":10
          },
          {
            "Nombre":"Pera","Cantidad":20
          },
          {
            "Nombre":"Naranja","Cantidad":30
          }
      ]
    },
    {
      "Verdura":[
        {
          "Nombre":"Lechuga","Cantidad":80
        },
        {
          "Nombre":"Tomate","Cantidad":15
        },
        {
          "Nombre":"Pepino","Cantidad":50
        }
      ]
    }
  ]
}
# Mostrando la data completa
print "*****Data total*****"
print data

# Mostrando la data del primer hijo
print "*****Data Frutas*****"
print data['Fruteria'][0]

# Mostrando la data del segundo hijo
print "*****Data Verduras*****"
print data['Fruteria'][1]

---

# -*- coding: utf-8 -*-
# Decodificar JSON
# Imprimir valores del json, por posíción, accediendo al último nivel
import json
data = {
  "Fruteria":[
    {
      "Fruta":[
        {
          "Nombre":"Manzana","Cantidad":10
          },
          {
            "Nombre":"Pera","Cantidad":20
          },
          {
            "Nombre":"Naranja","Cantidad":30
          }
      ]
    },
    {
      "Verdura":[
        {
          "Nombre":"Lechuga","Cantidad":80
        },
        {
          "Nombre":"Tomate","Cantidad":15
        },
        {
          "Nombre":"Pepino","Cantidad":50
        }
      ]
    }
  ]
}
# Mostrando la data completa
print "*****Data total*****"
print data

# Mostrando la data del primer hijo
print "*****Data Frutas*****"
print data['Fruteria'][0]

# Mostrando la data del segundo hijo
print "*****Data Verduras*****"
print data['Fruteria'][1]

# Mostrando la data de los elementos de Frutas
print "*****Data de elementos de Frutas *****"
print data['Fruteria'][0]["Fruta"][0]["Nombre"]
print data['Fruteria'][0]["Fruta"][0]["Cantidad"]
print data['Fruteria'][0]["Fruta"][1]["Nombre"]
print data['Fruteria'][0]["Fruta"][1]["Cantidad"]
print data['Fruteria'][0]["Fruta"][2]["Nombre"]
print data['Fruteria'][0]["Fruta"][2]["Cantidad"]

# Mostrando la data de los elementos de Verduras
print "*****Data de elementos de Verduras *****"
print data['Fruteria'][1]["Verdura"][0]["Nombre"]
print data['Fruteria'][1]["Verdura"][0]["Cantidad"]
print data['Fruteria'][1]["Verdura"][1]["Nombre"]
print data['Fruteria'][1]["Verdura"][1]["Cantidad"]
print data['Fruteria'][1]["Verdura"][2]["Nombre"]
print data['Fruteria'][1]["Verdura"][2]["Cantidad"]

##################
##### Clases #####
##################

En la vida cotidiana, conocemos los objetos, como una carro, una botella, una perdona, etc.
Esos objetos poseen ciertas caracteristicas, esas características, en programación orientada a objetos
las llamámos atributos del objeto, y a las acciones que puede realizar el objeto se conocen como métodos.
Podriamos crear un objeto llamado Humano, y sus atributos serian, la edad, estatura, nombre, cedula, nacionalidad
Y sus métodos serían, caminar, correr, levantarse, etc.
Una clase es una plantilla del cual proviene nuestro objeto, en ella establecemos los atributos y métodos que tendra un objeto.

¿Que es self?
Self es simplemente el nombre convencional para el primer argumento de un método en Python.
Por ejemplo, un método definido de la forma meth(self, a, b, c) debe ser llamado
con x.meth(a, b, c), por alguna instancia de la clase x, en la cual ocurre la definición;
de esta forma el método llamado pensara que es llamado como meth(x, a, b, c)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Definimos una clase, por convención se usa la primera letra en mayúscula
class Humano:
    def __init__(self): #Definimos un método, es una función pero cuando está dentro de una clase es un método, éste método init python lo reconoce, cuando se cree un nuevo objeto, automáticamente se va a ejecutar este método. En la variable self se va a guardar la referencia al objeto que estemos creando
        print "Soy un nuevo objeto"

pedro = Humano() #Creamos un objeto que tiene como plantilla la clase Humano

#********************
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Definimos una clase, por convención se usa la primera letra en mayúscula
class Humano:
    def __init__(self): #Definimos un método, es una función pero cuando está dentro de una clase es un método, éste método init python lo reconoce, cuando se cree un nuevo objeto, automáticamente se va a ejecutar este método. En la variable self se va a guardar la referencia al objeto que estemos creando
        print "Soy un nuevo objeto"

    def hablar(self,mensaje):
        print mensaje

pedro = Humano() #Creamos el objeto
raul = Humano() #Creamos el objeto
pedro.hablar('Hola') #Le pasamos valores por parametro que recibirá el método
raul.hablar('Hola, Pedro') #Le pasamos valores por parametro que recibirá el método

#********************
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self):
        self.edad = 25 #Agregamos un atributo, cada objeto que cree a partir de esta clase, tendra ese atributo
        print "Soy un nuevo objeto"

    def hablar(self,mensaje):
        print mensaje

pedro = Humano() #Creamos el objeto
print "Soy Pedro y tengo", pedro.edad

#********************
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):#Agregamos la variable edad
        self.edad = edad #Tenemos el atributo edad y le asignamos la variable edad que recibiremos como argumento del método

    def hablar(self,mensaje):
        print mensaje

pedro = Humano(26) #Enviamos por parámetro el valor que será recibido por el método, ya que está declarado el argumento edad junto a self
raul = Humano(21) #Enviamos por parámetro el valor que será recibido por el método, ya que está declarado el argumento edad junto a self
print "Soy Pedro y tengo", pedro.edad
print "Soy Raul y tengo", raul.edad

####################
##### Herencia #####
####################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print self.edad
        print mensaje

class IngSistemas(Humano): #Subclase que hereda de la Superclase, la subclase heredara todos los atributos y métodos de la Superclase
    def programar(self,lenguaje):
        print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'Debo estudiar el caso de ', de

pedro = IngSistemas(26) #Objeto creado con la clase IngSistemas pero usa el método de la Superclase Humano
raul = LicDerecho(27) #Objeto creado con la clase IngSistemas pero usa el método de la Superclase Humano
print "Soy Pedro y tengo", pedro.edad
print "Soy Raul y tengo", raul.edad
pedro.hablar('Hola')
raul.hablar('Hola, Pedro')

#Usando el método programar y enviando valores al argumento que necesita
#Usando el método estudiarCaso y enviando valores al argumento que necesita
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print mensaje

class IngSistemas(Humano):
    def programar(self,lenguaje):
        print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'Debo estudiar el caso de ', de

pedro = IngSistemas(26)
raul = LicDerecho(27)
pedro.hablar('Hola')
raul.hablar('Hola, Pedro')
pedro.programar('Python') #Usando el método programar y enviando valores al argumento que necesita
raul.estudiarCaso('Pedro')

#Definimos el método init que sobrescribira al método heredado de Humano, cuando el objeto use el metodo init usará el suyo y no el heredado.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print mensaje

class IngSistemas(Humano):
    def __init__(self): #Definimos el método init que sobrescribira al método heredado de Humano, cuando el objeto use el metodo init usará el suyo y no el heredado
        print 'Hola'

    def programar(self,lenguaje):
        print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'Debo estudiar el caso de ', de

pedro = IngSistemas()
raul = LicDerecho(27)
pedro.hablar('Hola')
raul.hablar('Hola, Pedro')
pedro.programar('Python')
raul.estudiarCaso('Pedro')

#############################
##### Herencia multiple #####
#############################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print mensaje

class IngSistemas(Humano):
    def __init__(self):
        print 'Hola'

    def programar(self,lenguaje):
        print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'Debo estudiar el caso de ', de

class Estudioso(IngSistemas,LicDerecho): #Hereda de dos clases
    pass #Palabra reservada, interpretada como vete! no hay nada que ver aquí. Cuando creamos una clase, forzosamente debe de existir un método y si no existe, usamos pass, en este ejemplo ya está heredando los métodos de otras clases

pepe = Estudioso() #Creamos el objeto
pepe.hablar('Hola, soy de herencia multiple') #Usando el método heredado de Humano, ya que la clase Estudioso hereda de IngSistemas y de LicDerecho, que a su vez heredan de Humano
pepe.programar('C++') #Usando el método programar heredado
pepe.estudiarCaso('Juan') #Usando el estudiarCaso heredado

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Obtener el índice de un elemento de la lista
lista = [1,"Dos",3]
buscar = 1
print lista.index(buscar) #Obtener el índice de un elemento de la lista

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Buscando elementos en una lista
lista = [1,"Dos",3]
buscar = "Dos"
if buscar in lista: #Buscar el eleménto en la lista
    print lista.index(buscar) #Mostrar el índice del elemento
else:
    print "No esta el elemento" #Notificar si el elemento no existe

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Agregando un nuevo elemento a la lista
lista = [1,"Dos",3]
print lista
lista.append("Nuevo elemento") #Agregamos un nuevo elemento a la lista
print lista

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Contar el numero de elementos presentes en una lista
lista = [1,"Dos",3,4,"Cinco",3]
print lista.count(3) #Buscar y contar cuantas veces está un elemento en la lista.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Insertando un nuevo elemento en la lista
lista = [1,"Dos",3,4,"Cinco",3]
print lista
lista.insert(2,"Nuevo") #Insertamos un nuevo elemento en la lista, en este caso insertamos la cadena "Nuevo" en la posición 2, pero no sustituye, solo se inserta, el resto de valores se corren ascendentemente.
print lista

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Juntar dos listas
lista = [1,2,3]
print lista
lista2 = [5,6,7]
lista.extend(lista2) #Método extend, juntar dos listas, podemos agregar una nueva lista al final de primera lista
print lista

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Extraer y eliminar un elemento de la lista
lista = [1,2,3]
print lista
lista.pop() #Elimina el último elemento de la lista si no especificamos un indice que borrar
print lista

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Extraer y eliminar un elemento de la lista, indicando la posición
lista = [1,2,3]
print lista
lista.pop(1) #Eliminamos el elemento que está en la posición 1 de la lista
print lista

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Método reverse, que invierte los elementos de la lista
lista = [1,2,3]
print lista
lista.reverse()
print lista

###################
##### Métodos #####
###################

##### len() #####

# -*- coding: utf-8 -*-
#El método len() devuelve el número de elementos de la lista, una variable, etc.
a = "casa"
print len(a)

# -*- coding: utf-8 -*-
#El método len() devuelve el número de elementos de la lista, una variable, etc.
lista = ["Proyecto1","Proyecto2","Proyecto3"]
print lista
print len(lista)

# -*- coding: utf-8 -*-
#Otro Ejemplo
list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']
print "First list length : ", len(list1)
print "Second list length : ", len(list2)

########################################################
##### Usando APIs con el Modulo Requests de Python #####
########################################################

#Requests es una librería para HTTP

Para este ejemplo aclaremos:

Github y Stackoverflow proporcionan su API para extraer diversos tipos de datos.

La documentación de la API de Github y StackOverflow se puede encontrar aquí.
Github: https://developer.github.com/v3/
StackOverflow: http://api.stackexchange.com/docs 

Pero ¿qué es lo que usamos para comunicarse con estas API?
Trabajar con HTTP es una tarea dolorosa. Python incluye un módulo llamado urllib2 pero trabajar con él puede llegar a ser engorroso.

### Solicitudes HTTP ###

Instalamos el paquete python-requests para hacer solicitudes HTTP

# apt-get install python-requests

Creamos y guardamos el fichero postrequest.py con el siguiente contenido:

#----- begin
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
r = requests.get('https://api.github.com', auth=('username', '123456'))
print r.status_code
print r.headers['content-type']
#----- end

Contiene la llamada a la librería instalada "import requests", creamos una variable "r"
y le asignames una solicitud GET a la api de logeo de github, donde le pasaremos el nombre de usuario y la contraseña, al ejecutarlo
nos dara una respuesta gracias a los print que declaramos, hora de probarlo:

$ python postrequest.py

#Si el usuario o la contraseña no coinciden, o no consigue nungun recurso buscado, acceso, etc, nos dará el siguiente error:

401
application/json; charset=utf-8

#De lo contrario si el usuario y la contraseña coinciden, si encontro el recurso o acceso, nos mostrara un OK:

200
application/json; charset=utf-8

-----

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejemplo pidiendo los datos al usuario.
import requests
username = raw_input("Username: ")
password = raw_input("Password: ")
r = requests.get('https://api.github.com', auth=(username, password))
print r.status_code
print r.headers['content-type']

################################################
##### Imprimir datetime de python y django #####
################################################

$ python
>>> import datetime
>>> now = datetime.datetime.now()
>>> print now
2017-01-05 04:08:15.932157

##################
##### Base64 #####
##################

'''
-- ¿Qué es la codificación Base64?

El Base64 es la manera en que los datos binarios de 8 bits se codifican a un formato que pueda ser representado en 7 bits.
Esto se hace utilizando sólo los caracteres A-Z, a-z, 0-9, +, y / con el fin de representar los datos.
El término base 64 viene del estándar Multipurpose Internet Mail Extensions (MIME), que es ampliamente utilizado para HTTP y XML, y
fue desarrollado originalmente para la codificación de adjuntos de los correos electrónicos y su correcta transmisión. 

-- ¿Por qué utilizamos Base64?

Base64 es muy importante para la representación de datos binarios, tanto que permite que los datos binarios puedan ser
representados de manera que parezcan y actúen como texto sin formato. Esto hace que sea más seguro almacenarlos en bases
de datos, enviarlos a través de correo electrónico o utilizarlos en formatos basados en texto como XML. Base64 se utiliza
básicamente para representar datos en formato ASCII.

-- La codificación Base64

La codificación Base64 es el proceso de convertir los datos binarios, en un juego de caracteres limitado a 64 caracteres.
Como hemos dicho en la primera sección, esos caracteres son A-Z, a-z, 0-9, +, y / (¿Los has contado?, ¿te has dado cuenta
de que se suman 64?). Este conjunto de caracteres se considera el conjunto de caracteres más común, y se conoce como el Base64
de MIME. Utiliza A-Z, a-z, 0-9, +, y / para los primeros 62 valores, y +, y / para los dos últimos valores.

Los datos codificados en Base64 terminan siendo más grandes que los datos originales, de manera que, como hemos dicho antes, por cada 3
bytes de datos binarios, hay al menos 4 bytes de datos codificados en Base64. Esto es debido al hecho de que estás apretando los datos en
un conjunto más pequeño de caracteres. 
'''

# -*- coding: utf-8 -*-
# Codificar con base64 una imágen
with open("path/of/file.*", "rb") as f:
    data = f.read()
    print data.encode("base64")

---

# -*- coding: utf-8 -*-
#Decodificar una cadena en base64 y convertirla en imágen
import base64
image = """
Aqui iría la cadena superlarga
generada con la codificación en base64
"""
imgdata = base64.b64decode(image)
filename = 'fff.png'  #Nombre con el que se va a crear la imágen 
with open(filename, 'wb') as f:
    f.write(imgdata)

----

# -*- coding: utf-8 -*-
# Decodificar y Codificar en un solo script usando base64 en python
import base64
with open("firefox-icon.png", "rb") as f:
    data = f.read()
    data1 = data.encode("base64")
    imgdata = base64.b64decode(data1)
    filename = 'fff.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)


#######################################################
##### Script para copiar un fichero a un servidor #####
#######################################################

# -*- coding: utf-8 -*-
import os
#os.system("scp FILE USER@SERVER:PATH")
os.system("scp ff.jpg user@192.168.x.x:/home/user/tmp")

#################################################
##### Script para usar comandos del sistema #####
#################################################

Básicamente es lo mismo que el comando anterior solo que
permite utilizar comandos de unix.

# -*- coding: utf-8 -*-
import os
os.system("mkdir new_folder")

# Otro ejemplo

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Uso de comandos de unix desde python
"""
import os

p = os.popen('ls -la')
print(p.read())

####################################
##### Crear carpeta con python #####
####################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Uso de comandos de unix desde python
"""
import os

print os.getcwd() # Imprimir el directorio actual
if not os.path.exists("x"):
  os.makedirs("x")

###################################
#### Validar email con python #####
###################################

# -*- coding: utf-8 -*-
"""
Validar email con python
"""
import re
correo='nombre@dominio.com'
if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
    print "Correo correcto"
else:
    print "Correo incorrecto"

##############################################################
##### Importar un ficehero, script, directorio en python #####
##############################################################

import sys
sys.path.append(pathToFolderContainingScripts)
from scriptName import functionName #scriptName without .py extension

################################################################
##### Enlace simbólico a las version de python por defecto #####
################################################################

/usr/bin/python

Si queremos cambiar de version por defecto de python, entonces borramos /usr/bin/python creamos un enlace simbólico /usr/bin/python que apunte a python 3.x

####################################################################################
##### Descarga de archivos desde una url http y almacenarlo en disco en Python #####
####################################################################################

# -*- coding: utf-8 -*-
import urllib
urllib.urlretrieve ("http://192.168.12.82/x.zip", "x.zip")

################################################
########## Ambiente virtual en Python ##########
################################################

Cuando se desarrollando software con Python, quizas se presente el problema de tener
utilizar diferentes versiones de una mismo paquete en diferentes proyectos, ya sea el
mismo Python o diferentes versiones de un Framework como Django por ejemplo, el
problema a solucionar radica en como poder instalar las dos o mas versiones de la
misma librería con el fin de poder desarrollar varios proyectos de forma simultánea.

La solución consiste en crear virtualenvs o entornos virtuales. Un entorno virtual de
Python es un espacio completamente independiente de otros entornos virtuales y de los
paquetes instalados globalmente en el sistema. Esto significa que es posible instalar la versión
2.7 de Python en un entorno virtual y la versión 3.0 en otro diferente o de forma
global sin problema alguno.

El porder tener diferentes entornos donde podemos instalar diferentes versiones de paquetes
nos da la oportunidad de hacer un desarrollo simultaneo así como poder hacer pruebas si
afectar a los paquetes del sistema global.

##### Instalación: #####

Para crear un ambiente virtual instalamos lo siguiente:

# aptitude install python-setuptools python-dev

# aptitude install python-virtualenv virtualenvwrapper

$ mkvirtualenv nombre_ambiente_virtual //  Con un usuario (diferente a root) cree un ambiente virtual para su proyecto.

$ workon nombre_ambiente_virtual // Para acceder al nombre del ambiente virtual creado

ejemplo: 
user@debian:/home$ workon proyecto // Accedemos al entorno virtual creado
(proyecto)user@debian:/home$ // Ya estamos en el entorno virtual creado, denotado por el nombre del entorno al inicio del prompt

$ deactivate nombre_ambiente_virtual // Para salir del entorno virtaul, o simplemente deactivate

$ lsvirtualenv // Para listar los entornos virtuales creados o disponibles.

$ rmvirtualenv nombre_virtualenv // Remover o borrar un entorno virtual.

// Los entornos virtuales se crean en el directorio /home/user/.virtualenvs

##### Tips #####

En Debian GNU/Linux 8 (Jessie) a veces el comando mkvirtualenv no funciona por lo que hacemos lo siguiente:

# apt-get install virtualenvwrapper

$ vim .bashrc // Como usuario normal (NO ROOT), hay que agregar las variables con la ruta para virtualenv en el .bashrc, Agregar el siguiente contenido:

# to virtualenvwrapper
export WORKON_HOME=$HOME/django
source /etc/bash_completion.d/virtualenvwrapper

luego:

$ source .bachrc

##### Usando virtualenv #####

Installation: 

# aptitude install python-virtualenv

-Crear un virtualenv:

$ virtualenv mi_env

-Activar el virtualenv:

$ source mi_env/bin/activate

-Instalar un paquete (p.ej. Django) en el virtualenv:

(mi_env)$ pip install django

-Trabajar en el proyecto.

-Salir del virtualenv:

(mi_env)$ deactivate

##### Usando Python 3 en virtualenvwrapper #####

# aptitude install python3.4 python3-pip python3.4-dev python3-setuptools

# aptitude install python3-virtualenv virtualenvwrapper

$ mkvirtualenv --python=/usr/bin/python3 my_env

$ workon my_env

(my_env)$

##### Usando Python 3 en virtualenv #####

$ virtualenv -p python3 my_env

##### Borrar entorno virtual #####

No hay comando para borrar un entorno virtual desde virtualenv, basta con cancelar o detener los procesos (servidores y servicios) usados por
ese entorno y luego borrar el directorio.

$ rm -rf myenv

########################
##### Paquetes pip #####
########################

// Para desarrollar software con rapidez y calidad, es imprescindible utilizar paquetes externos que ayuden
con parte de la funcionalidad que se desea implementar. En el ambiente Python esto no es la excepción.

// Para solventar ésta necesidad, la comunidad Python ha puesto convenientemente a disposición de los desarrolladores
un repositorio de paquetes de fácil acceso llamado PyPi. Solo es necesario ejecutar un comando en la terminal
para poder instalar el paquete Python que necesitemos. Incluso es posible instalar paquetes que no se encuentren
en el mencionado repositorio.

// Para descargar paquetes del repositorio PyPi se pueden utilizar varias herramientas, pero en este caso se
va a usar pip. Es necesario instalar esta herramienta en el sistema en caso de no estar disponible, antes
de poder instalar un paquete Python.

// El comando pip equivale al apt-get de Debian pero para paquetes Python.

# aptitude install python-pip python-dev python-setuptools python3-pip // Instalamos pip y otros necesarios, com python3 para pip, necesario en algunos proyectos.

// Una vez instalado ya podremos instalar paquetes de Python a traves de pip ejemplo:

$ pip install django // Nos instalara la ultima version de Django disponible en los paquetes pi

$ pip install django==1.7 // Instalar una versión específica de algun paquete.

// Tambien es posible crear ficheros que contengan rutinas para automatizar la instalacion
de varios paquetes ejemplo:

Creamos un requirements.txt y dentro escribimos como ejemplo:
django==1.5.12
pillow==2.4.0
Geraldo==0.4.17

// Luego podemos ejecutar un pip install sobre el fichero e instalará lo que contenga:

$ pip install -r requirements.txt

$ pip install -r requirements.txt --timeout 120 // Con este parametro le daremos mayor tiempo de respuesta al servidor, para conexiones lentas.

// Dentro de los .virtualenvs, dentro de nuestro entorno virtual en
lib/python2.7/site-packages podemos ver que se instalaron los paquetes de requirements.txt
de no ser así hay que revisar el fichero o el nombre de los paquetes a instalar, etc.

$ pip search nombre_paquete // Buscar un paquete.

$ pip uninstall package // Desinstalar un paquete.

$ pip show package // Para ver si un paquete está instalado, si es así, mostrará la version, y la ruta donde está instalado.

$ pip install Package --upgrade // Para actualizar un paquete a su última versión.

$ pip install --upgrade Package package==1.x.x // Actualizar un paquete a una versión específica.

 $ pip freeze // Listar los paquetes instalado y sus versiones exactas.

##### Error: ImportError: No module named packaging.version #####

Puede que alguna vez a pip le pique el trasero y no deje realizar acciones
de búsqueda, actualización etc.. entonces moveremos unos ficheros:

$ cd /usr/local/lib/python2.7/dist-packages

$ mv pkg_resources/ pkg_resources_bak/

Funcionó cuando se instalo en el sistema base, si está en un entorno virtual la
ruta será diferente.

###########################################
##### Usando un espejo de pip cercano #####
###########################################

Para usar los repositorios py.pi internos de Cenditel
vamos al directorio /home/usuario/.pip/
y creamos dentro el fichero pip.conf
Agregamos el siguiente contenido al fichero creado y guardamos:

[global]
index-url = http://pypi.cenditel/simple/

Luego actualizamos el pip y listo, si estamos usando un entorno virtual de python
entonces ejecutaremos los comandos dentro del entorno virtual.

$ pip install --upgrade pip
$ pip install package_name --trusted-host pypi.cenditel
$ pip install -r requirements.txt --trusted-host pypi.cenditel // Para instalar recursivamente un fichero de requerimientos.

##### Nota #####

Hay paquetes que requieren permisos de superusuario, entonces al usar sudo, o estar como
superusuarios ya no hará efecto el pip.conf que está en /home/usuario/.pip/
entonces, para que sirva con el root tambien crearemos el pip.conf pero en el home del root
que está en /root/.pip/

# touch /root/.pip/pip.conf

# nano /root/.pip/pip.conf // Y hacemos lo mismo que arriba, copiamos el contenido, guardamos y listo.

A veces no se crea el directorio .pip del usuario entonces lo creamos manualmente

/home/user$ mkdir .pip

root@debian# mkdir .pip // en /root
