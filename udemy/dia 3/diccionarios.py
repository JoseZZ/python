diccionario = {'c1': 'Hola', 'c2': 'Mundo', 'c3': 'Python'}
print(type(diccionario))

resultado = diccionario['c1']
print(resultado)

cliente = {"nombre": "Juan", "apellido": "Perez", "edad": 20, "peso": 60.5}
consulta = cliente["apellido"]
print(consulta)

dic = {"clave1": 1, "clave2": [10, 20, 30], "clave3": {"nombre": "Juan", "edad": 20}}
print(dic["clave2"])
print(dic["clave2"][1])
print(dic["clave3"]["nombre"])

nuevo_dic = {"clave1": 1, "clave2": 2, "clave3": 3}
print(nuevo_dic)
nuevo_dic["clave4"] = "Nuevo Dato"
print(nuevo_dic)
nuevo_dic["clave1"] = "Otro Dato"
print(nuevo_dic)

print(nuevo_dic.keys())
print(nuevo_dic.values())
print(nuevo_dic.items())



