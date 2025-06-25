import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/2022/10/el-modulo-secreto-de-python.html")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

titulo = sopa.select("title")
print(titulo[0].getText())

parrafos = sopa.select("p")
for parrafo in parrafos:
    print(parrafo.getText())

autor = sopa.select(".author-name span")
print(autor[0].getText())

pagina_imagenes = requests.get("https://www.udemy.com/user/fedegaray/")
sopa_imagenes = bs4.BeautifulSoup(pagina_imagenes.text, "lxml")

imagenes = sopa_imagenes.select("img")
imagen_federico = sopa_imagenes.select("img")[1]["src"]

f = open("federico.jpg", "wb")
f.write(requests.get(imagen_federico).content)
f.close()
print("Imagen descargada correctamente")







