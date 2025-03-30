lista = ["a", "b", "c"]

for valor in lista:
    numero_de_letra = lista.index(valor)
    print(f"{valor} esta en la posicion {numero_de_letra}")

nombres = ["Federico", "Juan", "Carlos", "Maria", "Jose"]

for nombre in nombres:
    if nombre.startswith("J"):
        print(f"{nombre} empieza con J")

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

for a, b, c in [[1, 2, 3], [4, 5, 6]]:
    print(a)
    print(b)
    print(c)

dic = {"k1": "a", "k2": "b", "k3": "c"}

for clave, valor in dic.items():
    print(clave)
    print(valor)

for clave in dic.keys():
    print(clave)

for clave in dic.values():
    print(clave)

for a, b in dic.items():
    print(a, b)
