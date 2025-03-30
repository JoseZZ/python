mascota = "perro"

if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
elif mascota == "pez":
    print("Tienes un pez")
else:
    print("No tienes ni un perro ni un gato")

edad = 16
calificacion = 9

if edad < 18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobaste el curso")
    else:
        print("Reprobaste el curso")
else:
    print("Eres mayor de edad")
    