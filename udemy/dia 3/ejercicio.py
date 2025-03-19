texto = input("Introduce un texto: ").lower()

letras = input("Introduzca tres letras a su eleccion: ").lower()

lista_letras = list(letras.lower())

print(lista_letras)

print(f"La letra {lista_letras[0]} aparece {texto.count(lista_letras[0])} veces en el texto")
print(f"La letra {lista_letras[1]} aparece {texto.count(lista_letras[1])} veces en el texto")
print(f"La letra {lista_letras[2]} aparece {texto.count(lista_letras[2])} veces en el texto")

lista_palabras = texto.split()
print(lista_palabras)

print(f"El texto tiene {len(lista_palabras)} palabras")

print(f"La primera letra del texto es {texto[0]} y la ultima letra es {texto[-1]}")

lista_palabras.reverse()
print(f"El texto al reves es: {lista_palabras}")

print(f"La palabra Pyhton aparece en el texto: {'Python' in texto}")
