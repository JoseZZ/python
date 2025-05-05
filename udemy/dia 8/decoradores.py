
def mayuscula(texto):
    """
    Cambia el texto a mayúsculas.
    :param texto: Texto a cambiar
    :return: Texto en mayúsculas
    """
    print( texto.upper())

def minuscula(texto):
    """
    Cambia el texto a minúsculas.
    :param texto: Texto a cambiar
    :return: Texto en minúsculas
    """
    print(texto.lower())

mi_funcion = mayuscula
mi_funcion("Hola Mundo")

def una_funcion(funcion):
    return funcion

una_funcion(mayuscula("probando"))

def cambiar_letras(tipo):
    """
    Cambia el texto a mayúsculas o minúsculas.
    :param tipo: Tipo de cambio (mayusculas o minusculas)
    :return: Texto cambiado
    """
    def upper(texto):
        return texto.upper()

    def lower(texto):
        return texto.lower()

    if tipo == "may":
        return upper
    elif tipo == "min":
        return lower

operacion = cambiar_letras("may")
print(operacion("Hola Buenas Tardes"))

def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        print(f"El valor de retorno es {c}")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

print(suma(5,8))

