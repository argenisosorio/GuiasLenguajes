// ### Guía C y C++ by dM ###

// Comentarios de Linea

/*
Comentarios de
multiple Linea
*/

**********Instalacion del compilador**********

//Es Necesario instalar el compilador para probar codigos de los programas

$ aptitude install build-essential

$ sudo apt-get install build-essential 


**********PROGRAMAS EN C**********

Los programas en C se guardan con la extension NombrePrograma.c

-Debe estar ubicado en el directorio del programa

gcc programa.c -o programa //Para Compilar el programa, -o para convertirlo en objeto
./programa //Para correr el programa

*****PROGRAMAS EN C++*****

Los programas en C++ se guardan con la extension NombrePrograma.cpp

-Debe estar ubicado en el directorio del programa

g++ programa.cpp -o programa //Para Compilar el programa
./programa //Para correr el programa


**********Imprimir por pantalla**********

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


**********VARIABLES**********

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


**********IF ELSE**********

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

#include<iostream> //Comparar dos numeros enteros
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


**********FOR**********

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


**********WHILE**********

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

//CALCULAR EL PROMEDIO DE NOTAS
#include<iostream>
using namespace std;
int main() {   
   int num,i=0,nota=0;   
   cout<<"CALCULAR EL PROMEDIO DE NOTAS"<<endl;
   cout<<"Introduzca el numero de Estudiantes: ";
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


**********DO WHILE**********

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


**********FUNCIONES**********

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

**********FUNCIONES CON PARAMETROS**********

//Funcion para sumar dos numeros pasando con parametros
#include<iostream>
using namespace std;
int suma; //Variable Global, puede ser usada por las funciones

int funcionSuma(int a, int b)
    {
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

//Funcion para sumar dos numeros
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

//Funcion para sumar dos numeros, todo dentro de la función
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

**********CLASES**********

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


**********EJEMPLOS**********

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

############################
##### Uso de Librerias #####
############################

Las librerías nos permite el uso de funciones en un programa sin la necesidad de escribir su código en nuestro programa
únicamente llamando a la biblioteca donde está contenida. Existen bibliotecas estándares en C que ya vienen incluida en la
mayoría de los compiladores, como son stdio.h, math.h, time.h... 
Para utilizar nuestra biblioteca, únicamente basta con situar en la cabecera del programa el nombre de la biblioteca para
poder utilizar todas las funciones contenidas en la misma.

1- Generar las funciones que necesitemos y escribelas todas juntas (codigo y cabeceras) en un mismo fichero:

int suma;
int funcionSuma(int a, int b){
    suma=a+b;
}

2- El fichero creado anteriormente, guardalo con extension .h, por ejemplo libreria.h (importante no ejecutarlo para que no le pueda cambiar sola la extensión).
Se deberá guardar en el mismo directorio de nuestro programa principal el .cpp

3- Llamar a la biblioteca en el programa. Deberemos colocar en la cabecera del programa, junto a los llamamiento de otras bibliotecas:

#include <libreria.h> // Cuando el fichero libreria.h se encuentre en la carpeta include de nuestro compilador.
#include "libreria.h" // Cuando el fichero libreria.h esté en el mismo directorio que el archivo que queremos compilar.

4- Uso de las funciones de la biblioteca: Finalmente ya podemos usar las funciones de libreria.h sin necesidad de copiar el codigo,
tal y como ilustra el programa siguiente, lo guardamos como .cpp, compilamos y ejecutamos y listo, debería realizar las operaciones
declaradas sin problemas.

#include<iostream>
#include <stdio.h>
#include "libreria.h"
using namespace std;
int main() {
    funcionSuma(15,20);
    cout<<suma<<endl;
    return 0;
}


