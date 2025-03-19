mi_lista = ["a", "b", "c"]
otra_lista = ["Hola", 55, 23, 45.3, "Adios"]

print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[0])
print(mi_lista[-1])
print(mi_lista[0:2])
lista3 = mi_lista + otra_lista
print(lista3)
print(mi_lista * 3)

lista3[0] = "zeta"
print(lista3)
lista3.append("Hola")
print(lista3)

eliminado = lista3.pop()
print(eliminado)
print(lista3)
lista3.pop(2)
print(lista3)

lista_caracteres = ['r', 'y', 'f', 'a', 'e', 'l', 'z', 'x', 'c', 'b']
lista_caracteres.sort()
print(lista_caracteres)

lista_numeros = [3, 5, 1, 6, 8, 2, 4, 7]
lista_numeros.reverse()
print(lista_numeros)

