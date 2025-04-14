archivo = open("prueba1.txt", "w")

#archivo.write("Hola mundo\n")
archivo.writelines(['hola ', 'como ', 'estás\n'])


archivo.close()

archivo = open("prueba1.txt", "a")
archivo.write("Hola mundo\n")



archivo.close()


