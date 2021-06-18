import tkinter
from tkinter import *
########### nos ayuda para los parametros de comando
from sys import version_info
from tkinter import ttk,messagebox

if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

from functools import partial
########### nos ayuda para los parametros de comando

import Controlador.Registros as Registros


class Saldo :
    obj_registros = Registros.ControlRegistros()
    def saldo(self,ventana_principal,tabla, lbltotal, lbl_gan_per):

        ventana_saldo = Toplevel(ventana_principal)


        #Label saldo
        lbl_saldo= Label(ventana_saldo)
        lbl_saldo.config(fon=("Helvética", 11),text="Saldo")
        lbl_saldo.grid(row=1, column=0, pady=10, padx=10, columnspan=2)

        txt_saldo=Entry(ventana_saldo)
        txt_saldo.config(fon=("Helvética", 11))
        txt_saldo.grid(row=1, column=1, pady=10, padx=10, columnspan=2)
        txt_saldo.insert(tk.END,self.obj_registros.consultar_saldo())

        lbl_borrar_regstros=Label(ventana_saldo)
        lbl_borrar_regstros.config(fon=("Helvética", 11),text="¿Deseas borrar todos los registros?")
        lbl_borrar_regstros.grid(row=2, column=0, pady=10, padx=10)

        lista_desple = ttk.Combobox(ventana_saldo, width=17)
        lista_desple.grid(row=2, column=1, pady=10, padx=10)
        opciones = ["No", "Si"]
        lista_desple['values'] = opciones
        lista_desple.current(0)

        btn_saldo=Button(ventana_saldo)
        btn_saldo.grid(row=3, column=0, pady=10, padx=10)
        btn_saldo.config(fon=("Helvética", 11), text="Guardar", command=partial(self.guardar,ventana_saldo,txt_saldo,lista_desple,tabla,lbltotal,lbl_gan_per))


        btn_cancelar=Button(ventana_saldo)
        btn_cancelar.config(fon=("Helvética", 11), text="Cancelar", command=partial(self.cancelar,ventana_saldo))
        btn_cancelar.grid(row=3, column=1, pady=10, padx=10)


    def cancelar(self, ventana_saldo):
        valor = messagebox.askyesno("Cancelar", "¿deseas cancelar la operacion?")
        if valor:
            ventana_saldo.destroy()



    def guardar(self,ventana_saldo,txt_saldo, lista_desple,tabla,lbltotal,lbl_gan_per):
        saldo = txt_saldo.get()
        valor = messagebox.askyesno("Actualizar", "¿Deseas realizar la accion?")
        if valor:
            self.obj_registros.actualizar_saldo(ventana_saldo,saldo, lista_desple, tabla)
            lbltotal.config(text=self.obj_registros.consultar_saldo())
            lbl_gan_per.config(text=self.obj_registros.consultar_ganacia_perdida())

            ventana_saldo.destroy()
