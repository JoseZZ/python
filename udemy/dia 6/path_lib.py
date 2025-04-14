from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Datos/formacion/python/udemy/carpeta_prueba/otro_archivo.txt')

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.stem)
print(carpeta.suffix)
print(carpeta.parent)
print(carpeta.is_file())
print(carpeta.is_dir())
print(carpeta.exists())


ruta_windows = PureWindowsPath('C:/Datos/formacion/python/udemy/carpeta_prueba/otro_archivo.txt')
print(ruta_windows)

