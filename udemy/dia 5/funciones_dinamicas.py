def chequear_3_cifras(numero):
    """
    Esta función verifica si un número tiene 3 cifras.
    :param numero: Número a verificar.
    :return: True si el número tiene 3 cifras, False en caso contrario.
    """
    return numero in range(100, 1000)

resultado = chequear_3_cifras(123)
print(resultado)

def chequear_3_cifras(lista):
    lista_3_cifras = []
    for numero in lista:
        if numero in range(100, 1000):
            print(f"El número {numero} tiene 3 cifras")
            lista_3_cifras.append(numero)
        else:
            print(f"El número {numero} no tiene 3 cifras")
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([15, 23, 3767, 4657, 500])
print(resultado)