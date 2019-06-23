miTupla = "Tupla1",1,2,3 # igual a poner ("Tupla",1,2,3)
print(miTupla)
miLista =list(miTupla) #crea una lista de la Tupla

miLista2 = ["Lista1",4,5,6] 
print(miLista2)
miTupla2 =tuple(miLista2) #crea una tupla de una lista

print("Cantidad de veces que 2 esta en la Tupla:",miTupla.count(2))#Cantidad de veces que se encuentra un elemento
print("lugar donde esta 2",miTupla.index(2))
print("longitud de Tupla",len(miTupla))#Longitud de la Tupla

tuplaUnitaria = 1, #igual a poner (1,)
print("longitud de Tupla unitaria",len(tuplaUnitaria))

tuplaPersona = ("Gabriel","Escobar",19) #Empaquetado de tupla
nombre, apellido, edad = tuplaPersona #Desempaquetado de tupla
print("Imprimiendo tupla", tuplaPersona)
print("Nombre:",nombre,"- Apellido:", apellido,"- Edad:", edad)