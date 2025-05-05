
class Animal:

    def __init__(self, edad, color):
        print("El animal ha sido creado")
        self.edad = edad
        self.color = color

    def nacer(self ):
        print("El animal ha nacido")

class Pajaro(Animal):
    pass

print(Animal.__subclasses__())

piolin = Pajaro(16, "amarillo")
piolin.nacer()
print(piolin.color)


