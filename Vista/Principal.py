from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import date


class Principal:
    fecha=str(date.today())
    ventana = Tk()
    ventana.title("Bitacora de trading "+fecha)
    ventana.iconbitmap("Recursos/img/icono.ico")
    ventana.geometry("1024x640")

    def ventana_Principal(self):
        #------Frames------
        #superior


        frameSuperior= Frame(self.ventana, width="1000", height="110")
        frameSuperior.pack()

        #inferior
        frameInferior = Frame(self.ventana, width="1000", height="500")
        frameInferior.config(bg="#4BDB6F")
        frameInferior.pack()

        # ------Frames------
        #-------menus------
        menubar = Menu(self.ventana)
        self.ventana.config(menu=menubar)
        #-------------filemenu------
        filemenu= Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Opciones",menu=filemenu)
        filemenu.add_command(label="Saldo")
        filemenu.add_command(label="Contacto")
        filemenu.add_command(label="Salir", command=self.salir)
        # -------------filemenu------

        #----------------contenido------------


        #boton nueva operacion
        btnNuevOperacion = Button(frameSuperior, text="Nueva Operacion")
        btnNuevOperacion.config(fon=("Helvética", 14))
        btnNuevOperacion.place(x=10, y=40)
        # boton nueva operacion
        lblResultados = Label(frameSuperior,text="Resultados de la tabla")
        lblResultados.config(fon=("Helvética", 14))
        lblResultados.place(x=220, y=50)

        #label fecha 1
        lblFechaIni= Label(frameSuperior,text="Fecha inicio:")
        lblFechaIni.config(fon=("Helvética", 14))
        lblFechaIni.place(x=420, y=50)
        #fecha de inicio
        btnFechaIni= Button(frameSuperior,text=self.fecha, command=self.calendario)
        btnFechaIni.config(fon=("Helvética", 14))
        btnFechaIni.place(x=550, y=40)

        #lacel fecha final
        lblFecha2 = Label(frameSuperior, text="final:")
        lblFecha2.config(fon=("Helvética", 14))
        lblFecha2.place(x=700, y=50)

        # fecha de final
        btnFechafin = Button(frameSuperior, text=self.fecha,command=self.calendario)
        btnFechafin.config(fon=("Helvética", 14))
        btnFechafin.place(x=780, y=40)
        # ----------------Contenido------------


        #-----mainloop-----------
        self.ventana.mainloop()
        # -----mainloop-----------

    def salir(self):
        valor = messagebox.askyesno("Salir", "¿deseas salir del programa?")
        if valor:
            self.ventana.quit()

    def calendario(self):
        ventanaCal= Tk()

        #label
        lblFechaIni_Cal= Label(ventanaCal, text="Selecciona una fecha:")
        lblFechaIni_Cal.config(fon=("Helvética", 14))
        lblFechaIni_Cal.grid(row =0, column=0,pady=10, padx=10)
        #calendario
        calendario = Calendar(ventanaCal, selectmode="day", date_pattern="d/m/yyyy")
        calendario.grid(row =1, column=0,pady=10, padx=10)
        #botones








