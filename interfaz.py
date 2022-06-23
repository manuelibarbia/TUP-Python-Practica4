from cProfile import label
from ctypes import sizeof
from tkinter import *
from tkinter import ttk


#**********Ventana**********#

root = Tk()
root.geometry("1000x700")
root.title("Peluqueria Canina")
root.configure(bg="lightblue")

#**********Ventana**********#



#**********Título**********#

title_text = Label(root, text = "Programa de peluquería canina", font = (40))
title_text.pack(pady=10)

#**********Título**********#



#**********Pestañas**********#


#**********Cargar perro**********#

opcion = ttk.Notebook(root)
opcion.pack(fill = "both", expand = "yes")

tabla1 = ttk.Frame(opcion)
opcion.add(tabla1, text = "Cargar perro")

tabla2 = ttk.Frame(opcion)
opcion.add(tabla2, text = "Editar perro")

tabla3 = ttk.Frame(opcion)
opcion.add(tabla3, text = "Borrar perro")

tabla4 = ttk.Frame(opcion)
opcion.add(tabla4, text = "Cargar motivo visita")

tabla5 = ttk.Frame(opcion)
opcion.add(tabla5, text = "Mostrar perros")

tabla6 = ttk.Frame(opcion)
opcion.add(tabla6, text = "Agregar comportamiento")

tabla7 = ttk.Frame(opcion)
opcion.add(tabla7, text = "Cargar personal")

tabla8 = ttk.Frame(opcion)
opcion.add(tabla8, text = "Mostrar peluqueros")

label_nombre_perro = ttk.Label(tabla1, text="Nombre del perro:")
label_nombre_perro.grid(row=0, column=0, padx=10, pady=10)
entry_nombre_perro = ttk.Entry(tabla1)
entry_nombre_perro.grid(row=0, column=1, padx=10, pady=10)

label_dueño = ttk.Label(tabla1, text="Nombre del dueño:")
label_dueño.grid(row=1, column=0, padx=10, pady=10)
entry_dueño = ttk.Entry(tabla1)
entry_dueño.grid(row=1, column=1, padx=10, pady=10)

label_direccion = ttk.Label(tabla1, text="Dirección:")
label_direccion.grid(row=2, column=0, padx=10, pady=10)
entry_direccion = ttk.Entry(tabla1)
entry_direccion.grid(row=2, column=1, padx=10, pady=10)

label_telefono = ttk.Label(tabla1, text="Teléfono:")
label_telefono.grid(row=3, column=0, padx=10, pady=10)
entry_telefono = ttk.Entry(tabla1)
entry_telefono.grid(row=3, column=1, padx=10, pady=10)

button_agregar_perro = ttk.Button(tabla1, text = "Agregar" )
button_agregar_perro.grid(row=6, column=2, pady=30)

#**********-Cargar perro**********#


#**********Editar perro**********#

label_nombre_perro_modificar = ttk.Label(tabla2, text="Nombre del perro a modificar:")
label_nombre_perro_modificar.grid(row=0, column=0, padx=10, pady=10)
entry_nombre_perro_modificar = ttk.Entry(tabla2)
entry_nombre_perro_modificar.grid(row=0, column=1, padx=10, pady=10)

label_nuevo_domicilio = ttk.Label(tabla2, text="Nuevo domicilio:")
label_nuevo_domicilio.grid(row=1, column=0, padx=10, pady=10)
entry_nuevo_domicilio = ttk.Entry(tabla2)
entry_nuevo_domicilio.grid(row=1, column=1, padx=10, pady=10)

label_nuevo_telefono = ttk.Label(tabla2, text=" Nuevo teléfono:")
label_nuevo_telefono.grid(row=2, column=0, padx=10, pady=10)
entry_nuevo_telefono = ttk.Entry(tabla2)
entry_nuevo_telefono.grid(row=2, column=1, padx=10, pady=10)

button_modificar_perro = ttk.Button(tabla2, text = "Modificar perro" )
button_modificar_perro.grid(row=3, column=1, pady=30)

#**********Editar perro**********#


#**********Borrar perro**********#

label_nombre_perro = ttk.Label(tabla3, text="Nombre del perro a borrar:")
label_nombre_perro.grid(row=0, column=0, padx=10, pady=10)
entry_nombre_perro = ttk.Entry(tabla3)
entry_nombre_perro.grid(row=0, column=1, padx=10, pady=10)

button_borrar_perro = ttk.Button(tabla3, text = "Borrar perro")
button_borrar_perro.grid(row=1, column=1, pady=30)

#**********Borrar perro**********#


#**********Agregar motivo**********#

label_nombre_perroo = ttk.Label(tabla4, text="Nombre del perro:")
label_nombre_perroo.grid(row=0, column=0, padx=10, pady=10)
entry_nombre_perroo = ttk.Entry(tabla4)
entry_nombre_perroo.grid(row=0, column=1, padx=10, pady=10)

label_baño = ttk.Label(tabla4, text="Motivo:")
label_baño.grid(row=1, column=0, padx=10, pady=10)
radiobutton1_motivo_visita = Radiobutton(tabla4, text = "Baño", value=True)
radiobutton1_motivo_visita.grid(row=1, column=1, padx=5, pady=10)
radiobutton2_motivo_visita = Radiobutton(tabla4, text = "Baño y corte", value=False)
radiobutton2_motivo_visita.grid(row=1, column=2, padx=5, pady=10)

button_agregar_motivo = ttk.Button(tabla4, text = "Guardar")
button_agregar_motivo.grid(row=2, column=1, pady=30)

