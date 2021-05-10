from tkcalendar import *
from tkinter import *

import Vista.Principal as p


class Calendarios:

    def plantilla_fec_ini(self, ventana, label,objeto):
        # objeto fecha

        ventanaCal = Toplevel(ventana)
        ventanaCal.geometry("270x300")
        ##-------toplavel-------

        # label seleccione fecha
        lblfechaSel = Label(ventanaCal, text="Selecciona una fecha de inicio")
        lblfechaSel.config(fon=("Helvética", 11))
        lblfechaSel.grid(row=0, column=0, pady=10, padx=10)

        # calendario
        calendario = Calendar(ventanaCal, selectmode="day", date_pattern="yyyy-mm-dd")
        calendario.grid(row=1, column=0, pady=10, padx=10)

        def salir():
            fecha = calendario.get_date()
            label.config(text=fecha)
            objeto.set_fecha_ini(fecha)
            ventanaCal.destroy()

        # boton salir
        btnSalirCal = Button(ventanaCal, text="Grabar", command=salir)
        btnSalirCal.config(fon=("Helvética", 11))
        btnSalirCal.grid(row=2, column=0, pady=10, padx=10)



    def plantilla_fec_fin(self, ventana, label,objeto):
        # objeto fecha

        ventanaCal = Toplevel(ventana)
        ventanaCal.geometry("270x300")
        ##-------toplavel-------

        # label seleccione fecha
        lblfechaSel = Label(ventanaCal, text="Selecciona una fecha de inicio")
        lblfechaSel.config(fon=("Helvética", 11))
        lblfechaSel.grid(row=0, column=0, pady=10, padx=10)

        # calendario
        calendario = Calendar(ventanaCal, selectmode="day", date_pattern="yyyy-mm-dd")
        calendario.grid(row=1, column=0, pady=10, padx=10)

        def salir():
            fecha = calendario.get_date()
            label.config(text=fecha)
            objeto.set_fecha_fin(fecha)
            ventanaCal.destroy()

        # boton salir
        btnSalirCal = Button(ventanaCal, text="Grabar", command=salir)
        btnSalirCal.config(fon=("Helvética", 11))
        btnSalirCal.grid(row=2, column=0, pady=10, padx=10)

    def plantilla_fec(self, ventana, label):
        # objeto fecha

        ventanaCal = Toplevel(ventana)
        ventanaCal.geometry("270x300")
        ##-------toplavel-------

        # label seleccione fecha
        lblfechaSel = Label(ventanaCal, text="Selecciona una fecha de inicio")
        lblfechaSel.config(fon=("Helvética", 11))
        lblfechaSel.grid(row=0, column=0, pady=10, padx=10)

        # calendario
        calendario = Calendar(ventanaCal, selectmode="day", date_pattern="yyyy-mm-dd")
        calendario.grid(row=1, column=0, pady=10, padx=10)

        def salir():
            fecha = calendario.get_date()
            label.config(text=fecha)
            ventanaCal.destroy()

        # boton salir
        btnSalirCal = Button(ventanaCal, text="Grabar", command=salir)
        btnSalirCal.config(fon=("Helvética", 11))
        btnSalirCal.grid(row=2, column=0, pady=10, padx=10)