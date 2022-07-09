#Nombre: Javier Valle

def glInt(): #Se usará para poder inicializar cualquier objeto interno que requiera el software de render.
    return ""

def glCreateWindow(width, height): #Se usará para inicializar el framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)
    return ""

def glViewPort(x, y, width, height): #Se usará para definir el área de la imagen sobre la que se va a poder dibujar.
    return ""

def glClear(): #Se usará para que llene el mapa de bits con un solo color.
    return ""

def glClearColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
    return ""

def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda
    return ""

def glColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
    return ""

def glFinish(): #Función que escribe el archivo de imagen resultante.
    return ""