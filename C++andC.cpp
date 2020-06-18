=================================
Guía de C y C++ by dM
=================================

// Comentarios de Linea

/*
Comentarios de
multiple Linea
*/

====
Nota
====

Usaremos $ para describir los comandos que se usaran con usuario regular.

Usaremos # para describir los comandos que se usaran con superusuario.

==========================
Instalacion del compilador
==========================

Es Necesario instalar el compilador para probar codigos de los programas

#  apt-get install build-essential

==============
Programas en C
==============

Los programas en C se guardan con la extension NombrePrograma.c

Debe estar ubicado en el directorio del programa

Para compilar el programa, -o para convertirlo en objeto.

$ gcc programa.c -o programa 

Para correr el programa

$ ./programa

================
Programas en C++
================

Los programas en C++ se guardan con la extension NombrePrograma.cpp

Debe estar ubicado en el directorio del programa

Para compilar el programa

$ g++ programa.cpp -o programa

Para correr el programa

$ ./programa 

==========
Ejercicios
==========

// Imprimir por pantalla
#include<iostream>
using namespace std;
int main (){
    cout<<"Wake up Neo..."; //Imprimir por pantalla una cadena   
    cout<<5000; //Imprimir por pantalla un entero    
    cout<<"\t Hola \n"; // \t imprime una tabulacion en la linea y \n es un de linea
    return 0;
}

--------------------

#include<iostream>
using namespace std;
int main (){    
    cout<<"Wake up Neo..."<<endl; //Imprimir por pantalla una cadena    
    cout<<"Wake up Neo..."<<endl; // endl es un fin de lienea, lo proximo que imprima aparece en otra linea
    return 0;
}


=========
Variables
=========

#include<iostream>
using namespace std;
char nombre[20]; // Variable de tipo char con un tamaño maximo de 20, se debe asignar el tamaño
int cedula; // Variable de tipo entero 

int main() {
    cout<<"Introduzca su nombre: "<<endl; // Pedimos los datos por pantalla para ser guardados
    cin>>nombre; // Guardamos la cadena en la variable declarada
    cout<<"Introduzca su cedula: "<<endl; // Pedimos los datos por pantalla para ser guardados
    cin>>cedula; // Guardamos la cadena en la variable declarada
    cout<<"Su nombre es: "<<nombre<<endl; // Mostramos el contenido de la variable
    cout<<"su cedula es: "<<cedula<<endl; // Mostramos el contenido de la variable
return 0;
}

--------------------

#include<iostream>
using namespace std;
string nombre="argenis"; // Asignamos una cadena como vaor de la variable
int main (){
    cout<<"El nombre es: "<<nombre<<endl; // Mostramos el contenido de la variable
    cout<<nombre<<endl; // Mostramos el contenido de la variable
    return 0;
}


=======
if else
=======

#include<iostream>
using namespace std;
int main() {   
   int a=3;
   if (a==1){
      cout<<"a es igual a 1"<<endl;   
   }
   else if(a==2){
      cout<<"a es igual a 2"<<endl;   
   }
   else if(a==3){
      cout<<"a es igual a 3"<<endl;   
   }   
return 0;
}

--------------------

// Comparar dos numeros enteros
#include<iostream>
using namespace std;
int a,b;
int main (){	
	cout<<"Introduzca el numero de A"<<endl;
    cin>>a;    
    cout<<"Introduzca el numero de B"<<endl;
    cin>>b;
    if(a==b){
    cout<<"A es igual a B"<<endl;
    }        
    else{
    cout<<"A es diferente de B"<<endl;
    }
    return 0;
}

=============
for structure
=============

//Calcular la suma de n numeros introducidos por teclado
#include<iostream>
using namespace std;

int main() {
int n,i;
float suma=0,num;
    cout<<"Introduzca la cantidad de numeros a sumar: ";
    cin>>n;
    for(i=0;i<n;i++) {
        cout<<"Introduzca un valor:  ";
        cin>>num;
        suma=suma+num;
    }
    cout<<"El resultado de la suma es: "<<suma<<endl;
return 0;
}

=====
while
=====

