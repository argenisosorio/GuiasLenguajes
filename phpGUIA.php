<!--  Guía PHP by dM -->
<HTML>
	<HEAD>
	<TITLE>Ejemplo de HTML con PHP</TITLE>
	</HEAD>
	<meta charset="UTF-8" />
<!-- -->
<!-- <?php ?> -->
<BODY>
<P><h3>Guía PHP</h3></P>
<?php 
//Comentarios de línea en PHP y /* De varias líneas */ igual a C++
#Comentarios de una línea en PHP
?>

<!--**********OPERADORES ARITMÉTICOS PHP**********
$a + $b //Suma las dos variables.
$a - $b //Resta las dos variables.
$a * $b //Multiplicación de las variables.
$a / $b //División entre las dos variables.
$a % $b //Módulo Resto de la división de $a entre $b -->

<!--**********OPERADORES DE COMPARACIÓN PHP**********
$a == $b //Igualdad Devuelve true si $a y $b son iguales.
$a === $b //Identidad Verdadero si son iguales y del mismo tipo.
$a != $b //Distinto True si son distintos.
$a <> $b //Distinto True si son distintos.
$a < $b //Menor que Cierto si $a es menor que $b
$a > $b //Mayor que Cierto si $a es mayor que $b
$a <= $b //Menor o igual Correcto si $a es menor o igual que $b
$a >= $b //Mayor o igual Correcto si $a es mayor o igual que $b -->

<!--**********OPERADORES DE ASIGNACIÓN COMBINADOS**********
$a++ Incremento $a = $a +1
$a~ Decremento $a = $a -1
++$a Incremento $a = $a +1
~$a Decremento $a = $a -1
$a += $b Suma $a = $a + $b
$a -= $b Resta $a = $a - $b
$a *= $b Multiplicación $a = $a * $b
$a /= $b División $a = $a / $b
$a %= $b Módulo $a = $a % $b
$a &= $b Y $a = $a & $b
$a |= $b O $a = $a | $b
$a A= $b O exclusiva $a = $a A $b
$a .= $b Concatenación $a = $a . $b
$a >>= $b Desplazamiento a la derecha $a = $a >> $b
$a <<= $b Desplazamiento a la izquierda $a = $a << $b -->

**********VARIABLES**********<P>
<?php //Comienzo del lenguaje PHP  
$nombre="Argenis";
$apellido="Osorio";
$edad=24;

#echo Sirve para imprimir por pantalla las cadenas o variables que necesitemos mostrar
echo '$nombre $apellido <br>'; //Las '' simples, permiten imprimir el contenido íntegro de caracteres que esté entre las comillas 
echo "El autor de esta página es: "; //Las "" dobles, permiten incluir variables para imprimirlas junto al texto
echo ("$nombre $apellido de $edad años"); 
?> <!--Final del Lenguaje PHP -->  
<P>

<U>Concatenación de cadenas</U><P>

<?php
$cadenal = "Troya es ";
$cadena2 = "madre de todos, ";
$cadena3 = "peleen por ella!";
$supercadena = $cadenal . $cadena2 . $cadena3;
echo $supercadena;
echo "<p>";

echo $cadenal . $cadena2 . $cadena3;
?><P>

<U>Otros ejemplos de concatenación</U><P>
<?php
$cadenal = "Hola ";
$cadena2 = "Mundo";
$cadenal = $cadenal . $cadena2;
echo $cadenal;
?><P>

<?php
$cadenal = "Hola ";
$cadena2 = "Mundo";
$cadenal .= $cadena2;
echo $cadenal;
?>

<P>**********SINTÁXIS PARA MÚLTIPLES LÍNEAS**********<P>
<?php
$texto = <<<INICIO
Existe en PHP una forma más de introducir cadenas, aparte de las comillas,
muy recomendable para largos textos o un considerable conjunto de
etiquetas HTML. La sintaxis es muy sencilla y comienza con el operador
(<<<) seguido de una etiqueta que indica el principio del texto. Después
de esto podemos escribir un conjunto de caracteres muy numerosos y, para
finalizar, la etiqueta de fin. El ejemplo muestra cómo almacenar un formulario
en una variable: 
INICIO;
echo $texto;
?><P>

<U>Ejemplo de Como PHP guarda el valor de las variables</U><P>
<?php
$a=2;
$b=3;
echo $a + $b; //Imprime 5
echo "<p>";

$a=2;
$b="3";
echo $a + $b; //Imprime 5
echo "<p>";

$a=2;
$b="3a";
echo $a + $b; //Imprime 5
echo "<p>";

$a=2;
$b="a3";
echo $a + $b; //Imprime 2
echo "<p>";
?>

**********SUMA DE ENTEROS PHP**********<P>
<?php
$cifra1=7;
$cifra2=7;
$suma=$cifra1+$cifra2;
?>
<?php echo "La suma de $cifra1 y de $cifra2 es igual a: $suma"; ?> <P>
La suma de los enteros a y b da: <?php echo $cifra1+$cifra2; ?> <P>
La suma es: <?php echo $suma; ?><P> 

