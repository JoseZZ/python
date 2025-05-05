class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Muuuuuuuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Beeeeeee")


vaca1 = Vaca("Jacinta")
oveja1 = Oveja("Marta")

animales = [vaca1, oveja1]
# Polimorfismo
for animal in animales:
    animal.hablar()

def animal_hablar(animal):
    animal.hablar()

animal_hablar(vaca1)
animal_hablar(oveja1)

