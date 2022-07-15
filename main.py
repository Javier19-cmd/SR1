from gl import *

def main():
    
    glInit()

    alto = int(input("Ingrese el alto de la ventana: "))
    ancho = int(input("Ingrese el ancho de la ventana: "))

    glCreateWindow(ancho, alto) #Creando la ventana.
    glClearColor(0.003, 1, 0.019) #Llenando el color de la pantalla.
    glClear(0.1, 0.5, 0.8) #Llenando el mapa de bits con el color que se le pasa.
    glViewPort(0, 0, ancho, alto) #Definiendo el área de la imagen sobre la que se va a poder dibujar.
    glColor(0.5, 0.5, 0.5) #Definiendo el color de la línea.
    glVertex(0, 0) #Definiendo el punto inicial de la línea.
    glFinish() #Finalizando la ventana.

    print(alto, ancho)

main()