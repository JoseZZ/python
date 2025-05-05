import shutil

carpeta_origen = "C:\\Users\\pepec\\Desktop\\Carpeta test"
archivo_destino = "Todo_comprimido"

shutil.make_archive(archivo_destino, "zip", carpeta_origen)

shutil.unpack_archive("Todo_comprimido.zip", "Carpeta extraida", "zip")
