import datetime
import random
from tkinter import *
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.45, 2.50, 3.00, 1.75, 2.25, 4.00, 4.50, 3.75, 2.00, 1.80]
precios_bebida = [0.50, 1.00, 1.20, 1.50, 1.75, 2.00, 2.50, 3.00, 2.25, 2.75]
precios_postre = [1.00, 1.50, 1.75, 2.00, 2.25, 2.50, 3.00, 3.50, 2.75, 3.25]


def calcular(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, resultado)
    operador = ''


def revisar_check():
    x = 0
    # revisar si el check esta marcado
    for c in variables_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state="normal")
            if texto_comida[x].get() == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state="disabled")
            texto_comida[x].set("0")
        x += 1
    # revisar si el check esta marcado
    x = 0
    for b in variables_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state="normal")
            if texto_bebida[x].get() == "0":
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state="disabled")
            texto_bebida[x].set("0")
        x += 1
    # revisar si el check esta marcado
    x = 0
    for p in variables_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state="normal")
            if texto_postre[x].get() == "0":
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state="disabled")
            texto_postre[x].set("0")
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        if cantidad.get() != "0":
            sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
            p += 1
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        if cantidad.get() != "0":
            sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
            p += 1
    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        if cantidad.get() != "0":
            sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[p])
            p += 1
    # calcular el total
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    iva = sub_total * 0.07
    total_final = sub_total + iva

    # mostrar los resultados
    varcostocomida.set(f"{round(sub_total_comida, 2)}")
    varcostobebida.set(f"{round(sub_total_bebida, 2)}")
    varcostopostre.set(f"{round(sub_total_postre, 2)}")
    var_sub_total.set(f"{round(sub_total, 2)}")
    var_iva.set(f"{round(iva, 2)}")
    var_total.set(f"{round(total_final, 2)}")


def recibo():
    texto_recibo.delete(1.0, END)  # limpiar el area de recibo
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    fecha_recibo = f"Fecha - {fecha}"
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"=" * 42 + "\n")
    texto_recibo.insert(END, "Items\t\tCant.\tCoste items\n")
    texto_recibo.insert(END, f"-" * 75 + "\n")

    # agregar items comida
    x = 0
    for plato in texto_comida:
        if plato.get() != "0":
            texto_recibo.insert(END,
                                f"{lista_comidas[x].title()}\t\t{plato.get()}\t{float(plato.get()) * precios_comida[x]}\n")
        x += 1
    # agregar items bebida
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END,
                                f"{lista_bebidas[x].title()}\t\t{bebida.get()}\t{float(bebida.get()) * precios_bebida[x]}\n")
        x += 1
    # agregar items postre
    x = 0
    for postre in texto_postre:
        if postre.get() != "0":
            texto_recibo.insert(END,
                                f"{lista_postres[x].title()}\t\t{postre.get()}\t{float(postre.get()) * precios_postre[x]}\n")
        x += 1
    texto_recibo.insert(END, f"-" * 75 + "\n")
    # agregar totales
    texto_recibo.insert(END, f"Subtotal:\t\t\t{var_sub_total.get()}\n")
    texto_recibo.insert(END, f"IVA:\t\t\t{var_iva.get()}\n")
    texto_recibo.insert(END, f"." * 63 + "\n")
    texto_recibo.insert(END, f"Total:\t\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"*" * 80 + "\n\n")
    texto_recibo.insert(END, "Vuelva pronto!\n")


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Guardar", "Recibo guardado correctamente")

def resetear():
    texto_recibo.delete(0.1,END)
    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_postre:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state="disabled")
    for cuadro in cuadros_bebida:
        cuadro.config(state="disabled")
    for cuadro in cuadros_postre:
        cuadro.config(state="disabled")

    for variable in variables_comida:
        variable.set(0)
    for variable in variables_bebida:
        variable.set(0)
    for variable in variables_postre:
        variable.set(0)

    varcostocomida.set('')
    varcostobebida.set('')
    varcostopostre.set('')
    var_sub_total.set('')
    var_iva.set('')
    var_total.set('')

# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry("1200x650+0+0")

# evitar maximizar la ventana
aplicacion.resizable(width=False, height=False)

