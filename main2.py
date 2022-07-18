from gl2 import *

glCreateWindow(100, 100) #Creando la ventana.
glClearColor(0, 0, 0) #Llenando el color de la pantalla.
glClear() #Llenando el mapa de bits con el color que se le pasa.

#Se comentó la instancia que está arriba de f.close() para debuggear el glViewPort().

#Ancho y alto de la pantalla en donde se dibujará el punto.
ancho = 25
alto = 25

glViewPort(0, 0, ancho, alto) #Definiendo el área de la imagen sobre la que se va a poder dibujar.
#glColor(0.5, 0.5, 0.5) #Definiendo el color del punto.
#glVertex(0, 0) #Definiendo el punto inicial del punto.
glFinish() #Escribiendo la ventana.