from tkinter import *

import Vista.Principal as p
import Controlador.DatosPrueba as cd
import Vista.Plantilla as pl


class Tabla:

    editar_operacion=pl.Plantilla()

    def TablaPrincipal(self):

        # -------variables------
        # objeto de la clase principal
        tabla = p.Principal.tabla

        tabla.pack()
        lista = cd.ConEntrada.datosProvisionales(self)
        # -------variables------
        # ------contenido------

        tabla.heading("#0", text="N.operacion")
        tabla.heading("#1", text="Fecha entrada")
        tabla.heading("#2", text="Fecha salida")
        tabla.heading("#3", text="C/V")
        tabla.heading("#4", text="Gan/Per")
        tabla.heading("#5", text="Nota")
        tabla.heading("#6", text="Img entrada")
        tabla.heading("#7", text="Img salida")

        ##------le damos tamaño a la columnas
        for i in range(0, 8):
            tabla.column("#" + str(i), width="125")
            print(i)
        ##------le damos tamaño a la columnas
        tabla.bind("<Double-Button-1>", self.click)
        ###--------------------Contenido de la tabla-------

        for l in lista:
            tabla.insert(parent="", index="end", text=l[0], values=(l[1], l[2], l[3], l[4], l[5], l[6], l[7]))

        ###--------------------Contenido de la tabla-------
        # ------contenido------

    def click(self, event):
        lista = cd.ConEntrada.datosProvisionales(self)
        seleccion = p.Principal.tabla.item(p.Principal.tabla.selection())
        self.editar_operacion.ventana_Editar(seleccion["text"],p.Principal.ventana)
















