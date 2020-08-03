#######################################################
##### Guía de Tornado Framework by dM y EngelPain #####
#######################################################

// Tornado es un servidor web y un Framework para aplicaciones web escrito en Python.

// Notas:
// Este manual fue probado en GNU/Linux Debian 9 Stretch de 64bits
// Usaremos $ para describir los comandos que se usaran con usuario regular.
// Usaremos # para describir los comandos que se usaran con superusuario.

##### Instalación #####

// Para esta prueba instalaremos tornado usando pip:

# pip install tornado

// Se instaló tornado==5.1.1

// Tornado requiere Python superior a la versión 3.4 y no soportará Python 2.

##### Mi primera aplicación con Tornado #####

// Habiendo realizado el paso de la instalación con éxito, se procederá a crear un archivo, se
llamará en este caso: holamundo con una extensión .py dado que será escrito con Python. 

// Ahora se abre el archivo y dentro de escribirá lo siguiente:

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IOLoop maneja los eventos relacionados con los sockets, por ejemplo, si tienen
# datos disponibles para leer, si pueden escribirse y si se ha producido un error.
import tornado.ioloop

# Envía la aplicación al servidor web
import tornado.web

# Clase que enviará el saludo
class HolaMundoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Mensaje a enviar: ¡Hola mundo!")

# Constructor de la aplicación
def enviar_saludo_app():
    return tornado.web.Application([
        (r"/", HolaMundoHandler),
    ])

if __name__ == "__main__":
    
    # Aplicación que se servirá
    app = enviar_saludo_app()
    
    # Puerto en el que será mostrada
    app.listen(8888)

    # Corre el servidor
    tornado.ioloop.IOLoop.current().start()

##### Despliegue de la aplicación #####

// Desde la consola se debe correr el comando:

$ python holamundo.py

// Visitamos la siguiente URL http://localhost:8888/ en el navegador web
// y se nos mostrará el mensaje de hola mundo

##### Probando saludos en otras urls #####

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IOLoop maneja los eventos relacionados con los sockets, por ejemplo, si tienen
# datos disponibles para leer, si pueden escribirse y si se ha producido un error.
import tornado.ioloop

# Envía la aplicación al servidor web
import tornado.web

# Clase que enviará el saludo
class HolaMundoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("¡Hola mundo!")


# Clase que enviará el saludo
class HolaMundoHandler2(tornado.web.RequestHandler):
    def get(self):
        mensaje = """
        <html>
          <head></head>
          <body>
            <p>¡Hola mundo 2!</p>
          </body>
        </html>
        """
        self.write(mensaje)

# Constructor de la aplicación
def enviar_saludo_app():
    return tornado.web.Application([
        (r"/", HolaMundoHandler),
        (r"/2", HolaMundoHandler2),
    ])

if __name__ == "__main__":

    # Aplicación que se servirá
    app = enviar_saludo_app()

    # Puerto en el que será mostrada
    app.listen(8888)

    # Corre el servidor
    tornado.ioloop.IOLoop.current().start()
