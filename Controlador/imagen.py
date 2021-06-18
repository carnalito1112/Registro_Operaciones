
from tkinter import messagebox

from tkinter import filedialog as fd
from PIL import Image


class imagen:

    def recuperar_img_entrada(self, objeto, label, ventana):
        nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo ",
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

    #abrimos la imagen con esta funcion
    def abrir_imagen_ent(self,dir_imagen):
        try:

            i = Image.open(dir_imagen, "r")
            i.show()
        except FileNotFoundError:

            messagebox.showerror(message="Archivo no encontrado",title="Archivo no encontrado")
            #ventana.wm_attributes("-topmost", True)



    def abrir_imagen_sal(self,objeto):
        try:

            i = Image.open(objeto.get_ruta_img_salida(), "r")
            i.show()
        except FileNotFoundError:

            messagebox.showerror(message="Archivo no encontrado",title="Archivo no encontrado")
            #ventana.wm_attributes("-topmost", True)

