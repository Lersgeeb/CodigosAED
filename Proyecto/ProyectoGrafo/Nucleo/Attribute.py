# -*- coding: utf-8 -*-
class Attribute:
    def __init__(self,distance = 0 , bandWidth = 0 ,users = 0 ,traffic = 0 ,mediaType = "undefined"):
        self.distance = int(distance)
        self.bandWidth = int(bandWidth)
        self.users = int(users)
        self.traffic = int(traffic)
        self.mediaType = mediaType
        

    def getWeight(self):
        '''
        N : cantidad de disminucion respecto a la distancia 
        CX : confiabilidad de acuerdo al tipo de medio 
        AB : Ancho de Banda
        CU : Cantidad de usuarios
        CT : Cantidad de Trafico
        CDM : Confiabilidad neta
        DC : Disminucion de confiabilidad
        LD : Limite de distancia para la disminucion
        '''
        CX,DC,LD = self.getConstant()
        CDM = self.confiabilitybyDistance(CX,DC,LD)
        weight = int ( self.users*self.traffic - self.bandWidth*CDM)

        if(self.getConstant != (0,0,0)):
            return weight
        else:
            return self.distance


    def confiabilitybyDistance(self,confiability,downConfiablity,limitDistance):
        N = self.distance//limitDistance
        CX = confiability
        CDM = CX * (1 - downConfiablity*(N))
        return CDM

    def getConstant(self):
        if(self.mediaType=="CAT5"):
            return (0.98,0.02,50)
        elif(self.mediaType=="CAT6"):
            return (0.98,0.01,50)
        elif(self.mediaType=="Fibra-Óptica"):
            return (0.9,0.05,100)
        elif(self.mediaType=="WIFI"):
            return (0.7,0.06,6)
        elif(self.mediaType=="Coaxial"):
            return (1,0.04,100)
        elif(self.mediaType=="Par-Trenzado"):
            return (1,0.01,100)
        else:
            return (0,0,1)  

'''
•CAT5: confiabilidad 0.98.
•CAT6: confiabilidad 0.98.
•Fibra-Óptica: confiabilidad 0.90.
•WIFI: 0.7.
•Coaxial: 1.
•Par-Trenzado: 1.
•***:
•CAT5: disminuye 0.02% de confiabilidad por cada 50 metros.
•CAT6: disminuye 0.01% de confiabilidad por cada 50 metros.
•Fibra-Óptica: disminuye 0.05% de confiabilidad por cada 100 metros.
•WIFI: disminuye 0.6% de confiabilidad por cada 6 metros.
•Coaxial: disminuye 0.04% de confiabilidad por cada 100 metros.
•Par-Trenzado: disminuye 0.01% de confiabilidad por cada 100 metros.
'''