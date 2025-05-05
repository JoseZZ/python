
def suma():
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    resultado = n1 + n2
    print("El resultado de la suma es: ", resultado)

def pedir_numero():
    while True:
        try:
            n = int(input("Introduce un número: "))
            print("El número es: ", n)
        except:
            print("Eso no es un número")
        else:
            print(f"Has introducido el número {n}")

try:
    suma()
except ValueError:
    print("Estas intentando concatenar un string con un entero")
except TypeError:
    print("Estas intentando sumar un string con un entero")
else:
    print("No ha ocurrido ningún error")
finally:
    print("Fin de la función suma")