**********If else PHP**********<P>
<?php
$a=15;
$b=10;
if ($a>=$b) {
echo ("Verdadero $a es mayor que $b <p>");
}
else {
echo ("Falso $a es menor que $b <p>");
}
?>

<!--Otro ejemplo de IF else-->
<?php
$dia=5;

if ($dia == 1) {
echo "El día es Lunes";
}
else { if ($dia == 2) {
echo "El día es Martes";
}
else {if ($dia == 3) {
echo "El día es Miércoles";
}
else {if ($dia == 4) {
echo "El día es Jueves";
}
else {if ($dia == 5) {
echo "El día es Viernes";
}	
}
}
}
}		
?>
<P>

<!--OTRA FORMA CON ELSEIF-->
<?php
$day=1;
if ($day == 1) {
echo "El día es Lunes";
} elseif ($day == 2) {
echo "El día es Martes";
} elseif ($day == 3) {
echo "El día es Miércoles";
} elseif ($day == 4) {
echo "El día es Jueves";
} elseif ($day == 5) {
echo "El día es Viernes";
}
?>
<P>

<?php #Otro IF en PHP
	$num=2;
	$num2=4;
	$num3=6;

	echo "El numero mayor es: ";

	if($num > $num2) {
		if($num > $num3) {
			echo $num;
		}
	}

	if($num2 > $num) {		
		if($num2 > $num3) {
			echo $num2;
		}
		
		if($num3 > $num2) {
			if($num3 > $num) {
			echo $num3;
		}		
	}	

	}
?><P>

**********CONSTANTES**********<P>
<?php
define ("EMPRESA","Sistemas Osorio"); //Definimos primero la constante y su contenido
echo EMPRESA; //Hay que destacar que el signo de $ no hace falta ponerlo
?>
<P>

