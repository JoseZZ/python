# elegir palabra al azar
def elegir_palabra():
    import random
    lista = ["silla", "pelota", "tulipan", "mesa", "gato", "tomate", "perro", "raton", "cama", "casa"]
    palabra = random.choice(lista)
    return palabra


# mostrar guiones
def mostrar_guiones(palabra, letras_usadas):
    guiones = []
    for letra in palabra:
        if letra in letras_usadas:
            guiones.append(letra)
        else:
            guiones.append("_")
    print(" ".join(guiones))
    print("\n")


# pedir letra
def pedir_letra():
    letras_validas = "abcdefghijklmnopqrstuvwxyz"
    letra = " "
    while letra not in letras_validas:
        letra = input("Ingresa una letra: ")
        letra.lower()
    return letra


# comprobar ganador
def comprobar_ganador(palabra, letras_usadas):
    for letra in palabra:
        if letra not in letras_usadas:
            return False
    return True


# comparar letra con palabra

letras_usadas = []
vidas = 6
palabra = elegir_palabra()

mostrar_guiones(palabra, letras_usadas)

while vidas > 0:
    elegida = pedir_letra()
    while elegida in letras_usadas:
        print(f"Ya has usado esa letra: {letras_usadas}")
        elegida = pedir_letra()

    letras_usadas.append(elegida)

    if elegida in palabra:
        print(f"La letra '{elegida}' está en la palabra")
        if comprobar_ganador(palabra, letras_usadas):
            print(f"Has ganado! La palabra era '{palabra}'")
            break
    else:
        print(f"La letra '{elegida}' no está en la palabra")
        vidas -= 1
        print(f"Te quedan {vidas} vidas\n")
    if vidas == 0:
        print("Has perdido")
        print(f"La palabra era '{palabra}'")

    print(f"Has usado las siguientes letras: {letras_usadas}")
    mostrar_guiones(palabra, letras_usadas)
