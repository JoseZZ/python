from random import randint

numero = randint(1,101)

print("Adivina el numero entre 1 y 100 en 8 intentos o menos")
encontrado = False
contador = 1

while contador <= 8:
    eleccion = int(input("Introduce un numero: "))
    if eleccion < 1 or eleccion > 100:
        print("El numero debe estar entre 1 y 100")
    elif eleccion < numero:
        print("El numero es mayor")
    elif eleccion > numero:
        print("El numero es menor")
    else:
        print(f"Enhorabuena! Has acertado en el intento {contador}")
        encontrado = True
        break

    contador += 1

if not encontrado:
    print("\nFin del juego")
    print(f"El numero era {numero}")