//Calcular la suma de n numeros introducidos por teclado
#include<iostream>
using namespace std;
int main() {
int n,i=0;
float suma=0,num;   
   cout<<"Introduzca cantidad de numeros que quiere sumar: ";
   cin>>n;   
   while(i<n){
      cout<<"Introduzca numero a sumar: ";
      cin>>num;
      suma=suma+num;
      i++;
   }
   cout<<"El total de la suma es: "<<suma<<endl;   
return 0;
}

--------------------

// Calcular el promedio de notas de n alumnos.
#include<iostream>
using namespace std;
int main() {
  int num,i=0,nota=0;
  cout<<"Calcular el promedio de notas de n alumnos."<<endl;
  cout<<"Introduzca el número de estudiantes: ";
  cin>>num;
  float notas[num],suma=0,promedio=0;
  while (i<num) {
  cout<<"Nota "<<i<<": ";
  cin>>notas[i];
  i++;
  } 
  for(int j=0;j<num;j++){
  suma=suma+notas[j];
  }
  promedio= suma / num;
  cout<<"El promedio de notas es: "<<promedio<<endl;
return 0;
}

========
do while
========

//Calcular la suma de N numeros introducidos
#include<iostream>
using namespace std;

int main() {
    int n,i=0,t;
    int suma=0;
    cout<<"Introduzca la cantidad de numeros a sumar: ";
    cin>>n;    
    do {
        cout<<"Introduzca un valor: ";
        cin>>t;
        suma=suma+t;
        i++;
    }
    while(i<n);
    cout<<"El resultado de la suma es: "<<suma<<endl;    
return 0;
}

=========
Funciones
=========

#include<iostream>
using namespace std;

void funcion1() {
    cout<<"Cadena de texto"<<endl; 
    }

void funcion2() {
    cout<<5000<<endl; 
    }

int main () {
    funcion1();
    funcion2();
    return 0;
}

========================
Funciones con parametros
========================

//Funcion para sumar dos numeros pasando con parametros
#include<iostream>
using namespace std;
int suma; // Variable Global, puede ser usada por las funciones
int funcionSuma(int a, int b) {
  suma=a+b;
  cout<<suma<<endl;
  }
int main() {
  funcionSuma(5,4);
  return 0;
}

--------------------

#include<iostream>
using namespace std;
int suma=20; //Variable global que puede ser usada por cualquier funcion del programa. 
int funcionSuma(){
    int suma=10; //Variable local que solo puede ser usada por la funcion donde fue declarada.
    cout<<"Variable local vale: "<<suma<<endl;
}
int main() {
    cout<<"Variable global vale: "<<suma<<endl; 
    funcionSuma();
return 0;
}

--------------------

// Funcion para sumar dos numeros
#include<iostream>
using namespace std;
int suma;
int a,b;
int funcionSuma(){
  suma=a+b;
  cout<<"La suma es: "<<suma<<endl;
}
int main() {
  cout<<"Introduzca un numero A: ";
  cin>>a;
  cout<<"Introduzca un numero B: ";
  cin>>b;
  funcionSuma();
return 0;
}

--------------------

// Funcion para sumar dos numeros, todo dentro de la función
#include<iostream>
using namespace std;
int suma;
int a,b;
int funcionSuma(){
    cout<<"Introduzca un numero A: ";
    cin>>a;
    cout<<"Introduzca un numero B: ";
    cin>>b;
    suma=a+b;
    cout<<"La suma es: "<<suma<<endl;
}
int main() {
    funcionSuma();
return 0;
}

--------------------

#include<iostream>
using namespace std;
int edades[3]; 
int solicitar() {    
  for(int i=0;i<3;i++){
  cout<<"Por favor introduzca las edad: ";
    cin>>edades[i];
    }
}
int imprimir() {
  for(int j=0;j<3;j++){
  cout<<"Su edades son: "<<edades[j]<<endl;
  }
}
int main() {
  solicitar();
  imprimir();
return 0;
}

======
Clases
======

#include <iostream>
using namespace std;
class Persona { // Declaramos la clase    
    private:   
    float edad; // Atributos privados de la clase
    float cedula; // Atributos privados de la clase
    public:                                       
    int pedir_edad() { return edad = 25;} // Metodos de la clase, seran las funciones que interactuan con los atributos
    int pedir_cedula() { return cedula = 19592165;} // Metodos de la clase, seran las funciones que interactuan con los atributos                  
};
int main()
{
  Persona argenis; // Creamos un objeto (argenis) comenzando con el nombre de la Clase (Persona)
  cout<<"La edad de Argenis es: "<<argenis.pedir_edad()<<endl; // El objeto creado (argenis) ereda los metodos y atributos de la clase (Persona)  
  cout<<"La cedula de Argenis es: "<<argenis.pedir_cedula()<<endl; // El objeto puede usar los metodos declarados en la clase de la cual ereda    
  return 0;
}

