def decorar_turno(funcion):
    """
    Decorador que imprime un saludo antes de ejecutar la funcion.
    :param funcion: Funcion a decorar
    :return: Funcion decorada
    """

    def funcion_decorada(turno):
        print(f"Su turno es: ")
        funcion(turno)
        print("Espere y sera atendido")

    return funcion_decorada


@decorar_turno
def turno_perfumeria(turno):
    print(f"P-{turno}")


def generar_perfumeria():
    x = 1
    while True:
        yield x
        x += 1


@decorar_turno
def turno_farmacia(turno):
    print(f"F-{turno}")


def generar_farmacia():
    x = 1
    while True:
        yield x
        x += 1


@decorar_turno
def turno_cosmetica(turno):
    print(f"C-{turno}")


def generar_cosmetica():
    x = 1
    while True:
        yield x
        x += 1
