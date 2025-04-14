from path_lib import Path
import os
from os import system

guia = Path(Path.home(), 'Recetas')

def lista_recetas(carpeta):
    lista = []
    print(f"Recetas en {carpeta}:")
    for file in Path(guia, carpeta).glob("**/*.txt"):
        lista.append(file)
        print(os.path.basename(file))
    print("\n")
    return lista

def mostrar_menu():
    system("cls")
    print("Bienvenido al recetario")
    print(f"Tus recetas estan en: {guia}")
    recetas = lista_recetas(guia)
    print(f"Recetas disponibles: {len(recetas)}")
    print("*" * 50)
    print("[1] - Leer receta")
    print("[2] - Crear receta")
    print("[3] - Crear categoria")
    print("[4] - Eliminar receta")
    print("[5] - Eliminar categoria")
    print("[6] - Listar recetas")
    print("[7] - Finalizar programa")
    print("\n")


def pedir_receta(categoria):
    nombre_receta = input("Nombre de la receta: ")
    return Path(guia, categoria, nombre_receta)


def pedir_categoria():
    nombre_categoria = input("Nombre de la categoria: ")
    return Path(guia, nombre_categoria)

def mostrar_categorias():
    print("Categorias disponibles:")
    categorias = os.listdir(guia)
    for categoria in categorias:
        print(f"[{categoria}]")


opcion = 0

while opcion != 7:
    mostrar_menu()
    opcion = int(input("Elige una opción: "))
    if opcion < 1 or opcion > 7:
        print("Opción inválida, por favor elige una opción entre 1 y 6")
        continue
    if opcion == 1:
        print("Leer receta")
        mostrar_categorias()
        categoria = pedir_categoria()
        if not categoria.exists():
            print("Categoria no encontrada")
            continue
        lista_recetas(categoria)
        ruta_receta = pedir_receta(categoria)
        print(ruta_receta)
        if ruta_receta.exists():
            archivo = open(ruta_receta, "r")
            print(archivo.read())
        else:
            print("Receta no encontrada")
    elif opcion == 2:
        print("Crear receta")
        mostrar_categorias()
        categoria = pedir_categoria()
        if not categoria.exists():
            print("Categoria no encontrada")
            continue
        ruta_receta = pedir_receta(categoria)
        if not ruta_receta.exists():
            archivo = open(ruta_receta, "w")
            contenido = input("Contenido de la receta: ")
            archivo.write(contenido)
            print(f"Receta creada")
        else:
            print("Receta ya existe")
    elif opcion == 3:
        print("Crear categoria")
        ruta_categoria = pedir_categoria()
        if not ruta_categoria.exists():
            ruta_categoria.mkdir()
            print(f"Categoria creada")
        else:
            print("Categoria ya existe")
    elif opcion == 4:
        print("Eliminar receta")
        mostrar_categorias()
        categoria = pedir_categoria()
        if not categoria.exists():
            print("Categoria no encontrada")
            continue
        lista_recetas(categoria)
        ruta_receta = pedir_receta(categoria)
        if ruta_receta.exists():
            os.remove(ruta_receta)
            print(f"Receta eliminada")
        else:
            print("Receta no encontrada")
    elif opcion == 5:
        print("Eliminar categoria")
        mostrar_categorias()
        ruta_categoria = pedir_categoria()
        if ruta_categoria.exists():
            for archivo in ruta_categoria.glob("*"):
                os.remove(Path(ruta_categoria, archivo))
            os.rmdir(ruta_categoria)
            print(f"Categoria eliminada")
        else:
            print("Categoria no encontrada")
    elif opcion == 6:
        print("Listar recetas")
        lista_recetas(guia)





