from path_lib import Path

# Create a Path object
carpeta = Path('C:/Datos/formacion/python/udemy/carpeta_prueba')
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

