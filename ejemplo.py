import struct

#Set de utilidades. Estas funciones se pueden hacer en otro archivo para mayor comodidad.

#Recibe un string y lo convierte en una lista de bytes.
def char(c):
    #Ocupa 1 byte.
    #=c es para que sea un caracter. El encode es para convertir el caracter a bits. El =c es para convertir esos bits a bytes.
    return struct.pack("=c", c.encode('ascii'))

#Recibe un número como parámetro.
def word(w):
    #Ocupa 2 bytes.
    #El formato para un word es 'h'. Este gasta 2 bytes, que es lo que se quiere.
    return struct.pack("=h", w)

#Recibe un número como parámetro.
def dword(d): #Double word.
    #Ocupa 4 bytes. El l es para un num de 4 bytes.
    return struct.pack("=l", d)

def color(r, g, b): #Función que crea el color.
    #3 bytes
    return bytes([b, g, r])

#Colorea un punto de la imagen.
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

class Render(object):
    #Puede quedar vacío.
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.clear() #Llama al método clear. Barre lo anterior que puede estar.

    #Método que se usará para dibujar un punto en la pantalla.
    def clear(self):
        #Generador del color.
        self.framebuffer = [
            [(200, 0, 0) for x in range(self.width)] for y in range(self.height)
        ]
    
    def write(self, filename):
        #Abrir en bw: binary write.
        f = open(filename, "bw")
        #Pixel header.
        f.write(char('B'))
        f.write(char('M'))
        #Tamaño del archivo en bytes.
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0)) #Algo que no se usará.
        f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen.
        
        #Info header.
        f.write(dword(40)) 
        f.write(dword(self.width)) #Ancho de la imagen.
        f.write(dword(self.height)) #Alto de la imagen.
        
        f.write(word(1)) #1 color de pixel.
        f.write(word(24)) #24 bits por pixel.
        f.write(dword(0)) #Algo que no se usará.
        
        #Tamaño de la imagen sin el header.
        f.write(dword(self.width * self.height * 3)) 

        #Pixels que no se usarán mucho.
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #Escribir la imagen como tal.
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()
    
    #Hacer un punto.
    def point(self, x, y, c):
        self.framebuffer[x][y] = c
    
    def set_current_color(self, c): #Cambiar el color actual.
        self.current_color = c


r = Render(1024, 1024) #Crea un objeto render con un tamaño de 1024x1024.

r.set_current_color = color(200, 100, 0)

for x in range(100, 200):
    for y in range(100, 200):
        r.point(x, y) #Punto rojo.
r.write("a.bmp") #Escribe el archivo.