print("---------------------------------------------------------------------------------")
filestr ="Extras\\Python Intro\\MyTxtFile.txt"

myFile = open(filestr)  #Inicializar el archivo de texto
miStr = myFile.read()   #retorna todas las lineas en forma de string
print(miStr)
myBackup = miStr
                        #de usarse una segunda vez no retornaria nada almenso que:
myFile.seek(0)  #resetea el "cursor" que lee el texto y lo coloca segun su parametro (0 : principio)
print("---------------------------------------------------------------------------------")
miStr = myFile.readlines() #retorna cada linea del texto en una lista 
print(miStr)
print("---------------------------------------------------------------------------------")
myFile.close()  #Cierra el archivo de texto

with open(filestr) as myNewFile: #Otra forma de abrir un archivo de texto que lo cierra
                                     #automaticamente una vez fuera del bloque
    content = myNewFile.read()
    print(content)

print("---------------------------------------------------------------------------------")

with open(filestr,mode = "a") as myNewFile2:    #w: escribir sobre un archivo (sobrescribe los datos)
                                                #r: leer el archivo
                                                #a:añadir mas lineas a un archivo
                                                #r+:leer y escribir sobre un archivo
                                                #w+:escribir y leer un archivo(sobrecribe sobre el archivo o lo crea)
    myNewFile2.write("\nmi cuarta linea")

with open(filestr,"r") as myNewFile3:                                     
    content = myNewFile3.read()
    print(content) 
  
print("---------------------------------------------------------------------------------")

with open(filestr,"w") as myNewFile3:   
    myNewFile3.write(myBackup)   

with open(filestr) as myNewFile3:                              
    content = myNewFile3.read()
    print(content) 

#C:\\Users\\Manuel\Downloads\\Gabriel\\V periodo\\Algoritmo y Estructura de Datos\\codigos\\Extras\\Python Intro\\MyTxtFile.txt