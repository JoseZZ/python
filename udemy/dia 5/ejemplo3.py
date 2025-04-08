from random import *


def lanzar_moneda():
    tirada = choice(["Cara", "Cruz"])
    return tirada


def probar_suerte(tirada, numeros):
    if tirada == "Cara":
        print(f"La lista se autodestruirá")
        numeros.clear()
    else:
        print(f"La lista fue salvada")
    return numeros


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
tirada = lanzar_moneda()
lista = probar_suerte(tirada, lista_numeros)
print(lista)


