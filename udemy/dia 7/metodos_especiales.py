
mi_lista = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

print(len(mi_lista))

class CD:
    def __init__(self, artista, album, anio, canciones):
        self.artista = artista
        self.album = album
        self.anio = anio
        self.canciones = canciones

    def __str__(self):
        return f"{self.artista} - {self.album} - {self.anio} - {self.canciones}"

    def __len__(self):
        return len(self.canciones)

    def __del__(self):
        print("Eliminando objeto CD")

mi_cd = CD("Metallica", "Master of Puppets", 1986, ["Battery", "Master of Puppets", "The Thing That Should Not Be"])
print(mi_cd)
print(len(mi_cd))
del mi_cd
