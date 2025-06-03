import os
import re
import time
import math
from datetime import datetime


def buscar_serie(archivo):
    patron = r"N\w{3}-\d{5}"
    file = open(archivo, "r")
    contenido = file.read()
    busqueda = re.search(patron, contenido)
    file.close()
    if busqueda:
        return busqueda.group()
    else:
        return None


def current_date():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def buscar_en_archivos():
    cuantos_archivos = 0
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")
    ruta = "Mi_Gran_Directorio"
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            archivo = os.path.join(carpeta, arch)
            serie = buscar_serie(archivo)
            if serie:
                print(f"{arch}\t{serie}")
                cuantos_archivos += 1

    return cuantos_archivos


print("----------------------------------------------------")
print(f"Fecha de búsqueda: {current_date()}")
inicio = time.time()
cuantos_encontrados = buscar_en_archivos()
final = time.time()
print(f"\nNúmeros encontrados: {cuantos_encontrados}")
print(f"Duración de la búsqueda: {math.ceil((final - inicio) * 1000)} segundos")
print("----------------------------------------------------")

