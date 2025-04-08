
def reducir_lista(lista):
    lista_nueva = []
    for numero in lista:
        if numero not in lista_nueva:
            lista_nueva.append(numero)
    mayor = max(lista_nueva)
    lista_nueva.pop(lista_nueva.index(mayor))
    return lista_nueva

def promedio(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)


lista_numeros = [1 ,2 ,15 ,7 ,2]

lista = reducir_lista(lista_numeros)
print(lista)
valor = promedio(lista)
print(valor)


