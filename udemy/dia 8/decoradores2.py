
def decorar_saludo(funcion):
    """
    Decorador que imprime un saludo antes de ejecutar la funcion.
    :param funcion: Funcion a decorar
    :return: Funcion decorada
    """
    def funcion_decorada(palabra):
        print("Hola, soy un decorador")
        funcion(palabra)
    return funcion_decorada

def mayusculas(texto):
    """
    Cambia el texto a mayúsculas.
    :param texto: Texto a cambiar
    :return: Texto en mayúsculas
    """
    print(texto.upper())

def minusculas(texto):
    """
    Cambia el texto a minúsculas.
    :param texto: Texto a cambiar
    :return: Texto en minúsculas
    """
    print(texto.lower())

minusculas("Hola Mundo")
mayusculas("Hola Mundo")

@decorar_saludo
def mayusculas_decorada(texto):
    """
    Cambia el texto a mayúsculas.
    :param texto: Texto a cambiar
    :return: Texto en mayúsculas
    """
    print(texto.upper())

@decorar_saludo
def minusculas_decorada(texto):
    """
    Cambia el texto a minúsculas.
    :param texto: Texto a cambiar
    :return: Texto en minúsculas
    """
    print(texto.lower())

mayusculas_decorada("Hola Mundo")
minusculas_decorada("Hola Mundo")

mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula_decorada("Hola Mundo")

