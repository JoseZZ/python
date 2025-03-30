lista = ["a", "b", "c"]
indice = 0

for item in enumerate(lista):
    print(item)
    print(item[0])
    print(item[1])

for valor in enumerate(range(50,56)):
    print(valor)
    print(valor[0])
    print(valor[1])

mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1][0])