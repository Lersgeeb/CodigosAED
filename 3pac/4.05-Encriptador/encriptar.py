#-*- coding: utf-8 -*-
"""
etimologia:
encryption: es el proeso de codigicar un mensaje o informacion de tal manera que solo las partes autorizadas puedan acceder a el
encoding: el proceso de codificiacion convierte

Cifrado Cesar
es un cirfrado po desplazamiento se encarga de mover cada letra una cantidad de caracteres
en el alfabeto puede ser n desplazamientos a la derecha o izquierda
en honor a julio cesar quien uso desplaza,miento de 3 espacios e.g ADA = DGD

Numero binarios
es el sistema de escritura y calculo usando numeros que usan solo 2 digitos para su numeracion (0 y 1)
Tiene 2 como base (unicamente cuenta con 2 digitos e.g base 10 con diez digitos, octal con 8 digitos 
Hexadecimal con 16 etc.)


Operaciones Binarias
las operaciones binarios convencionales son:
AND(representado por el simbolo & ampersand)
OR(representado por el simbolo )
NOT()
XOR
NAND
NOR

Principio basico:
cifrar 1 letra con una letra.
01000100 -> 68
11111011
10111011 utilizando XOR (XOR solo puede existir cuando uno es verdadero y otro es falso)
11111011
10111011
"""
#cifra
#a es la letra que queremos cifrar b es la contrasena
cifrado = chr(ord("a") ^ ord("b")) 
print(cifrado)

#descifra
descifrado = chr(ord(cifrado) ^ ord("b"))
print(descifrado)

phrase = "hola mundo"
password = "z"
print("plain text: %s" % phrase)

encripted = "".join(
    list(
        map(
            lambda x: chr(x ^ ord(password)),
            bytearray(phrase,'utf-8')
        )
    )
)
print("encripted text: %s" % encripted)

decrypted =  "".join(
    list(
        map(
            lambda x: chr(x ^ ord(password)),
            bytearray(encripted,'utf-8')
        )
    )
)

print("Decrypted text: %s" % decrypted)

class Encryptor:
    def __init__(self):
        pass


    def encrypt(self,phrase,password): #solo toma en cuenta el primer caracter de la contraseña
        return "".join(list(map(lambda x: chr(x ^ ord(password[0])),bytearray(phrase,'utf-8'))))

    def decrypt(self,encriptedtext,password):
        return self.encryptM(encriptedtext,password)
        
    def encryptM(self,phrase,password): #Toma en cuenta todas las letras de la contraseña
        encripted= []
        c = 0
        for i in bytearray(phrase,'utf-8'):
            encripted.append(chr( i ^ ord(password[c % len (password)])))
            c+=1
        
        return "".join(encripted)

 
e = Encryptor()
print(e.encrypt("Hola mundo","buenos dias"))
print(e.decrypt(e.encryptM("Hola mundo","buenos dias"),"buenas dias"))
