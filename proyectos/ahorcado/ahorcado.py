import random


def get_word():
    lista_palabras = []
    with open("peliculas.txt", "r") as archivo_palabras:
        for line in archivo_palabras:
            palabra = line.strip().upper()
            if palabra:
                lista_palabras.append(palabra)

    return random.choice(lista_palabras)


def dibujar_ahorcado(intentos):
    partes = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
    print(partes[6 - intentos])


def ahorcado():
    palabra = get_word()
    letras_palabra = set(palabra)  # Convertir la palabra a un conjunto para verificar letras
    abecedario = set("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    letras_adivinadas = set()
    letras_usadas = set()
    intentos = 6
    print("¡Bienvenido al juego del Ahorcado!")
    print("Tienes", intentos, "intentos para adivinar la pelicula o el personaje infantil.")

    while intentos > 0 and letras_palabra != letras_adivinadas:
        # Mostrar el estado actual de la palabra
        print("Has usado las letras:", ", ".join(sorted(letras_usadas)))
        mostrar_palabra = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        print("Palabra:", " ".join(mostrar_palabra))

        letra = input("Introduce una letra (presiona Enter para continuar): ").upper()
        if letra in abecedario - letras_usadas:
            letras_usadas.add(letra)
            if letra in letras_palabra:
                letras_adivinadas.add(letra)
                print("¡Correcto!\n")
            else:
                intentos -= 1
                print("Incorrecto. Te quedan", intentos, "intentos.\n")
                dibujar_ahorcado(intentos)
        elif letra in letras_usadas:
            print("Ya has usado esa letra. Intenta con otra.")
        else:
            print("Entrada inválida. Por favor, introduce una letra del abecedario.\n")

    if letras_palabra == letras_adivinadas:
        print("¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        print("Lo siento, has perdido. La palabra era:", palabra)


ahorcado()
