import tkinter
from tkinter import *
from datetime import date
from tkinter import ttk
from sys import version_info

if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

from functools import partial

import Vista.Calendario as cal
import Controlador.Registros as registro


class Plantilla:

    def ventanaEntrada(self, ventana):
        ##ventana
        venEntrada = Toplevel(ventana)
        # venEntrada.geometry("800x500")

        # declaracion de variables
        fecha_ini = str(date.today())
        fecha_fin = str(date.today())

        # objeto de la clase
        obj_calendario = cal.Calendarios()

        # objeto de la clase

        # botones declaracion
        btn_fecha_inicio = Button(venEntrada)
        btn_fecha_fin = Button(venEntrada)
        btn_guardar_registro = Button(venEntrada)
        # ----------contenido

        lbl_fecha_inicio = Label(venEntrada, text="Fecha entada:")
        lbl_fecha_inicio.config(fon=("Helvética", 11))
        lbl_fecha_inicio.grid(row=0, column=0, pady=10, padx=10)

        lbl_fecha_inicio_2 = Label(venEntrada, text=fecha_ini)
        lbl_fecha_inicio_2.config(fon=("Helvética", 11))
        lbl_fecha_inicio_2.grid(row=0, column=1, pady=10, padx=10)

        # boton

        btn_fecha_inicio.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec,venEntrada,lbl_fecha_inicio_2))
        btn_fecha_inicio.grid(row=0, column=2, pady=10, padx=10)

        lbl_fecha_fin = Label(venEntrada, text="Fecha entada:")
        lbl_fecha_fin.config(fon=("Helvética", 11))
        lbl_fecha_fin.grid(row=1, column=0, pady=10, padx=10)

        lbl_fecha_fin_2 = Label(venEntrada, text=fecha_fin)
        lbl_fecha_fin_2.config(fon=("Helvética", 11))
        lbl_fecha_fin_2.grid(row=1, column=1, pady=10, padx=10)
        # boton

        btn_fecha_fin.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec,venEntrada,lbl_fecha_fin_2))
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



        btn_guardar_registro.config(fon=("Helvética", 11), text="guadar", command=partial(self.registro_nuevo,lbl_fecha_inicio_2.cget("text"), lbl_fecha_fin_2.cget("text"),lista_desple.get(),campotexto.get("1.0","end")))
        btn_guardar_registro.grid(row=5, column=1, pady=10, padx=10, columnspan=2)

    def registro_nuevo(self, fecha_inicial, fecha_fin, operacion, nota):
        nuevo_registro = registro.Registros()
        nuevo_registro.Nueva_operacion(fecha_inicial, fecha_fin, operacion, nota)
