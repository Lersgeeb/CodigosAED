def printList(lista,tab = 0):

    for value in lista:
        if(isinstance(value, list)):         
            printList(value,tab+1)
        else:
            print(("%s%s" % ("\t"*tab,value)))

lista = [1,2,[2.4,"2.6",[2.66,2.88]],3,4,5]
printList(lista)