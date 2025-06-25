import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# lista de titulos con 4 o 5 estrellas
titulos = []
for i in range(1, 51):
    # Obtener la pagina de libros
    resultado = requests.get(url_base.format(i))
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")
    # Seleccionar los libros
    libros = sopa.select(".product_pod")
    for libro in libros:
        # Si el libro tiene 4 o 5 estrellas, agregar el titulo a la lista
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            titulo = libro.select("a")[1]["title"]
            print(titulo)
            titulos.append(titulo)

# Imprimir los titulos
print("Libros con 4 o 5 estrellas:")
for titulo in titulos:
    print(titulo)
