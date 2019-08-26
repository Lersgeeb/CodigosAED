def printDict(dct,tab=0):
     for k,v in dct.items():
        if(isinstance(v,dict)):
            print("%s%s" % ("\t"*(tab),k))
            printDict(v,tab+1)
        else:  
            print("%s%s : %s" % ("\t"*(tab),k,v))
            