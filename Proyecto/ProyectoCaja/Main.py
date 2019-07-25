from Clip import *
from CopyEraser import *
from Eraser import *
from Folder import *
from Marker import *
from Pen import *
from PostIt import *
from ReamOfPaper import *
from Staple import *
from Stapler import *
from Tape import *
from Box import *
from Shelf import *

#creando algunos objetos
clip1 = Clip("Sifap","Mediano")
eraser1 = Eraser("Milan","Grande")
eraser2 = Eraser("Pelikan","Pequeño")
pen1 = Pen("Bic","2HB")
pen2 = Pen("Bic","4HB")
pen3 = Pen("Stabilo","4HB")
pen4 = Pen("Studio","4HB")
marker1 = Marker("Sharpie","Permanente")
marker2 = Marker("Bic","Permanente")
reamOfPaper1 = ReamOfPaper("Chamex","Hoja carta","200")
folder1 = Folder("Econofile","grande","200")
tape1 = Tape("Tesa", "Transparente")
stapler1 = Stapler("King", "200", "Grande")

#creando caja1
box1 = Box()

#Agregando objetos a la caja1
box1.add(clip1)
box1.add(pen1)
box1.add(pen2)
box1.add(pen3)
box1.add(folder1)

box1.showContent() #imprimir el contenido de la caja

#creando caja2
box2 = Box()

#Agregando objetos a la caja2
box2.add(eraser1)
box2.add(eraser2)
box2.add(marker1)
box2.add(marker2)
box2.add(tape1)

box2.showContent() #imprimir el contenido de la caja

#creando caja3
box3 = Box()

#Agregando objetos a la caja3
box3.add(stapler1)
box3.add(reamOfPaper1)

box3.showContent() #imprimir el contenido de la caja

#Crear Estante
shelf = Shelf()

#Agregar cajas a estante
shelf.push(box1)
shelf.push(box2)
shelf.push(box3)

#Mostrar cantidad de cajas en el estante
print(shelf.nBoxes())

#Imprimir contenido de la última caja en entrar
shelf.pop().showContent()
