import numeros

def inicio():
    eleccion = 0
    perfumeria = numeros.generar_perfumeria()
    farmacia = numeros.generar_farmacia()
    cosmetica = numeros.generar_cosmetica()
    while eleccion != 4:
        imprimir_menu()
        try:
            eleccion = int(input("Por favor, elige una opción: "))
            if eleccion == 1:
                print("Bienvenido a la sección de Perfumería")
                numeros.turno_perfumeria(next(perfumeria))
            elif eleccion == 2:
                print("Bienvenido a la sección de Farmacia")
                numeros.turno_farmacia(next(farmacia))
            elif eleccion == 3:
                print("Bienvenido a la sección de Cosmética")
                numeros.turno_cosmetica(next(cosmetica))
            elif eleccion == 4:
                print("Gracias por su visita. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intentalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
        else:
            sigue = continuar()
            if not sigue:
                print("Gracias por su visita. ¡Hasta luego!")
                break

def imprimir_menu():
    print("*****************************************")
    print("¿A que sección desea ir?")
    print("*****************************************")
    print("1. Perfumeria")
    print("2. Farmacia")
    print("3. Cosmetica")
    print("4. Salir")
    print("*****************************************")

def continuar():
    while True:
        continuar = input("¿Desea coger otro turno? (s/n): ").lower()
        if continuar == 's':
            return True
        elif continuar == 'n':
            return False
        else:
            print("Opción no válida. Por favor, introduce 's' o 'n'.")

inicio()