--------------------

/*El (::) es llamado el operador de resolución de ámbito. Esencialmente le dice al compilador que pedir_edad y
mostrar_edad pertenecen a la clase Persona. Dicho de otra forma, :: declara que esas funcionen se encuentra en el
ámbito de la clase Persona. Varias clases diferentes pueden usar los mismos nombres de función. El compilador
sabe cuál función pertenece a cuál clase y esto es posible por el operador de resolución de ámbito y el nombre
de la clase.*/

#include <iostream>
using namespace std;
class Persona {          
    private:   
    float edad;
    public:                                       
    int pedir_edad();
    int mostrar_edad();
};
int Persona::pedir_edad(){
    cout<<"Por favor introduzca la edad: ";
    cin>>edad;    
}    
int Persona::mostrar_edad(){
    //return (edad);
    cout<<"La edad de Argenis es: "<<edad<<endl; 
}
int main()
{
  Persona argenis;
  argenis.pedir_edad();
  argenis.mostrar_edad();   
  return 0;
}


========
Ejemplos
========

//Calcular el promedio de notas de alumnos
#include<iostream>
using namespace std;
int i=0,num;
float promedio,suma;
int notas[10];
int main() {   
   cout<<"Introduzca el numero de Estudiantes: ";
   cin>>num;
   while (i<num) {
   cout<<"Nota: ";
   cin>>notas[i];
   i++;
   }   
   for(int j=0;j<num;j++){
      //cout<<"Las notas son: "<<notas[j]<<endl;
      suma=suma+notas[j];
      promedio=suma/num;
   }
   cout<<"La suma de las notas es: "<<suma<<endl;
   cout<<"El promedio de notas es: "<<promedio<<endl;      
return 0;
}

============================================
Teoría sobre librerias estáticas y dinámicas
============================================

Según vamos haciendo programas, nos damos cuenta que algunas partes del código
se utilizan en muchos de ellos. Por ejemplo, podemos tener varios programas que
utilizan números complejos y las funciones de suma, resta, etc son comunes.
También es posible, por ejemplo, que nos guste hacer juegos, y nos damos cuenta
que estamos repitiendo una y otra vez el código para mover una imagen por la
pantalla.

Sería estupendo poder meter esas funciones en un directorio separado de los
programas concretos y tenerlas ya compiladas, de forma que podamos usarlas
siempre que queramos. Las ventajas enormes de esto son:

-No tener que volver a escribir el código (o hacer copy-paste).

-Nos ahorraremos el tiempo de compilar cada vez ese código que ya está
compilado. Además, ya sabemos que mientras hacemos un programa, probamos
corregimos, hay que compilar entre muchas y muchas veces.

-El código ya compilado estará probado y será fiable. No las primeras veces,
pero sí cuando ya lo hayamos usado en 200 programas distintos y le hayamos ido
corrigiendo los errores.

La forma de hacer esto es hacer librerías. Una librería son una o más funciones
que tenemos ya compiladas y preparadas para ser utilizadas en cualquier programa
que hagamos.  Hay que tener el suficiente ojo cuando las hacemos como para no
meter ninguna dependencia de algo concreto de nuestro programa. Por ejemplo, si
hacemos nuestra función de mover la imagen, tendremos que hacer la función de
forma que admita cualquier imagen ya que no nos pegaría nada Lara Croft dando
saltos en un juego estilo space invaders.

=========================================
Cómo tenemos que organizar nuestro código
=========================================

Para poder poner nuestro código en una librería, necesitamos organizarlo de la
siguiente manera:

-Uno o más ficheros fuente .c o .cpp con el código de nuestras funciones.

-Uno o más ficheros de cabecera, las librerías .h con los tipos (typedefs,
structs y enums) y prototipos de las funciones que queramos que se puedan utilizar.

===============================
Librerias estáticas y dinámicas
===============================

