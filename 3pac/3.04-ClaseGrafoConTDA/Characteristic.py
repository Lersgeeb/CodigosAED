class Characteristic:
    def __init__(self,prueba = 0,distance = 0 , bandWidth = 0 ,users = 0 ,traffic = 0 ,mediaType = "undefined"):
        self.distance = distance
        self.bandWidth = bandWidth
        self.users = users
        self.traffic = traffic
        self.mediaType = mediaType
        self.prueba = prueba

    def getWeight(self):
        return self.prueba