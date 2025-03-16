nombre = input("Introduce tu nombre:")
ventas = input("Introduce cuanto has vendido este mes:")

comisiones = (float(ventas) * 13) / 100

print("Hola " + nombre + ", tus comisiones son de: " + str(round(comisiones, 2)))