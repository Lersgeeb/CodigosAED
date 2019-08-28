import random

#para crear un arreglo de i tamaño en una sola linea
ar = [i for i in range(0,4)]
#print(a)

#para crear un arreglo de i tamaño con numeros aleatorios 
randomArray =  [int(random.random()*100) for i in range(0,7)]
#print(randomArray)

#para crear un matriz cuadrada de n tamaño con 0 
n=4
matrizVacia = [[0 for j in range(0,n)] for i in range(0,n)]
#print(matrizVacia)

#para crear un matriz cuadrada de n tamaño con valores variantes
matriz = [[i+j for j in range(0,n)] for i in range(0,n)] 
#print(matriz)

'''
map(funcion,elemento*)  : Procesar "de una vez" cada elemento de un Arreglo
lambda parametro:resultado  : Hacer una funcion de una linea
'''

#1 - Ejercicio convertir [1,2,3,4] a [2,3,4,5] 
def sumArray(x):
    return x+1

arrayConverted1 = list(map(sumArray,[i for i in range(1,5)]))
#print(arrayConverted1)

#2 - Ejercicio convertir [1,2,3,4] a [2,3,4,5] con lambda
arrayConverted2 = list(map(lambda x:x+1,[i for i in range(1,5)]))
#print(arrayConverted2)

#3 - Ejercicio Crear matriz 4x4 de 0 en una linea
matrizVacia4x4 = [[0 for j in range(0,4)] for i in range(0,4)]
#print(matrizVacia4x4)

#4 - Ejercicio Crear matriz 4x4 de valores random en una linea
matrizRandom4x4 = [[int(random.random()*100) for j in range(0,4)] for i in range(0,4)]
#print(matrizRandom4x4)

#5 - Ejercicio sumar las anteriores dos matrices en una sola linea
matrizSum = list(map(lambda x,y:list(map(lambda a,b:a+b, x,y)),matrizVacia4x4,matrizRandom4x4))
print("Matriz Vacia: %s\nMatriz Random: %s\n\nMatriz Sumada: %s\n" % (matrizVacia4x4,matrizRandom4x4,matrizSum))
