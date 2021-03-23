from tkinter import *
from tkinter import messagebox

class Principal:
    ventana = Tk()
    ventana.title("Bitacora de trading")
    ventana.iconbitmap("Recursos/img/icono.ico")
    ventana.geometry("1024x640")

    def ventana_Principal(self):
        #------Frames------
        #superior
        frameSuperior= Frame(self.ventana, width="1000", height="200")
        frameSuperior.config(bg="#B2CEFA")
        frameSuperior.pack()

        #inferior
        frameInferior = Frame(self.ventana, width="1000", height="400")
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
        btnNuevOperacion.place(y=60, x=35)
        # boton nueva operacion
        lblResultados = Label(frameSuperior,text="Resultados de la tabla:")
        lblResultados.config(fon=("Helvética", 14))
        lblResultados.place(y=70, x=250)
        # ----------------Contenido------------
        #-----mainloop-----------
        self.ventana.mainloop()
        # -----mainloop-----------
    def salir(self):
        valor = messagebox.askyesno("Salir", "¿deseas salir del programa?")
        if valor:
            self.ventana.quit()







