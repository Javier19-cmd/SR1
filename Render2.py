from utilidades import *

#Variables globales.

#Ancho y alto de la pantalla.
anchoP, altoP = 0, 0
#Color de la pantalla.
colorP = 0
#Framebuffer de la pantalla.
framebuffer = []

#Este método recibe el color del framebuffer.
def recibirColor(color):
    global colorP

    #Llenando el framebuffer.
    colorP = color


#Método que renderiza el archivo.
def Render2(width, height):
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
