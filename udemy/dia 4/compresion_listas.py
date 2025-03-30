palabra = "Python"

lista = [letra for letra in palabra]
print(lista)

numeros = [numero for numero in range(0, 20, 2)]
print(numeros)

lista_numeros = [numero / 2 for numero in range(0, 20)]
print(lista_numeros)

lista_numeros = [numero for numero in range(0, 20) if numero % 2 == 0]
print(lista_numeros)

lista_numeros = [numero if numero % 2 != 0 else "no" for numero in range(0, 20)]
print(lista_numeros)

pies = [10, 20, 30, 40, 50]
metros = [pie * 0.3048 for pie in pies]
print(metros)
