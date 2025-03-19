mi_tuple = (1, 2, 3, 4)
print(type(mi_tuple))
otra_tuple = 1, 2, 3, 4
print(type(otra_tuple))

tupla = (1, "hola", [1, 2, 3], 4.9, (10, 20))
print(tupla[1])
print(tupla[2][1])
print(tupla[4][1])

tupla = list(tupla)
print(type(tupla))
tupla = tuple(tupla)
print(type(tupla))

tupla = (1, 2, 1)
x, y, z = tupla
print(x, y, z)
print(len(tupla))

print(tupla.count(1))
print(tupla.index(2))


