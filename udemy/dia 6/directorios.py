import os

ruta = os.getcwd()
print(ruta)

#os.chdir("C:\\Datos\\formacion\\python\\udemy\\carpeta_prueba")
#archivo = open("otro_archivo.txt", "r")
#print(archivo.read())

os.mkdir("C:\\Datos\\formacion\\python\\udemy\\carpeta_prueba\\dentro")

ruta = "C:\\Datos\\formacion\\python\\udemy\\carpeta_prueba\\otro_archivo.txt"

elemento = os.path.basename(ruta)
print(elemento)
directorio = os.path.dirname(ruta)
print(directorio)
tupla = os.path.split(ruta)
print(tupla)

os.rmdir("C:\\Datos\\formacion\\python\\udemy\\carpeta_prueba\\dentro")









