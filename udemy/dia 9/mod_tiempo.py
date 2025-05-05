import time

def prueba_for(numero):
    lista = []
    for i in range(1, numero + 1):
        lista.append(i)
    return lista

def prueba_while(numero):
    lista = []
    i = 1
    while i <= numero:
        lista.append(i)
        i += 1
    return lista

inicio = time.time()
print(inicio)
prueba_for(1500000)
final = time.time()
print(f"Tiempo de ejecución con for: {final - inicio} segundos")

inicio = time.time()
prueba_while(1500000)
final = time.time()
print(f"Tiempo de ejecución con while: {final - inicio} segundos")

