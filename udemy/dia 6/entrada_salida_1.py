mi_archivo = open("prueba.txt")
print(type(mi_archivo))
print(mi_archivo)

#print( mi_archivo.read())


#linea = mi_archivo.readline()
#print(linea)
#linea = mi_archivo.readline()
#print(linea.rstrip())
#linea = mi_archivo.readline()
#print(linea)

#for linea in mi_archivo:
 #     print("Aquí hay una línea del archivo: " + linea)

todas = mi_archivo.readlines()
print(todas)



mi_archivo.close()


