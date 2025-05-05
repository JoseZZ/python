
class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("rojo", "canario")
otro_pajaro = Pajaro("azul", "loro")

print(f"Mi pájaro es de color {mi_pajaro.color} y es un {mi_pajaro.especie}.")
print(f"Otro pájaro es de color {otro_pajaro.color} y es un {otro_pajaro.especie}.")
print(f"Mi pájaro tiene alas: {mi_pajaro.alas}.")
print(f"Otro pájaro tiene alas: {otro_pajaro.alas}.")
