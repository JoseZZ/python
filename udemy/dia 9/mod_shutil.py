import os
import shutil
import send2trash

print(os.getcwd())
archivo = open("curso.txt", "w")
archivo.write("Hola Mundo")
archivo.close()

print(os.listdir())
shutil.move("curso.txt", "C:\\Users\\pepec\\Desktop")

send2trash.send2trash("C:\\Users\\pepec\\Desktop\\curso.txt")

print(os.walk("C:\\Users\\pepec\\Desktop\\Carpeta test"))
ruta = "C:\\Users\\pepec\\Desktop\\Carpeta test"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Hay las subcarpetas: ")
    for sub in subcarpeta:
        print(f"Subcarpeta: \t{sub}")
    print(f"Los archivos son: ")
    for arch in archivo:
        print(f"Archivo: \t{arch}")
    print("-" * 20)