#**********Agregar motivo**********#


#**********Mostrar tabla**********#

ttk.Label(tabla5, text="ID").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(tabla5, text="Nombre perro").grid(row=0, column=1, padx=5, pady=5)
ttk.Label(tabla5, text="Nombre dueño").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(tabla5, text="Domicilio").grid(row=0, column=3, padx=5, pady=5)
ttk.Label(tabla5, text="Teléfono").grid(row=0, column=4, padx=5, pady=5)
ttk.Label(tabla5, text="Baño").grid(row=0, column=5, padx=5, pady=5)
ttk.Label(tabla5, text="Baño y corte").grid(row=0, column=6, padx=5, pady=5)

#**********Mostrar tabla**********#


#**********Agregar comportamiento**********#

label_comportamiento = ttk.Label(tabla6, text="Comportamiento:")
label_comportamiento.grid(row=0, column=0, padx=10, pady=10)
radiobutton1_comportamiento = Checkbutton(tabla6, text="Muy bien")
radiobutton1_comportamiento.grid(row=0, column=1)
radiobutton2_comportamiento = Checkbutton(tabla6, text="Bien")
radiobutton2_comportamiento.grid(row=0, column=2)
radiobutton3_comportamiento = Checkbutton(tabla6, text="Mal")
radiobutton3_comportamiento.grid(row=0, column=3)
radiobutton4_comportamiento = Checkbutton(tabla6, text="Muy mal")
radiobutton4_comportamiento.grid(row=0, column=4)

button_agregar_perro = ttk.Button(tabla6, text = "Agregar" )
button_agregar_perro.grid(row=1, column=1, pady=30)

#**********Agregar comportamiento**********#

#**********Agregar personal**********#

label_codigo_identificatorio = ttk.Label(tabla7, text="Codigo identificatorio:")
label_codigo_identificatorio.grid(row=0, column=0, padx=10, pady=10)
entry_codigo_identificatorio = ttk.Entry(tabla7)
entry_codigo_identificatorio.grid(row=0, column=1, padx=10, pady=10)

label_nombre_personal = ttk.Label(tabla7, text="Nombre:")
label_nombre_personal.grid(row=1, column=0, padx=10, pady=10)
entry_nombre_personal = ttk.Entry(tabla7)
entry_nombre_personal.grid(row=1, column=1, padx=10, pady=10)

label_apellido_personal = ttk.Label(tabla7, text="Apellido:")
label_apellido_personal.grid(row=2, column=0, padx=10, pady=10)
entry_apellido_personal = ttk.Entry(tabla7)
entry_apellido_personal.grid(row=2, column=1, padx=10, pady=10)

label_dni = ttk.Label(tabla7, text="DNI:")
label_dni.grid(row=3, column=0, padx=10, pady=10)
entry_dni = ttk.Entry(tabla7)
entry_dni.grid(row=3, column=1, padx=10, pady=10)

label_direccion_personal = ttk.Label(tabla7, text="Direccion:")
label_direccion_personal.grid(row=4, column=0, padx=10, pady=10)
entry_direccion_personal = ttk.Entry(tabla7)
entry_direccion_personal.grid(row=4, column=1, padx=10, pady=10)

label_telefono_personal = ttk.Label(tabla7, text="Telefono:")
label_telefono_personal.grid(row=5, column=0, padx=10, pady=10)
entry_telefono_personal = ttk.Entry(tabla7)
entry_telefono_personal.grid(row=5, column=1, padx=10, pady=10)

label_email_personal = ttk.Label(tabla7, text="Email:")
label_email_personal.grid(row=6, column=0, padx=10, pady=10)
entry_email_personal = ttk.Entry(tabla7)
entry_email_personal.grid(row=6, column=1, padx=10, pady=10)

label_años_experiencia = ttk.Label(tabla7, text="Años de experiencia:")
label_años_experiencia.grid(row=7, column=0, padx=10, pady=10)
entry_años_experiencia = ttk.Entry(tabla7)
entry_años_experiencia.grid(row=7, column=1, padx=10, pady=10)

label_sueldo_personal = ttk.Label(tabla7, text="Sueldo:")
label_sueldo_personal.grid(row=8, column=0, padx=10, pady=10)
entry_sueldo_personal = ttk.Entry(tabla7)
entry_sueldo_personal.grid(row=8, column=1, padx=10, pady=10)

button_agregar_perro = ttk.Button(tabla7, text = "Agregar" )
button_agregar_perro.grid(row=9, column=1, pady=30)

#**********Agregar personal**********#

#**********Mostrar peluqueros**********#

ttk.Label(tabla8, text="Codigo identificatorio").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(tabla8, text="Nombre").grid(row=0, column=1, padx=5, pady=5)
ttk.Label(tabla8, text="Apellido").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(tabla8, text="DNI").grid(row=0, column=3, padx=5, pady=5)
ttk.Label(tabla8, text="Direccion").grid(row=0, column=4, padx=5, pady=5)
ttk.Label(tabla8, text="Teléfono").grid(row=0, column=5, padx=5, pady=5)
ttk.Label(tabla8, text="Email").grid(row=0, column=6, padx=5, pady=5)
ttk.Label(tabla8, text="Años de experiencia").grid(row=0, column=7, padx=5, pady=5)
ttk.Label(tabla8, text="Sueldo").grid(row=0, column=8, padx=5, pady=5)

#**********Mostrar peluqueros**********#
root.mainloop()