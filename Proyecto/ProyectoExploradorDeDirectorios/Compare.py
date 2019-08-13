class Compare:

    alphabet="/0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        pass
        
    def greaterLength(self,str1, str2):
        g = len(str1)
        if(len(str2) > g):
            g = len(str2)
       
        return g
            
    def lesserLength(self,str1, str2):
        l = len(str1)
        if(len(str2) < l):
            l = len(str2)
       
        return l
            
    def compare(self, object1, object2):
        
        if(isinstance(object1,int)):
            object1 = str(object1)

        if(isinstance(object1,str)):
            pass
        else:
            object1 = object1.name
        
        if(isinstance(object2,int)):
            object2 = str(object2)

        if(isinstance(object2,str)):
            pass
        else:
            object2 = object2.name

        lesser = self.lesserLength(object1,object2)
        for i in range(0,lesser,1):
            if(Compare.alphabet.index(object1[i]) > Compare.alphabet.index(object2[i])):
                return 1

            elif(Compare.alphabet.index(object1[i]) < Compare.alphabet.index(object2[i])):
                return -1
        if(lesser == self.greaterLength(object1,object2)):
            return 0

        elif(len(object1) == lesser):
            return -1

        else:
            return 1

