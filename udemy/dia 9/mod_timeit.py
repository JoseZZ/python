import timeit


def prueba_while(numero):
    lista = []
    i = 1
    while i <= numero:
        lista.append(i)
        i += 1
    return lista


declaracion = """
prueba_for(10)
"""
setup = """
def prueba_for(numero):
    lista = []
    for i in range(1, numero + 1):
        lista.append(i)
    return lista
"""

duracion = timeit.timeit(declaracion, setup, number=1000000)
print(duracion)

declaracion2 = """
prueba_while(10)
"""
setup2 = """
def prueba_while(numero):
    lista = []
    i = 1
    while i <= numero:
        lista.append(i)
        i += 1
    return lista
"""

duracion2 = timeit.timeit(declaracion2, setup2, number=1000000)
print(duracion2)
