class Animal:

    def __init__(self, edad, color):
        print("El animal ha sido creado")
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")

    def hablar(self):
        print("El animal habla")


class Pajaro(Animal):

    def __init__(self, edad, color,altura):
        print("El pájaro ha sido creado")
        super().__init__(edad, color)
        self.altura = altura

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")


print(Animal.__subclasses__())

mi_animal = Animal(5, "marrón")
piolin = Pajaro(16, "amarillo",39)
piolin.nacer()
print(piolin.color)
piolin.hablar()
piolin.volar(10)
