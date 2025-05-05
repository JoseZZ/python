
class Pajaro:
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros.")

piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(10)

