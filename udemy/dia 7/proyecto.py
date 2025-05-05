class Persona:
    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    # Constructor
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        # Llamada al constructor de la clase padre
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # Método público
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Número de cuenta: {self.numero_cuenta}, Balance: {self.balance}"

    def depositar(self, monto):
        self.balance += monto
        print(f"Deposito de {monto} realizado. Nuevo balance: {self.balance}")

    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto
            print(f"Retiro de {monto} realizado. Nuevo balance: {self.balance}")
        else:
            print("Fondos insuficientes para realizar el retiro.")

def inicio():
    opcion = 0
    while opcion != 4:
        print("1. Crear cliente")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cliente = crear_cliente()
            print(cliente)
        elif opcion == 2:
            monto = float(input("Ingrese el monto a depositar: "))
            cliente.depositar(monto)
            print(f"El balance actual es: {cliente.balance}")
        elif opcion == 3:
            monto = float(input("Ingrese el monto a retirar: "))
            cliente.retirar(monto)
            print(f"El balance actual es: {cliente.balance}")
        elif opcion == 4:
            print("Saliendo del programa.")
        else:
            print("Opción no válida. Intente nuevamente.")


def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    balance = float(input("Ingrese el balance inicial: "))
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente

inicio()

