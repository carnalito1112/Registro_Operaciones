from tkinter import *
from tkinter import messagebox
from datetime import date

import Vista.Calendario as c
import Vista.TablaPrincipal as tp


class Principal:
    # ------------variable---------
    fechaTitle = str(date.today())
    # ------------variable---------
    # ----------ventana------
    ventana = Tk()
    ventana.title("Bitacora de trading " + fechaTitle)
    ventana.iconbitmap("Recursos/img/icono.ico")
    ventana.geometry("1024x640")
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

    fechaIni = str(date.today())
    fechaFin = str(date.today())
    btnFechaIni = Button(frameSuperior, text=fechaIni)
    btnFechaFin = Button(frameSuperior, text=fechaFin)

    ##------------variables-----------

    ###Contructor
    def principalVen(self):
        ##-------objetos-----
        calendario = c.Calendarios()
        tabla=tp.Tabla() #ejecutamos el constructor de la clase tabla
        ##-------objetos-----

        # -------menus------
        menubar = Menu(self.ventana)
        self.ventana.config(menu=menubar)
        # -------------filemenu------
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opciones", menu=filemenu)
        filemenu.add_command(label="Saldo")
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
        lblTotal = Label(self.frameSuperior, text="25,550")
        lblTotal.config(fon=("Helvética", 11))
        lblTotal.place(x=300, y=15)

        # label Ganancia/perdida
        lblGanPerLetra = Label(self.frameSuperior, text="Ganancia/Perdida:")
        lblGanPerLetra.config(fon=("Helvética", 11))
        lblGanPerLetra.place(x=420, y=15)

        # label Ganancia/perdida la obtenemos de la siguiene manera saldo original - saldo total hasta hoy
        lblGanPer = Label(self.frameSuperior, text="550")
        lblGanPer.config(fon=("Helvética", 11))
        lblGanPer.place(x=550, y=15)

        # label Ganancia/perdida dia anterior en letra
        lblGanPerDiaLetra = Label(self.frameSuperior, text="Ganancia/Perdida dia anterior:")
        lblGanPerDiaLetra.config(fon=("Helvética", 11))
        lblGanPerDiaLetra.place(x=635, y=15)

        # Label ganancia/perdida de dia anterior
        lblGanPerDia = Label(self.frameSuperior, text="200")
        lblGanPerDia.config(fon=("Helvética", 11))
        lblGanPerDia.place(x=840, y=15)

        # boton nueva operacion
        btnNuevOperacion = Button(self.frameSuperior, text="Nueva Operacion")
        btnNuevOperacion.config(fon=("Helvética", 11))
        btnNuevOperacion.place(x=10, y=60)
        # boton nueva operacion
        lblResultados = Label(self.frameSuperior, text="Resultados de la tabla")
        lblResultados.config(fon=("Helvética", 11))
        lblResultados.place(x=220, y=70)

        # label fecha inicio

        lblFechaIni = Label(self.frameSuperior, text="Fecha inicio:")
        lblFechaIni.config(fon=("Helvética", 11))
        lblFechaIni.place(x=420, y=70)
        # boton fecha de inicio

        self.btnFechaIni.config(fon=("Helvética", 11), command=calendario.ventanaCalIni)
        self.btnFechaIni.place(x=550, y=60)

        # lacel fecha final
        lblFecha2 = Label(self.frameSuperior, text="final:")
        lblFecha2.config(fon=("Helvética", 11))
        lblFecha2.place(x=700, y=70)

        # boton fecha de final

        self.btnFechaFin.config(fon=("Helvética", 11), command=calendario.ventanaCalFin)
        self.btnFechaFin.place(x=780, y=60)
        # ----------------Contenido superior------------


        # -----mainloop-----------
        self.ventana.mainloop()
        # -----mainloop-----------

    def salir(self):
        valor = messagebox.askyesno("Salir", "¿deseas salir del programa?")
        if valor:
            self.ventana.quit()
