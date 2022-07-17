from utilidades import *

#Variables globales del archivo.
framebuffer = []
ancho, alto = 0, 0 

#Método para poder escribir el framebuffer del archivo de imagen.
def FrameBuffer(r, g, b):
    global framebuffer #Variable global para modificar el framebuffer del archivo.

    #Llenando de bits el framebuffer.
    framebuffer = [
        [color(r, g, b) for x in range(ancho)]
        for y in range(alto)
    ]

def Render(Width, Height):
    global ancho, alto #Variables globales del archivo que se modificarán.

    #Llenando las variables globaloes.
    ancho = Width
    alto = Height

    #Método que sirve para poder crear el archivo de imagen.
    def write():

        #Se abre el archivo con la forma de bw.
        f = open("SR1.bmp", "bw")

        #Se escribe el encabezado del archivo.

        #Haciendo el pixel header.
        f.write(char('B'))
        f.write(char('M'))
        #Escribiendo el tamaño del archivo en bytes.
        f.write(dword(14 + 40 + Width * Height * 3))
        f.write(dword(0)) #Cosa que no se utilizará en este caso.
        f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
        #Lo anterior suma 14 bytes.

        #Información del header.
        f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(Width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(Height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
        f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
        f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(Width * Height * 3)) #Tamaño de la imagen sin el header.
        #Pixels que no se usarán mucho.
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        #Lo anterior suma 40 bytes.

        # #Pintando el archivo de color negro.
        # for x in range(Height):
        #     for y in range(Width):
        #         f.write(framebuffer[x][y])

        f.close() #Cerrando el archivo que se escribió.

    #Creando punto para debuggear la creación del archivo. Preguntar si está bien esta función en esta clase.
    def point(x, y, color):
        #Se escribe el pixel en la posición x, y con el color.
        framebuffer[x][y] = color

    #point(200, 400, color) #Creando el punto.
    write() #Llamando al método que escribirá el archivo.