En linux podemos hacer dos tipos de librerías: estáticas y dinámicas.

Una librería estática es una librería que 'se copia' en nuestro programa cuando
lo compilamos. Una vez que tenemos el ejecutable de nuestro programa, la
librería no sirve para nada (es un decir, sirve para otros futuros proyectos).
Podríamos borrarla y nuestro programa seguiría funcionando, ya que tiene copia
de todo lo que necesita. Sólo se copia aquella parte de la librería que se
necesite. Por ejemplo, si la librería tiene dos funciones y nuestro programa
sólo llama a una, sólo se copia esa función.

Una librería dinámica NO se copia en nuestro programa al compilarlo. Cuando
tengamos nuestro ejecutable y lo estemos ejecutando, cada vez que el código
necesite algo de la librería, irá a buscarlo a ésta. Si borramos la librería,
nuestro programa dará un error de que no la encuentra.

====================================================================
¿Cuáles son las ventajas e inconvenientes de cada uno de estos tipos
de librerías?
====================================================================

-Un programa compilado con librerías estáticas es más grande, ya que se hace
copia de todo lo que necesita.

-Un programa compilado con librerías estáticas se puede llevar a otro ordenador
sin necesidad de llevarse las librerías.

-Un programa compilado con librerías estáticas es, en principio, más rápido en
ejecución. Cuando llama a una función de la librería, la tiene en su código y no
tiene que ir a leer el fichero de la librería dinámica para encontrar la función
y ejecutarla.

-Si cambiamos una librería estática, a los ejecutables no les afecta. Si
cambiamos una dinámica, los ejecutables se ven afectados. Esto es una ventaja si
hemos cambiado la librería para corregir un error (se corrige automáticamente en
todos los ejecutables), pero es un inconveniente si tocar eso nos hace cambiar
los ejecutables (por ejemplo, hemos añadido un parámetro más a una función de la
librería, los ejecutables ya hechos dejan de funcionar).

===================================
¿Qué tipo de librería uso entonces?
===================================

Es como siempre una cuestión de compromiso entre las ventajas y los
inconvenientes. Para programas no muy grandes y por simplicidad, se suelen usar
librerías estáticas. Las dinámicas están bien para programas enormes o para
librerías del sistema, que como están en todos los ordenadores con linux no es
necesario andar llevándoselas de un lado a otro.

En unix las librerías estáticas suelen llamarse libnombre.a y las dinámicas
libnombre.so, donde nombre es el nombre de nuestra librería.

================
Uso de librerias
================

Las librerías nos permite el uso de funciones en un programa sin la necesidad de
escribir su código en nuestro programa únicamente llamando a la biblioteca donde
está contenida. Existen bibliotecas estándares en C que ya vienen incluida en la
mayoría de los compiladores, como son stdio.h, math.h, time.h... Para utilizar
nuestra biblioteca, únicamente basta con situar en la cabecera del programa el
nombre de la biblioteca para poder utilizar todas las funciones contenidas en la
misma.

1- Generar las funciones que necesitemos y escribelas todas juntas (codigo y
cabeceras) en un mismo fichero:

int suma;
int funcionSuma(int a, int b){
    suma=a+b;
}

2- El fichero creado anteriormente, guardalo con extension .h, por ejemplo
libreria.h (importante no ejecutarlo para que no le pueda cambiar sola la
extensión). Se deberá guardar en el mismo directorio de nuestro programa
principal el .cpp

3- Llamar a la biblioteca en el programa. Deberemos colocar en la cabecera del
programa, junto a los llamamiento de otras bibliotecas:

#include <libreria.h> // Cuando el fichero libreria.h se encuentre en la carpeta include de nuestro compilador.
#include "libreria.h" // Cuando el fichero libreria.h esté en el mismo directorio que el archivo que queremos compilar.

4- Uso de las funciones de la biblioteca: Finalmente ya podemos usar las
funciones de libreria.h sin necesidad de copiar el codigo, tal y como ilustra
el programa siguiente, lo guardamos como .cpp, compilamos y ejecutamos y listo,
debería realizar las operaciones declaradas sin problemas.

#include<iostream>
#include <stdio.h>
#include "libreria.h"
using namespace std;
int main() {
  funcionSuma(15,20);
  cout<<suma<<endl;
  return 0;
}