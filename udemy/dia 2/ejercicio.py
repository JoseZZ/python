nombre = input("Introduce tu nombre:")
ventas = input("Introduce cuanto has vendido este mes:")

comisiones = round((float(ventas) * 13) / 100, 2)

print(f"Hola {nombre}, tus comisiones son de: {comisiones} ")