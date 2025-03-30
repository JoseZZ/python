monedas = 5

while monedas > 0:
    print(f"Te quedan {monedas} monedas")
    monedas -= 1
else:
    print("No te quedan monedas")

respuesta = "s"
while respuesta == "s":
    respuesta = input("Quieres seguir jugando? s/n: ")
else:
    print("Fin del juego")

nombre = input("Dime tu nombre: ")

for letra in nombre:
    if letra == "a":
        print("La letra a ha sido encontrada")
        break
    elif letra == "e":
        continue
    else:
        print(letra)
