class Node:

    def __init__(self,value):
        self.value = value

# -*- coding: utf-8 -*-
# coding en python
import random
import math
'''
#importar math,random y su uso
al=random.random()
print(al)
print(math.floor(al))

num = math.floor((al*(100-0) + 0))
print(num)


#Agregar informacion (input)
sum = input("cual es tu nombre?" )
print("mucho gusto %s" % (sum,))

print("cual es tu edad?")
age = input()
print("%s años" % (age,))

'''
#join y split
miNums = ["1","2","3","4","5","6","7"]
miNums2 = [1,2,3,4,5,6,7]
mistr = " - ".join(miNums)
print(mistr)

newArr = mistr.split(" - ")
print(newArr)

#typeof de py
a = Node(1)
print(isinstance(a,object))
hola = "hola"
#del hola 
print(hola)

arr2 = []
