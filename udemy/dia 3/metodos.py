texto = "Este es el texto de Federico"
print(texto.upper())
print(texto[2:9].upper())
print(texto.lower())
print(texto.split())
print(texto.split("t"))

a = "Aprender"
b = "python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
print (e)

print(texto.find("s"))
print(texto.find("g"))

print(texto.replace("Federico", "Fede"))
print(texto.replace("e", "x"))
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala", "buena"))