import zipfile

mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")
mi_zip.write("texto_a.txt")
mi_zip.write("texto_b.txt")
mi_zip.close()

zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")
print(zip_abierto.namelist())
zip_abierto.extractall()
