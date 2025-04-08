def sumar(**kwargs):
    print(type(kwargs))
    total = 0
    for num in kwargs.values():
        total += num
    return total


def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"La clave es {clave} y el valor es {valor}")
        total += valor
    return total


def suma_combinar(num1, num2, *args, **kwargs):
    print(f"El primer numero es {num1}")
    print(f"El segundo numero es {num2}")
    for arg in args:
        print(f"El argumento es {arg}")
    for clave, valor in kwargs.items():
        print(f"La clave es {clave} y el valor es {valor}")


print(sumar(a=1, b=2, c=3, d=4, e=5))
print(suma(a=1, b=2, c=3, d=4, e=5))
print(suma_combinar(14, 26, 326, 64, 25, a="uno", b="dos", c="tres"))

lista_argumentos = [10, 20, 30, 40, 50]
lista_kargumentos = {"a": "uno", "b": "dos", "c": "tres"}
suma_combinar(15,58, *lista_argumentos, **lista_kargumentos)

