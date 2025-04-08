from random import randint


def lanzar_dados():
    dado1 = randint(1, 7)
    dado2 = randint(1, 7)
    return [dado1, dado2]


def evaluar_jugada(res1, res2):
    suma = res1 + res2
    if suma <= 6:
        return f"La suma de tus dados es {suma}. Lamentable"
    elif 6 < suma < 10:
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"


resultados = lanzar_dados()
print(resultados)
cadena = evaluar_jugada(resultados[0], resultados[1])

print(cadena)