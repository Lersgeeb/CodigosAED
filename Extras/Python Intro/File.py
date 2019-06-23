myFile = open("MyTxtFile.txt","r")  #Inicializar el archivo de texto
miStr = myFile.read()   #retorna todas las lineas en forma de string
print("miStr")
                        #de usarse una segunda vez no retornaria nada almenso que:
myFile.seek(0)  #resetea el "cursor" que lee el texto y lo coloca segun su parametro (0 : principio)

miStr = myFile.readlines() #retorna cada linea del texto en una lista 
print(miStr)

myFile.close()  #Cierra el archivo de texto

with open("MyTxtFile.txt") as myNewFile: #Otra forma de abrir un archivo de texto que lo cierra
                                     #automaticamente una vez fuera del bloque
    content = myNewFile.read()
    print(content)

with open("MyTxtFile.txt",mode = "a") as myNewFile2: #w: escribir sobre un archivo
                                        #r: leer el archivo
                                        #a:añadir mas lineas a un archivo
                                        #r+:leer y escribir sobre un archivo
                                        #w+:escribir y leer un archivo(sobrecribe sobre el archivo o lo crea)
    myNewFile2.write("\nmi cuarta linea")
    print(myNewFile2)

with open("MyTxtFile.txt","w") as myNewFile3:
    myNewFile3.write("\nmi quinta linea")    

