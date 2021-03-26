from tkinter import ttk

import Vista.Principal as p

class Tabla:

    def __init__(self):

        #-------variables------
        #objeto de la clase principal
        principal= p.Principal()
        tabla=ttk.Treeview(principal.frameInferior, columns=[f"#{n}" for n in range(1, 9)])
        tabla.pack()
        # -------variables------
        #------contenido------

        tabla.heading("#0", text="N.operacion")
        tabla.heading("#1", text="Fecha entrada")
        tabla.heading("#2", text="Fecha salida")
        tabla.heading("#3", text="C/V")
        tabla.heading("#4", text="Gan/Per")
        tabla.heading("#5", text="Nota")
        tabla.heading("#6", text="Img entrada")
        tabla.heading("#7", text="Img salida")
        tabla.heading("#8", text="Editar")
        ##------le damos tamaño a la columnas
        for i in range(0,9):
            tabla.column("#"+str(i),width="110")
            print(i)
        ##------le damos tamaño a la columnas

        ###--------------------Contenido de la tabla-------
        tabla.insert(parent="",index="end", iid=0,values=("1","2","3","4","5","6","7","8"))

        ###--------------------Contenido de la tabla-------
        # ------contenido------