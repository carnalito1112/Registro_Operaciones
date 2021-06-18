from datetime import date
from tkinter import *
from tkinter import messagebox, ttk

from sys import version_info

if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

from functools import partial

import Vista.Calendario as c
import Vista.TablaPrincipal as tp
import Vista.Plantilla as pt
import Vista.Saldo as saldo
import Controlador.Registros as control_registros
import Controlador.Datos_consulta as datos_tabla_fecha


class Principal:
    # ------------variable---------
    fechaTitle = str(date.today())
    # ------------variable---------
    # ----------ventana------
    ventana = Tk()
    ventana.title("Bitacora de trading " + fechaTitle)
    #ventana.iconbitmap("Recursos/img/icono.ico")
    ventana.geometry("1024x400")
    # ----------ventana------
    # ------Frames------
    # superior
    frameSuperior = Frame(ventana, width="1000", height="110")
    frameSuperior.pack()
    # inferior
    frameInferior = Frame(ventana, width="1000", height="500")
    frameInferior.config(bg="#4BDB6F")
    frameInferior.pack()
    # ------Frames------

    ##-----------variables-----------

    ##Tabla---}-- de la clase tabla principal
    tabla = ttk.Treeview(frameInferior, columns=[f"#{n}" for n in range(1, 8)])
    ##Tabla----




    #-----variables locales de la clase principal
    fechaIni = str(date.today())
    fechaFin = str(date.today())
    btnFechaIni = Button(frameSuperior, text="Cambiar")
    btnFechaFin = Button(frameSuperior, text="Cambiar")
    lblTotal = Label(frameSuperior )
    lblGanPer = Label(frameSuperior)

    ##------------variables-----------

    #objetos globales

    obj_datos_fecha = datos_tabla_fecha.ConEntrada()

    # objetos globales

    def principalVen(self):
        ##-------objetos-----
        obj_calendario = c.Calendarios()
        tabla = tp.Tabla()
        obj_sal=saldo.Saldo()
        obj_reg = control_registros.ControlRegistros()



        ##-------objetos-----

        # -------menus------
        menubar = Menu(self.ventana)
        self.ventana.config(menu=menubar)
        # -------------filemenu------
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opciones", menu=filemenu)
        filemenu.add_command(label="Saldo",command=partial(obj_sal.saldo,self.ventana, self.tabla,self.lblTotal,self.lblGanPer))
        filemenu.add_command(label="Contacto")
        filemenu.add_command(label="Salir", command=self.salir)

        # -------------filemenu------

        # ----------------contenido superior------------
        # lbl de bienvenida = obtenemos el usuario directamente de la BD
        lblBienvenida = Label(self.frameSuperior, text="Bienvenido Usuario")
        lblBienvenida.config(fon=("Helvética", 14))
        lblBienvenida.place(x=10, y=10)

        # label total letra
        lblTotalLetra = Label(self.frameSuperior, text="Total: ")
        lblTotalLetra.config(fon=("Helvética", 11))
        lblTotalLetra.place(x=240, y=15)
        # label total numero lo obtenemos de sumar las ganancias o perdidas de un usuario

        self.lblTotal.config(fon=("Helvética", 11),text=obj_reg.consultar_saldo())
        self.lblTotal.place(x=300, y=15)

        # label Ganancia/perdida
        lblGanPerLetra = Label(self.frameSuperior, text="Ganancia/Perdida:")
        lblGanPerLetra.config(fon=("Helvética", 11))
        lblGanPerLetra.place(x=420, y=15)

        # label Ganancia/perdida la obtenemos de la siguiene manera saldo original - saldo total hasta hoy

        self.lblGanPer.config(fon=("Helvética", 11), text=obj_reg.consultar_ganacia_perdida())
        self.lblGanPer.place(x=550, y=15)

        # # label Ganancia/perdida dia anterior en letra
        # lblGanPerDiaLetra = Label(self.frameSuperior, text="Ganancia/Perdida dia anterior:")
        # lblGanPerDiaLetra.config(fon=("Helvética", 11))
        # lblGanPerDiaLetra.place(x=635, y=15)
        #
        # # Label ganancia/perdida de dia anterior
        # lblGanPerDia = Label(self.frameSuperior, text="200")
        # lblGanPerDia.config(fon=("Helvética", 11))
        # lblGanPerDia.place(x=840, y=15)

        # boton nueva operacion
        btnNuevOperacion = Button(self.frameSuperior, text="Nueva Operacion", command=self.get_plantilla)
        btnNuevOperacion.config(fon=("Helvética", 11))
        btnNuevOperacion.place(x=10, y=60)
        # boton nueva operacion
        lblResultados = Label(self.frameSuperior, text="Resultados de la tabla")
        lblResultados.config(fon=("Helvética", 11))
        lblResultados.place(x=180, y=70)

        # label fecha inicio

        lblFechaIni = Label(self.frameSuperior, text="Fecha inicio:")
        lblFechaIni.config(fon=("Helvética", 11))
        lblFechaIni.place(x=350, y=70)

        # label fecha inicio 2
        #se envia a calendario
        lblFecha_ini_2 = Label(self.frameSuperior, text=self.fechaIni)
        lblFecha_ini_2.config(fon=("Helvética", 11))
        lblFecha_ini_2.place(x=445, y=70)
        # boton fecha de inicio

        self.btnFechaIni.config(fon=("Helvética", 11), command=partial(obj_calendario.plantilla_fec,self.ventana,lblFecha_ini_2))
        self.btnFechaIni.place(x=540, y=60)

        # lacel fecha final
        lblFecha_fin = Label(self.frameSuperior, text="final:")
        lblFecha_fin.config(fon=("Helvética", 11))
        lblFecha_fin.place(x=650, y=70)

        #se envia a calendario
        lblFecha_fin_2 = Label(self.frameSuperior, text=self.fechaFin)
        lblFecha_fin_2.config(fon=("Helvética", 11))
        lblFecha_fin_2.place(x=690, y=70)

        # boton fecha de final

        self.btnFechaFin.config(fon=("Helvética", 11), command=partial(obj_calendario.plantilla_fec,self.ventana,lblFecha_fin_2))
        self.btnFechaFin.place(x=790, y=60)

        #boton  consultar

        btnConsultar_tabla=Button(self.frameSuperior, text="Consultar")
        btnConsultar_tabla.place(x=915, y=60)
        btnConsultar_tabla.config(fon=("Helvética", 11), command=partial( self.Consultar_tabla_fecha,lblFecha_ini_2,lblFecha_fin_2, self.tabla))


        # ----------------Contenido superior------------


        # ----------------Contenido inferior------------
        tabla.TablaPrincipal()
        # ----------------Contenido inferior------------

        # -----mainloop-----------
        self.ventana.mainloop()
        # -----mainloop-----------

    def salir(self):
        valor = messagebox.askyesno("Salir", "¿deseas salir del programa?")
        if valor:
            self.ventana.quit()



    def get_plantilla(self):
        plantilla = pt.Plantilla()
        plantilla.ventana_Nuevo(self.ventana, self.tabla)

    def Consultar_tabla_fecha(self,Fecha_ini,Fecha_fin,tabla):


        lista_fecha= self.obj_datos_fecha.datos_tabla_fechas(Fecha_ini,Fecha_fin)
        for row in tabla.get_children():
            tabla.delete(row)

        for l in lista_fecha:
            tabla.insert(parent="", index="end", text=l[0], values=(l[1], l[2], l[3], l[4], l[5], l[6], l[7]))
        print(lista_fecha)