# titulo de la ventana
aplicacion.title("Mi Restaurante")

# color de fondo
aplicacion.config(bg="burlywood")

# panel superior
panel_superior = Frame(aplicacion, bg="burlywood", bd=1, relief="flat")
panel_superior.pack(side=TOP)
# titulo del panel superior
titulo = Label(panel_superior, text="Sistema de facturacion", width=27, bg="burlywood", fg="azure4", font=("Dosis", 58))
titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief="flat")
panel_izquierdo.pack(side=LEFT, fill=BOTH)
# panel precios
panel_precios = Frame(panel_izquierdo, bd=1, relief="flat", bg="azure4", padx=40)
panel_precios.pack(side=BOTTOM)
# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, "bold"), bd=1, relief="flat", fg="azure4")
panel_comidas.pack(side=LEFT)
# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"), bd=1, relief="flat",
                           fg="azure4")
panel_bebidas.pack(side=LEFT)
# panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"), bd=1, relief="flat",
                           fg="azure4")
panel_postres.pack(side=LEFT)

# panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief="flat")
panel_derecho.pack(side=RIGHT)
# panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief="flat", bg="burlywood")
panel_calculadora.pack()
# panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief="flat", bg="burlywood")
panel_recibo.pack()
# panel botones
panel_botones = Frame(panel_derecho, bd=1, relief="flat", bg="burlywood")
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'carne', 'pescado', 'ensalada', 'sopa', 'pizza1', 'pizza2', 'hamburguesa', 'hot dog',
                 'papas fritas']
lista_bebidas = ['agua', 'refresco', 'zumo', 'cafe', 'te', 'cerveza', 'vino1', 'vino2', 'licor1', 'licor2']
lista_postres = ['helado', 'tarta', 'fruta', 'chocolate', 'galleta', 'pastel1', 'pastel2', 'brownie', 'flan', 'pudin', ]

# Generar items comida
variables_comida = []
contador = 0
cuadros_comida = []
texto_comida = []
for comida in lista_comidas:
    # crear variable para cada comida
    variables_comida.append('')
    variables_comida[contador] = IntVar()

    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=("Dosis", 19, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador, column=0, sticky="w")

    # crear cuadro de texto para cada comida
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")  # valor por defecto

    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=("Dosis", 19, "bold"),
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_comida[contador])

    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1

# Generar items bebidas
contador = 0
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
for bebida in lista_bebidas:
    # crear variable para cada bebida
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()

    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=("Dosis", 19, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador, column=0, sticky="w")

    # crear cuadro de texto para cada bebida
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")  # valor por defecto

    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=("Dosis", 19, "bold"),
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)

    contador += 1

# Generar itemspostres
contador = 0
variables_postre = []
cuadros_postre = []
texto_postre = []
for postre in lista_postres:
    # crear variable para cada postre
    variables_postre.append('')
    variables_postre[contador] = IntVar()

    postre = Checkbutton(panel_postres, text=postre.title(), font=("Dosis", 19, "bold"), onvalue=1, offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador, column=0, sticky="w")

    # crear cuadro de texto para cada postre
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set("0")  # valor por defecto
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=("Dosis", 19, "bold"),
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)

    contador += 1

# variables de coste
varcostocomida = StringVar()
varcostobebida = StringVar()
varcostopostre = StringVar()
var_sub_total = StringVar()
var_iva = StringVar()
var_total = StringVar()

