import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import filedialog as fd


class imagen_link:

    def recuperar_img_entrada(self, objeto, label, ventana):
        nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo :D",
                                        filetypes=(("png files", "*.png"), ("todos los archivos", "*.*")),
                                        parent=ventana)
        if nombrearch != '':
            archi1 = open(nombrearch, "r", encoding="utf-8")
            archi1.close()

            # print(nombrearch)
            objeto.set_ruta_img_entrada(nombrearch)
            label.config(text=nombrearch)

    def recuperar_img_salida(self, objeto, label, ventana):
        nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo",
                                        filetypes=(("png files", "*.png"), ("todos los archivos", "*.*")),
                                        parent=ventana)
        if nombrearch != '':
            archi1 = open(nombrearch, "r", encoding="utf-8")
            archi1.close()

            # print(nombrearch)
            objeto.set_ruta_img_salida(nombrearch)
            label.config(text=nombrearch)
