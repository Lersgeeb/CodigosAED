# -*- coding: utf-8 -*-
from Contact import *
from BST import * 
from Contact import *

def showMenu():
    
    mytree = BST()
    answer = 0

    contacto1 = Contact("Maria",0)
    contacto2 = Contact("Pedro",-2)
    contacto3 = Contact("Juan",-3)
    contacto4 = Contact("Carlos",-1)
    contacto5 = Contact("Jose",2)
    contacto6 = Contact("Jazmin",1)
    contacto7 = Contact("Daniel",3)

    mytree.add(contacto1)
    mytree.add(contacto2)
    mytree.add(contacto3)
    mytree.add(contacto4)
    mytree.add(contacto5)
    mytree.add(contacto6)
    mytree.add(contacto7)
    
    '''
    mytree.searchContact(0)
    mytree.remove(123)
    mytree.remove(0)
    mytree.searchContact(0)
    mytree.searchContact(3)
    ''' 

    while(answer != 4):
        print("\n-------MENU-------")
        print("1. Añadir Contacto\n2. Buscar Contacto\n3. Eliminar Contacto\n4. Salir\n")
        answer = int( input("Escoge una opcion\n") )
        
        if(answer==1):
            name = input("\nAgregar nombre del contacto que desea agregar\n")
            number =int( input("\nAgregar numero del usuario\n") )
            newContact = Contact(name,number)
            mytree.add(newContact)

        elif(answer==2):
            number =int( input("\nAgregar numero del usario para hacer la busqueda\n") )
            mytree.searchContact(number)
            
        elif(answer==3):
            number =int( input("\nAgregar numero del usario que desea eliminar\n") )
            mytree.remove(number)

        elif(answer==4):
            pass

        else:
            print("\nOpcion no disponible\n")