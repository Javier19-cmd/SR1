from utilidades import *

#Variables globales.

#Ancho y alto de la pantalla.
anchoP, altoP = 0, 0

#Color del framebuffer.
colorP = 0

#Framebuffer de la pantalla.
framebuffer = []

#Este método recibe el color del framebuffer.
def recibirColorFondo(color):
    global colorP

    #Llenando el framebuffer.
    colorP = color


#Método que renderiza el archivo.
def DimensionesPantalla(width, height):
    global anchoP, altoP

    #Llenando las variables globales.
    anchoP = width
    altoP = height

#Método que escribe el framebuffer.
def Framebuffer():
    print(colorP)

    print(colorP)
    global framebuffer

    #Llenando de bits el framebuffer.
    framebuffer = [
        [colorP for x in range(anchoP)]
        for y in range(altoP)
    ]

#Método que escribe el archivo bmp.
def Render2():
        
        #Se abre el archivo con la forma de bw.
        f = open("prueba.bmp", "bw")

        #Se escribe el encabezado del archivo.

        #Haciendo el pixel header.
        f.write(char('B'))
        f.write(char('M'))
        #Escribiendo el tamaño del archivo en bytes.
        f.write(dword(14 + 40 + anchoP * altoP * 3))
        f.write(dword(0)) #Cosa que no se utilizará en este caso.
        f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
        #Lo anterior suma 14 bytes.

        #Información del header.
        f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(anchoP)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(altoP)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
        f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
        f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(anchoP * altoP * 3)) #Tamaño de la imagen sin el header.
        #Pixels que no se usarán mucho.
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        #Lo anterior suma 40 bytes.

        #Pintando el archivo de color negro.
        for x in range(altoP):
            for y in range(anchoP):
                f.write(framebuffer[y][x])


        f.close() #Cerrando el archivo que se escribió.