# etiquetas de coste y campos de entrada comida
etiqueta_coste_comida = Label(panel_precios,
                              text="Coste comida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_coste_comida.grid(row=0, column=0)

texto_coste_comida = Entry(panel_precios,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           justify="right",
                           textvariable=varcostocomida)  # valor por defecto
texto_coste_comida.grid(row=0, column=1, padx=41)

# etiquetas de coste y campos de entrada bebida
etiqueta_coste_bebida = Label(panel_precios,
                              text="Coste bebida",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_coste_bebida.grid(row=1, column=0)
texto_coste_bebida = Entry(panel_precios,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           justify="right",
                           textvariable=varcostobebida)  # valor por defecto
texto_coste_bebida.grid(row=1, column=1, padx=41)

# etiquetas de coste y campos de entrada postre
etiqueta_coste_postre = Label(panel_precios,
                              text="Coste postre",
                              font=("Dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_coste_postre.grid(row=2, column=0)
texto_coste_postre = Entry(panel_precios,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           justify="right",
                           textvariable=varcostopostre)  # valor por defecto
texto_coste_postre.grid(row=2, column=1, padx=41)

# etiquetas de coste total y campo de entrada
etiqueta_coste_total = Label(panel_precios,
                             text="Subtotal",
                             font=("Dosis", 12, "bold"),
                             bg="azure4",
                             fg="white")
etiqueta_coste_total.grid(row=0, column=2)
texto_coste_total = Entry(panel_precios,
                          font=("Dosis", 12, "bold"),
                          bd=1,
                          width=10,
                          state="readonly",
                          justify="right",
                          textvariable=var_sub_total)
texto_coste_total.grid(row=0, column=3, padx=41)

# etiquetas de coste total y campo de entrada iva
etiqueta_coste_iva = Label(panel_precios,
                           text="IVA",
                           font=("Dosis", 12, "bold"),
                           bg="azure4",
                           fg="white")
etiqueta_coste_iva.grid(row=1, column=2)
texto_coste_iva = Entry(panel_precios,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        justify="right",
                        textvariable=var_iva)  # valor por defecto
texto_coste_iva.grid(row=1, column=3, padx=41)

# etiquetas de coste total y campo de entrada total
etiqueta_coste_total_final = Label(panel_precios,
                                   text="Total",
                                   font=("Dosis", 12, "bold"),
                                   bg="azure4",
                                   fg="white")
etiqueta_coste_total_final.grid(row=2, column=2)
texto_coste_total_final = Entry(panel_precios,
                                font=("Dosis", 12, "bold"),
                                bd=1,
                                width=10,
                                state="readonly",
                                justify="right",
                                textvariable=var_total)  # valor por defecto
texto_coste_total_final.grid(row=2, column=3, padx=41)

# botones
botones = [
    "Total",
    "Recibo",
    "Guardar",
    "Resetear"]
botones_creados = []

columnas = 0

# crear botones
for boton in botones:
    # crear boton
    boton_creado = Button(panel_botones,
                          text=boton.title(),
                          font=("Dosis", 14, "bold"),
                          bg="azure4",
                          fg="white",
                          width=8,
                          bd=1)
    botones_creados.append(boton_creado)
    boton_creado.grid(row=0, column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)

# area calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=("Dosis", 16, "bold"),
                          bd=1,
                          width=32)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# botones de la calculadora
botones_calculadora = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "x",
    "R", "B", "0", "/"]

botones_guardados = []

# crear botones de la calculadora
fila = 1
columna = 0
for boton in botones_calculadora:
    # crear boton
    boton_creado = Button(panel_calculadora,
                          text=boton.title(),
                          font=("Dosis", 16, "bold"),
                          bg="azure4",
                          fg="white",
                          width=8,
                          bd=1)
    botones_guardados.append(boton_creado)

    # posicionar boton
    boton_creado.grid(row=fila, column=columna)
    # aumentar columna
    if columna == 3:
        fila += 1
    columna += 1
    if columna > 3:
        columna = 0

botones_guardados[0].config(command=lambda: calcular('7'))
botones_guardados[1].config(command=lambda: calcular('8'))
botones_guardados[2].config(command=lambda: calcular('9'))
botones_guardados[3].config(command=lambda: calcular('+'))
botones_guardados[4].config(command=lambda: calcular('4'))
botones_guardados[5].config(command=lambda: calcular('5'))
botones_guardados[6].config(command=lambda: calcular('6'))
botones_guardados[7].config(command=lambda: calcular('-'))
botones_guardados[8].config(command=lambda: calcular('1'))
botones_guardados[9].config(command=lambda: calcular('2'))
botones_guardados[10].config(command=lambda: calcular('3'))
botones_guardados[11].config(command=lambda: calcular('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: calcular('0'))
botones_guardados[15].config(command=lambda: calcular('/'))

# evitar que la pantalla se cierre
aplicacion.mainloop()