<!--Uso de un parrafo dentro de na constante-->
<?php
define ("CONSTANTE","El lenguaje SQL permite la comunicación con el sistema gestor de base de datos. Fue desarrollado<br>
sobre un prototipo de gestor de b.d.d relacionales denominados system r<br>
Diseñado por IBM desarrollado en los años 70, alrededor del 1979 oracle corp. Presento la primera<br>
implementación comercial de SQL.<br>"); 
echo CONSTANTE; 
echo "<P>";

echo CONSTANTE; 
echo "<P>";

echo CONSTANTE; 
echo "<P>";
?>
<P>

**********SWITCH PHP**********<P>
<?php
$dia = 7 ;
switch ($dia) {
	case 1:
		echo "El día es Lunes";
		break;
	case 2 :
		echo "El día es Martes";
		break;
	case 3 :
		echo "El día es Miércoles";
		break;
	case 4 :
		echo "El día es Jueves";
		break;
	case 5:
		echo "El día es Viernes";
		break;
	case 6 :
		echo "El día es Sábado";
		break;
	case 7:
		echo "El día es Domingo" ;
		break;
	default:
	echo "El día de la semana es incorrecto";
}
?>
<P>

**********FOR EN PHP**********<P>
<?php
for ($x = 1; $x < 20; $x++) {
if ($x == 10) {
break;
} else {
echo "$x<br>";
}
}
?>
<P>

**********WHILE EN PHP**********<P>
<?php
$num=1;
while ($num <= 10){
echo $num;
$num++;
}
?>

**********FUNCIONES PHP**********<P>
<?php
	$a = 6; //Variable Global
	$b = 11; //Variable Global

	function miFuncion() {
		global $a, $b; //Variables Local
		$b = $a + $b;
	}
	miFuncion();
	echo $b;
?>
<P>
	
<!--Otra forma -->
<?php
	$aa = 5; //Variable Global
	$bb = 10; //Variable Global
	
	function miFuncion2() {
		$GLOBALS["bb"] = $GLOBALS["aa"] + $GLOBALS["bb"];
	}
	miFuncion2();
	echo $bb;
?><P>


<U>Argumentos por defecto de las funciones</U><P>

<?php
function capitales($Pais,$Capital = "Madrid",$habitantes = "muchos") {
return ("La capital de $Pais es $Capital y tiene $habitantes
habitantes.<br>") ;
}
echo capitales("España");
echo capitales("Portugal","Lisboa");
echo capitales("Francia","Paris","muchísimos");
?><P>

<U>Ejemplo de funciones matemáticas</U><P>

<?php
echo sqrt(9); // Raíz cuadrada de 9 es 3
echo "<p>";
echo rand(1,20); // Número aleatorio entre 1 y 20
echo "<p>";
echo pi(); //Número pi
?><P>

<U>Obtener fecha actual del sistema</U><P>

<!-- 
a Imprime "am" o "pm" 
A "AM" o "PM"
h La hora en formato (01-12).
H Hora en formato 24 (00-23).
g Hora de 1 a 12 sin un cero delante.
G Hora de 1 a 23 sin cero delante.
i Minutos de 00 a 59.
s Segundos de 00 a 59.
d Día del mes (01 a 31).
j Día del mes sin cero (1 a 31).
w Día de la semana (0 a 6). El 0 es el domingo.
m Mes actual (01 al 12).
n Mes actual sin ceros (1 a 12).
Y Año con 4 dígitos (2004).
y Año con 2 dígitos (04).
z Día del año (0 a 365).
t Número de días que tiene el mes actual.-->

<?php
echo date ("d");
echo "/";
echo date ("m");
echo "/";
echo date ("Y");
?>
<P>

<U>Otra forma</U><P>
<?php
echo "Fecha actual: " . date("d-m-Y") . "<br>";
echo "Día del año: " . date("z") . "<br>";
?>

<!-- Función time() -->
<html>
    <head>
        <title>xxx</title>
        <meta charset="UTF-8" />
    </head>	    
<body>
<?php //Comienzo del lenguaje PHP  
    $t=time();
    echo($t . "<br>");
    echo(date("Y-m-d",$t));
?>
</body>
</html>

<P>**********COMPARACIÓN DE CADENAS**********<P>
<?php
$cadenal = "Prueba";
$cadena2 = "Prueba";

if (strcmp($cadenal,$cadena2) == 0) { # strcasecmp no hace distinción entre mayúsculas y minúsculas
echo "Las dos cadenas son iguales";
} elseif (strcmp($cadenal,$cadena2) < 0) {
echo "La cadenal es menor que la cadena2";
} else {
echo "La cadenal es mayor que la cadena2" ;
}
?>

<P>**********SUSTITUCIÓN DE CADENAS**********<P>

<?php
$cadena = "Esta cadena tiene muchas letras";
$cadena = str_replace("Esta","Este",$cadena);
echo str_replace("cadena","conjunto",$cadena);
?>

<P>**********ORDENAMIENTO DE VALORES**********<P>
<!-- 
Función Explicación
asort() Ordena de forma ascendente el array pasado como argumento.
Ordena las parejas índice/valor atendiendo al dato. Es un buen
método para los arrays asociativos.
arsort() Igual que asort () , pero ordena en sentido descendente.
ksort() Ordena de forma ascendente el array pasado como argumento.
Ordena las parejas índice/valor atendiendo esta vez al índice.
krsort() Igual que ksort (), pero ordena en sentido descendente.
sort() Ordena de forma ascendente el array pasado como argumento. Se
pierde el valor asociativo entre el índice y el valor.
rsort() Igual, pero en orden descendente.  -->

<?php
	function recorre ($numero) {
	foreach ($numero as $indice => $valor) {
	echo "$indice: $valor<br>";
	}
	}

	$pila =	array(5,1,4,2,3) ;
	echo "Array sin ordenar<br>" ;
	recorre($pila);
	echo "Ordenación asort()<br>" ;
	asort($pila);
	recorre($pila);
	echo "Ordenación arsort()<br>" ;
	arsort($pila);
	recorre($pila);
	echo "Ordenación ksort()<br>";
	ksort($pila);
	recorre ($pila) ;
	echo "Ordenación krsort()<br>";
	krsort ($pila);
	recorre($pila);
	echo "Ordenación sort()<br>";
	sort($pila);
	recorre($pila);
	echo "Ordenación rsort()<br>";
	rsort($pila);
	recorre($pila);
?>

<P>**********CONECTAR CON LA BASE DE DATOS**********<P>

<?php /*
	$servidor = "localhost";
	$usuario = "luis";
	$pass = "secreto";
	$base_datos = "Compras";
	//Conexión al servidor de bases de datos
	$descriptor = mysql_connect($servidor,$usuario, $pass) ;
	//Se selecciona la base de datos
	mysql_select_db($base_datos,$descriptor);
	//Se cierra la conexión cuando terminemos
	mysql__close ( $descriptor) ;
	*/
?>

<!-- Otra forma y con comprobación de conexión -->

<?php /*
	$conexion=mysql_connect("localhost","root","") or die ("No se conecto");
	mysql_select_db("baseDedatos",$conexion) or die ("No se pudo seleccionar");
	$sql=mysql_query("INSERT INTO tabla(campo1,campo2,campo3,campo4,campo5) 
	value('$valor1','$valor2','$valor3','$valor4','$valor5')",$conexion) or die ("No se almaceno");
	*/
?>	


<P>**********CARGAR VARIABLES CON DATOS DE UN FORM**********<P>

<!DOCTYPE html>
<html>
	<head>  
		<title>Potencia</title>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" /> 
	</head> 

<body bgcolor="SteelBlue">
  <div align="center">
    </p><b>Titulo</b><p>
  </div>

  <div id="formulario" align="center">
    <form action="#" method="post">
      Numero (a): <input type="text" name="a"/> <br /><p></p>
      Numero (b): <input type="text" name="b"/> <br /><p></p>
      <input type="submit" value="Calcular"/>
    </form>
  </div>

  <div align="center">
    <p></p>
    <?php
       $a = $_REQUEST['a'];
       $b = $_REQUEST['b'];
       //echo $a;
       //echo $b;
       //echo "La cifra 1 es $a <br />";
       //echo "La cifra 1 es $b";
    ?>
  </div>  

</body>
</html>
  
  
  

<P>**********XXX**********<P>





<HR>
</BODY>
</HTML>

