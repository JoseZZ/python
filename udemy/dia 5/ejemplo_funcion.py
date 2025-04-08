precios_cafe = [("capuchino", 1.5), ("expresso", 2.0), ("americano", 1.8), ("latte", 2.5)]

for elemento in precios_cafe:
    print(f"El precio del {elemento[0]} es {elemento[1]} euros")

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ""
    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return(cafe_mas_caro, precio_mayor)

print(f"El cafe mas caro es {cafe_mas_caro(precios_cafe)}")



