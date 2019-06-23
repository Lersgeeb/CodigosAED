print("\nhello world")
print("...\n")

unaStr = "10"
numInt = 2
numFlt = 3.5e-3

print("Imprimiendo diferentes tipos de datos")
print(numFlt, "- dato tipo float")
print(numInt, "- dato tipo int")
print(unaStr, "- dato tipo String\n")

Strtoint = int(unaStr)
print(Strtoint, "Conversion de String a int\n")

print("\nNumero agregado con Formatting: {}".format(unaStr)) # agregar string con formatting
print(f"Numero agregado con Formatting: {unaStr}") # agregar string con formatting
print("Numero float agregado con Formatting: {nf}".format(nf=numFlt)) # agregar string con formatting
print("Numero float agregado con Formatting: {nf:10.3f}\n".format(nf=numFlt))# {valor:espacio.decimalesf}

print("hacer lista y luego usar metodo para revertir los valores")
miLista = [3,2,1]
print(miLista)
miLista.reverse() #invierte los datos de la lista
print(miLista)
miLista.extend([4,5,6]) #agrega varios datos o otra lista (se puede hacer con el operador "+")
print(miLista)
print(miLista[0:3]) #imprime del primer dato al segundo
miLista.insert(3,3.5)#en el indice dado en el primer valor se guarda el segundo valor
print(miLista)
print("2 esta en la posicion:",miLista.index(2))#busca la posicion del valor

if(1 in miLista):   #se busca el objeto en la lista y retorna un valor boolean 
    print("1 esta en la lista")
if(9 in miLista):
    print("9 esta en la lista")   

miLista.append("esto es una string") #se puede agregar objetos de diferente tipo
print(miLista)   

miLista.remove(5)   #remover valor del parametro de la lista
print(miLista,"se removio 5")

miLista.pop()   #regresa el ultimo valor de la lista y lo remueve
print(miLista,"se removio el ultimo elemento")

miLista.extend([1,5,2,3])
miLista.sort()   #ordena la Lista
print(miLista,"se ordeno la lista")