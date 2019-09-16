
lista = []
for i in range(100000):
    #lista = lista + [i] # aproximadamente 21 segundos
    #lista.append(i) #menos de un segundo
    pass

def secFibonacci(n):
    n1 = 0
    n2 = 1
    if(n==1 or n==0):
        return n
    for i in range(2,n+1,1):
        nEsimo = n1 + n2 
        n1 = n2
        n2 = nEsimo
        if(n==i):
            return nEsimo

def Rec2Fibonacci(n):
    n = int(n)
    if(n==1 or n==0):
        return n
    elif(n>1):
        return Rec2Fibonacci(n-1) + Rec2Fibonacci(n-2)
    else:
        return False
'''
print(Rec2Fibonacci(35)) #9 segundos
print(Rec2Fibonacci(37)) #22 segundos
print(Rec2Fibonacci(40)) #91 segundos
print(Rec2Fibonacci(1000000)) #muchooos segundos

print(secFibonacci(35)) #menos de 1 segundo
print(secFibonacci(37)) #menos de 1 segundo
print(secFibonacci(40)) #menos de 1 segundo
print(secFibonacci(1000000)) #12 segundos
'''

def metodo1(n):
    suma = 0
    for i in range(n+1):
        suma +=i 
    return suma
n=0
y = 5


def search(value,matrix):
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            if(value == matrix[i][j]):  return True
    else:   return False


matriz = [[1,2],[4,3]]
print(search(5,matriz))