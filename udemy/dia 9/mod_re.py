import re

texto = "Si necesitas ayuda llama al (658)-123-456 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra)

patron = "nada"
busqueda = re.search(patron, texto)
print(busqueda)

patron = "ayuda"
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

busqueda = re.findall(patron, texto)
print(busqueda)
print(len(busqueda))
for hallazgo in re.finditer(patron,texto):
    print(hallazgo)
    print(hallazgo.group())
    print(hallazgo.span())
    print(hallazgo.start())
    print(hallazgo.end())

texto = "Llama al 564-123-456 ya mismo"

patron= r"\d{3}-\d{3}-\d{3}"
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.group())

patron = re.compile(r"(\d{3})-(\d{3})-(\d{3})")
busqueda = re.search(patron,texto)
print(busqueda.group(2))

clave = input("Clave: ")
patron= r"\D{1}\w{7}"
busqueda = re.search(patron, clave)
print(busqueda)

texto = "No atendemos los lunes por la tarde"
buscar = re.search(r"lunes|martes", texto)
print(buscar)

buscar = re.search(r"...demos...", texto)
print(buscar)

# Digito al inicio
buscar = re.search(r"^\D", texto)
print(buscar)

# Digito al final
buscar = re.search(r"\D$", texto)
print(buscar)

# Indicar que el patron debe excluir con llaves y acento circunflejo
# Busca todo lo que no sea un espacio
# Con el signo + busca hasta el espacio vacio y corta ahi
buscar = re.findall(r"[^\s]+", texto)
print(buscar)

