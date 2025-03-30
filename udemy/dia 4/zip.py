nombres = ["Federico", "Juan", "Carlos", "Maria", "Jose"]
edades = [20, 30, 40, 50, 60]
ciudades = ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "La Plata"]

combinados = list(zip(nombres, edades))
print(combinados)

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")