from tkcalendar import *
from tkinter import *
import Vista.Principal as p


class Calendarios:

    def ventanaCalIni(self):
        # -------toplavel-------
        ventanaCal = Toplevel()
        ventanaCal.geometry("270x300")
        ##-------toplavel-------

        # objeto de la clase VenPrincipal
        venPrin = p.Principal()
        # objeto de la clase VenPrincipal

        # label seleccione fecha
        lblfechaSel = Label(ventanaCal, text="Selecciona una fecha de inicio")
        lblfechaSel.config(fon=("Helvética", 11))
        lblfechaSel.grid(row=0, column=0, pady=10, padx=10)

        # calendario
        calendario = Calendar(ventanaCal, selectmode="day", date_pattern="d/m/yyyy")
        calendario.grid(row=1, column=0, pady=10, padx=10)

        def salir():
            venPrin.fechaIni = calendario.get_date()
            venPrin.btnFechaIni.config(text=venPrin.fechaIni)
            ventanaCal.destroy()

        # boton salir
        btnSalirCal = Button(ventanaCal, text="Salir", command=salir)
        btnSalirCal.config(fon=("Helvética", 11))
        btnSalirCal.grid(row=2, column=0, pady=10, padx=10)

        # MainLoop
        ventanaCal.mainloop()
