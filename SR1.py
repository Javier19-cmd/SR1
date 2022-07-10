"""
#Nombre: Javier Valle
#Carnet: 20159

Referencias: 

1. Instanciar un archivo de Python: https://www.youtube.com/watch?v=rYcluou5gEo&ab_channel=LuisCabreraBenito
2. Saber si un número es múltiplo de otro: https://www.youtube.com/watch?v=jOCh6ZpkE1k&ab_channel=JohnOrtizOrdoñez
3. Hacer un return de múltiples variables: https://www.youtube.com/watch?v=QOQTYuynU3w&ab_channel=ProgramaResuelto
4. Formato de archivo BMP: https://en.wikipedia.org/wiki/BMP_file_format#:~:text=The%20BMP%20file%20format%2C%20also,and%20OS%2F2%20operating%20systems. 
"""

import Render

def glInt(): #Se usará para poder inicializar cualquier objeto interno que requiera el software de render.
    glColor(0, 0.02, 0.01) #Creando el color de la línea.

    #Importar la clase de Render.
    r = Render.Render(ancho, alto)

def glCreateWindow(width, height): 
    #Se usará para inicializar el framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)
    
    try: 
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            return width, height
        else:
            print("Error")
    except: 
        print("Ocurrió un error")

ancho, alto = glCreateWindow(1024, 2048) #Se inicializan las dimensiones de la ventana.

def glViewPort(x, y, width, height): #Se usará para definir el área de la imagen sobre la que se va a poder dibujar.
    return ""

def glClear(): #Se usará para que llene el mapa de bits con un solo color.
    return ""

def glClearColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
    return ""

def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda
    return ""

def glColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
    #Convertir el valor de 0 a 1 de 0 a 255 y luego llamar al color.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    else:
        color = bytes([int(b * 255), int(g * 255), int(r * 255)])
        return color

def glFinish(): #Función que escribe el archivo de imagen resultante.
    return ""


glInt() #Inicializando el programa.