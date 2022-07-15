from utilidades import *

#Archivo que inicializará el software de render.
class Render(object):

    framebuffer = []

    def __init__(self, width, height):
        
        #Se inicializan los valores de la ventana.
        self.width = width
        self.height = height

        #Método que sirve para poder crear el archivo de imagen.
        def write():

            #Se abre el archivo con la forma de bw.
            f = open("SR1.bmp", "bw")

            #Haciendo el pixel header.
            f.write(char('B'))
            f.write(char('M'))
            #Escribiendo el tamaño del archivo en bytes.
            f.write(dword(14 + 40 + self.width * self.height * 3))
            f.write(dword(0)) #Cosa que no se utilizará en este caso.
            f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
            #Lo anterior suma 14 bytes.

            #Información del header.
            f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
            f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
            f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(width * height * 3)) #Tamaño de la imagen sin el header.
            #Pixels que no se usarán mucho.
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            #Lo anterior suma 40 bytes.

            #Pintando el archivo de color negro.
            for x in range(self.height):
                for y in range(self.width):
                    f.write(self.framebuffer[x][y])

            f.close() #Cerrando el archivo que se escribió.

        #Creando punto para debuggear la creación del archivo. Preguntar si está bien esta función en esta clase.
        def point(x, y, color):
            #Se escribe el pixel en la posición x, y con el color.
            self.framebuffer[x][y] = color

        #point(200, 400, color) #Creando el punto.
        write() #Llamando al método que escribirá el archivo.