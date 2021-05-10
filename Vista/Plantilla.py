import tkinter
from tkinter import *
from datetime import date
from tkinter import ttk, messagebox
from sys import version_info

if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

from functools import partial

import Vista.Calendario as cal
import Modelo.Mod_operacion as Mop

class Plantilla:

    def ventana_Editar(self,id, ventana):
        #nueva operacion objeto
        obj_nuevo=Mop.Operacion()
        print(id)

        ##ventana
        venEntrada = Toplevel(ventana)
        # venEntrada.geometry("800x500")

        # declaracion de variables
        fecha_ini = str(date.today())
        fecha_fin = str(date.today())

        # objeto de la clase
        obj_calendario = cal.Calendarios()
        # objeto de la clase

        #asignamos a objeto registro fechas
        obj_nuevo.set_fecha_ini(fecha_ini)
        obj_nuevo.set_fecha_fin(fecha_fin)

        # botones declaracion
        btn_fecha_inicio = Button(venEntrada)
        btn_fecha_fin = Button(venEntrada)
        btn_guardar_registro = Button(venEntrada)
        btn_cancelar=Button(venEntrada)
        # ----------contenido

        lbl_fecha_inicio = Label(venEntrada, text="Fecha entada:")
        lbl_fecha_inicio.config(fon=("Helvética", 11))
        lbl_fecha_inicio.grid(row=0, column=0, pady=10, padx=10)

        lbl_fecha_inicio_2 = Label(venEntrada, text=fecha_ini)
        lbl_fecha_inicio_2.config(fon=("Helvética", 11))
        lbl_fecha_inicio_2.grid(row=0, column=1, pady=10, padx=10)

        # boton

        btn_fecha_inicio.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec_ini,venEntrada,lbl_fecha_inicio_2,obj_nuevo))
        btn_fecha_inicio.grid(row=0, column=2, pady=10, padx=10)

        lbl_fecha_fin = Label(venEntrada, text="Fecha entada:")
        lbl_fecha_fin.config(fon=("Helvética", 11))
        lbl_fecha_fin.grid(row=1, column=0, pady=10, padx=10)

        lbl_fecha_fin_2 = Label(venEntrada, text=fecha_fin)
        lbl_fecha_fin_2.config(fon=("Helvética", 11))
        lbl_fecha_fin_2.grid(row=1, column=1, pady=10, padx=10)
        # boton

        btn_fecha_fin.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec_fin,venEntrada,lbl_fecha_fin_2,obj_nuevo))
        btn_fecha_fin.grid(row=1, column=2, pady=10, padx=10)

        lbl_desplegable = Label(venEntrada, text="Operacion: ")
        lbl_desplegable.config(fon=("Helvética", 11))
        lbl_desplegable.grid(row=2, column=0, pady=10, padx=10)

        lista_desple = ttk.Combobox(venEntrada, width=17)
        lista_desple.grid(row=2, column=1, pady=10, padx=10)
        opciones = ["compra", "venta"]
        lista_desple['values'] = opciones

        # campo de texto LBL
        lbl_campo_texto = Label(venEntrada, text="Nota: ")
        lbl_campo_texto.config(fon=("Helvética", 11))
        lbl_campo_texto.grid(row=3, column=0, pady=10, padx=10)

        # campo de texto
        campotexto = Text(venEntrada)
        campotexto.grid(row=4, column=0, pady=10, padx=10, columnspan=2)
        campotexto.config(width=30, height=10)

        def guardar():
            obj_nuevo.set_operacion(lista_desple.get())
            obj_nuevo.set_nota(campotexto.get("1.0","end"))
            self.registro_nuevo(obj_nuevo)

        btn_guardar_registro.config(fon=("Helvética", 11), text="guadar", command=guardar)
        btn_guardar_registro.grid(row=5, column=1, pady=10, padx=10, columnspan=2)

        def salir():
            valor = messagebox.askyesno("Salir", "¿deseas salir?")
            if valor:
                venEntrada.destroy()

        btn_cancelar.config(fon=("Helvética", 11), text="Cancelar", command=salir)
        btn_cancelar.grid(row=5, column=2, pady=10, padx=10, columnspan=2)

    def registro_nuevo(self,nuevo_registro):

        print(nuevo_registro.__str__())



    def ventana_Nuevo(self, ventana):
        #nueva operacion objeto
        obj_nuevo=Mop.Operacion()


        ##ventana
        venEntrada = Toplevel(ventana)
        # venEntrada.geometry("800x500")

        # declaracion de variables
        fecha_ini = str(date.today())
        fecha_fin = "0000-00-00"

        # objeto de la clase
        obj_calendario = cal.Calendarios()
        # objeto de la clase

        #asignamos a objeto registro fechas
        obj_nuevo.set_fecha_ini(fecha_ini)
        obj_nuevo.set_fecha_fin(fecha_fin)

        # botones declaracion
        btn_fecha_inicio = Button(venEntrada)
        btn_guardar_registro = Button(venEntrada)
        btn_cancelar=Button(venEntrada)
        # ----------contenido

        lbl_fecha_inicio = Label(venEntrada, text="Fecha entada:")
        lbl_fecha_inicio.config(fon=("Helvética", 11))
        lbl_fecha_inicio.grid(row=0, column=0, pady=10, padx=10)

        lbl_fecha_inicio_2 = Label(venEntrada, text=fecha_ini)
        lbl_fecha_inicio_2.config(fon=("Helvética", 11))
        lbl_fecha_inicio_2.grid(row=0, column=1, pady=10, padx=10)

        # boton

        btn_fecha_inicio.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec_ini,venEntrada,lbl_fecha_inicio_2,obj_nuevo))
        btn_fecha_inicio.grid(row=0, column=2, pady=10, padx=10)

        # lbl_fecha_fin = Label(venEntrada, text="Fecha entada:")
        # lbl_fecha_fin.config(fon=("Helvética", 11))
        # lbl_fecha_fin.grid(row=1, column=0, pady=10, padx=10)
        #
        # lbl_fecha_fin_2 = Label(venEntrada, text=fecha_fin)
        # lbl_fecha_fin_2.config(fon=("Helvética", 11))
        # lbl_fecha_fin_2.grid(row=1, column=1, pady=10, padx=10)
        # # boton
        #
        # btn_fecha_fin.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec_fin,venEntrada,lbl_fecha_fin_2,obj_nuevo))
        # btn_fecha_fin.grid(row=1, column=2, pady=10, padx=10)

        lbl_desplegable = Label(venEntrada, text="Operacion: ")
        lbl_desplegable.config(fon=("Helvética", 11))
        lbl_desplegable.grid(row=2, column=0, pady=10, padx=10)

        lista_desple = ttk.Combobox(venEntrada, width=17)
        lista_desple.grid(row=2, column=1, pady=10, padx=10)
        opciones = ["compra", "venta"]
        lista_desple['values'] = opciones

        # campo de texto LBL
        lbl_campo_texto = Label(venEntrada, text="Nota: ")
        lbl_campo_texto.config(fon=("Helvética", 11))
        lbl_campo_texto.grid(row=3, column=0, pady=10, padx=10)

        # campo de texto
        campotexto = Text(venEntrada)
        campotexto.grid(row=3, column=1, pady=10, padx=10, columnspan=2)
        campotexto.config(width=30, height=10)

        def guardar():
            valor = messagebox.askyesno("Guardar", "¿deseas guardarlo?")
            if valor:
                obj_nuevo.set_operacion(lista_desple.get())
                obj_nuevo.set_nota(campotexto.get("1.0","end"))
                self.registro_nuevo(obj_nuevo)
                venEntrada.destroy()
            else:
                venEntrada.destroy()

        btn_guardar_registro.config(fon=("Helvética", 11), text="guadar", command=guardar)
        btn_guardar_registro.grid(row=5, column=1, pady=10, padx=10, columnspan=2)

        def salir():
            valor = messagebox.askyesno("Salir", "¿deseas salir?")
            if valor:
                venEntrada.destroy()

        btn_cancelar.config(fon=("Helvética", 11), text="Cancelar", command=salir)
        btn_cancelar.grid(row=5, column=2, pady=10, padx=10, columnspan=2)

    def registro_editar(self, nuevo_registro):

        print(nuevo_registro.__str__())