if(True):
    print("Esto es verdadero")

if(False):
    print("Esto es verdadero")   
else:
    print("Esto es falso")    

num=1
if(num==0):
    print("Numero = 0")
elif(num==1):
    print("Numero = 1")
else:
    print("Numero != 0 o 1")

keep=0
while(keep < 3):
    
    print("keep es" , str(keep))
    keep +=1       

myList =[(1,2),(3,4),(5,6),(7,8)]
for (a,b) in myList:
    print(a)
    print(b)

miDic ={"k1":1,"k2":2,"k3":3}
for item in miDic:
    print(item) #solo se imprimira la declaracion(key)

for value in miDic.values():
    print(item) #solo se imprimira el valor(value)

for d in miDic.items():
    print(d) #imprimira la declaracion(key) y el valor(value)

for (item,value) in miDic.items():
    print(item) #imprimira la declaracion(key) 
    print(value) #imprimira el valor(value)
