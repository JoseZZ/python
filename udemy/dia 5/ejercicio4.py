def describir_persona(nombre, **kwargs):
    mensaje = f"Características de {nombre}:"
    for key, value in kwargs.items():
        mensaje = mensaje + f"\n- {key}: {value}"
    print(mensaje)

describir_persona("María", color_ojos="azules", color_pelo="rubio")