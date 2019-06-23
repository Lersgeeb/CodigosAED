class Dog:
   
    def __init__(self, nombre, dia, mes, año, ladrido):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes
        self.año = año
        self.ladrido = ladrido

    def getLadrido(self):

        return self.ladrido
       
    def setLadrido(self,ladrido):
        msg = "\nCambiando ladrido a " + self.nombre + "...\n"
        print(msg)
        self.ladrido=ladrido
        

    def getCumple(self):
        cadena = str(self.dia) + "/" + str(self.mes) + "/" + str(self.año)

        return cadena

    def getNombre(self):

        return self.nombre

    def __str__(self):
        cadena = "Nombre: " + self.getNombre() + " - Cumpleaños: " + self.getCumple() + " - Ladrido: " + self.getLadrido()
        
        return cadena    

    def __add__(self, otherDog):
        
        return Dog("Puppy of " + self.nombre + " and " + otherDog.nombre, \
        self.mes, self.dia, self.año + 1, \
        self.ladrido + otherDog.ladrido)

def main():

    print("\nEjecucion...\n")
    perro1 = Dog("Rockie", 20, 12, 2018, "guau!")
    perro2 = Dog("Arcoiris", 24, 9, 2017, "woooof")

    print(perro1)
    print(perro2)

    perro1.setLadrido("ruaaaaaar!")
    print(perro1)

    perro3 = perro1 + perro2
    print(perro3)


if __name__ == "__main__":
    main()