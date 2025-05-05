def mi_funcion():
    return 4


def mi_generador():
    yield 4

print(mi_funcion())
print(mi_generador())

gen = mi_generador()
print(next(gen))

def mi_lista():
    lista = []
    for i in range(1,5):
        lista.append(i * 10)
    return lista

def mi_generador_lista():
    for i in range(1,5):
        yield i * 10

print(mi_lista())
print(mi_generador_lista())
gen = mi_generador_lista()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def otro_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

gen = otro_generador()
print(next(gen))
print(next(gen))
print(next(gen))

