from random import shuffle


palitos = ["-","--","---","----","-----"]

def mezclar(lista):
    """
    Mezcla una lista de elementos.
    """
    shuffle(lista)
    return lista

def probar_suerte():
    """
    Probar suerte con una lista de palitos.
    """
    intento = ""
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un número entre 1 y 4: ")

    return int(intento)

def chequear_intento(lista, intento):
    """
    Chequear si el intento es correcto.
    """
    if lista[intento - 1] == "-":
        print("A lavar los platos")
    else:
        print("Te has salvado")

    print("Te ha tocado el palito: ", lista[intento - 1])


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)


