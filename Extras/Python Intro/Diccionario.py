capitales = {"Honduras":"Tegucigalpa", "Francia":"Paris", "Espania":"Madrid"}
print("Mi diccionario:",capitales)
print(capitales["Honduras"])
print(capitales.keys()) #imprime solo los enunciados
print(capitales.values())   #imprime solo los valores de todos los enunciados
print(len(capitales))   #imprime la longitud del diccionario

capitales["Italia"] = "Roooooma"    #Agregar valor al Diccionario
print(capitales) 

capitales["Italia"] = "Roma"    #Sobrescribir valor existente
print(capitales)

del capitales["Francia"]    #Borrar valor en el diccionario
print(capitales)

jugadores = {"Messi":10,"Cristiano":7,"Iniesta":8 , "Yo":"sin numero"}
print(jugadores)

miTupla = ("Usa","Inglaterra","Honduras")
capitalesConDupla = {miTupla[0]:"Washington",miTupla[1]:"Londres",miTupla[2]:"Tegucigalpa"}
print(capitalesConDupla)

jgChamp ={"Nombre":"Messi", "Equipo":"Barcelona", "Champions":{"temporadas":[2006,2009,2011,2015]}}#Se pueden agregar Dic
print(jgChamp)                                                                                     #dentro de otros Dic.
print(jgChamp["Champions"])
