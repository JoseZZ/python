serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("Serie no encontrada")

cliente = {"nombre": "Juan", "apellido": "Perez", "edad": 20, "peso": 60.5}

pelicula = {"titulo": "Titanic",
            "ficha_tecnica": {"director": "James Cameron", "duracion": 195}}

elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre, "apellido": apellido, "edad": edad, "peso": peso}:
            print("Es un cliente")
            print(nombre, apellido, edad, peso)
        case {"titulo": titulo, "ficha_tecnica": {"director": director, "duracion": duracion}}:
            print("Es una pelicula")
            print(titulo, director, duracion)
        case _:
            print("Tipo no encontrado")
