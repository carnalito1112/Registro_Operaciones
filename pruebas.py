import sqlite3
from PIL import Image
import time


conexion = sqlite3.connect("BD\Trading.db")


cur = conexion.cursor()
cur.execute("SELECT op_id_operacion,op_fecha_entrada,op_fecha_salida,op_operacion,op_gan_per,op_nota,op_ruta_imagen_ent,op_ruta_imagen_sal FROM tb_operaciones ")
rows = cur.fetchall()

print(rows)







#"""ABRIR UNA IMAGEN A COLOR Y A GRISES"""
def abrir_imagen():
    im="C:/Users/PC-Trading/Pictures/cyberpunk-2077.jpg"
    i= Image.open(im,"r")
    i.show()

abrir_imagen()








# import tkinter as tk
# from tkinter import scrolledtext as st
# import sys
# from tkinter import filedialog as fd
# from tkinter import messagebox as mb
#
# class Aplicacion:
#     def __init__(self):
#         self.ventana1=tk.Tk()
#         self.agregar_menu()
#         self.scrolledtext1=st.ScrolledText(self.ventana1, width=80, height=20)
#         self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
#         self.ventana1.mainloop()
#
#     def agregar_menu(self):
#         menubar1 = tk.Menu(self.ventana1)
#         self.ventana1.config(menu=menubar1)
#         opciones1 = tk.Menu(menubar1, tearoff=0)
#         opciones1.add_command(label="Guardar archivo", command=self.guardar)
#         opciones1.add_command(label="Recuperar archivo", command=self.recuperar)
#         opciones1.add_separator()
#         opciones1.add_command(label="Salir", command=self.salir)
#         menubar1.add_cascade(label="Archivo", menu=opciones1)
#
#     def salir(self):
#         sys.exit()
#
#     def guardar(self):
#         nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
#         if nombrearch!='':
#             archi1=open(nombrearch, "w", encoding="utf-8")
#             archi1.write(self.scrolledtext1.get("1.0", tk.END))
#             archi1.close()
#             mb.showinfo("Información", "Los datos fueron guardados en el archivo.")
#
#     def recuperar(self):
#         nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("png files","*.png"),("todos los archivos","*.*")))
#         if nombrearch!='':
#             archi1=open(nombrearch, "r", encoding="utf-8")
#             archi1.close()
#             self.scrolledtext1.delete("1.0", tk.END)
#             print(nombrearch)
#
#
# aplicacion1=Aplicacion()
#
#
#
#












# from tkinter import *
# from tkcalendar import *
#
# ventana = Tk()
# ventana.geometry("600x400")
#
# calendario = Calendar(ventana, selectmode="day", date_pattern="d/m/yyyy")
# calendario.pack(pady=20)
#
#
# def grabar_fecha():
#     fecha = calendario.get_date()
#     my_label.config(text=fecha)
#
#
# my_botton = Button(ventana, text="obtener fecha", command=grabar_fecha)
# my_botton.pack(pady=20)
#
# my_label = Label(ventana, text="")
# my_label.pack(pady=20)
# ventana.mainloop()
#



# from datetime import date
# from datetime import datetime
#
# #Día actual
# today = date.today()
#
# #Fecha actual
# now = datetime.now()
#
# print(today)
# print(now)


# lista = [["id_1","2","3","4","5","6","7","8"],
#         ["id_1","2","3","4","5","6","7","8"],
#         ["id_1","2","3","4","5","6","7","8"]]
#
# #
# # for i in range(len(lista)):
# #     for j in range(0,8):
# #         print((lista[i][j]), end='')
# #         if(lista[i][j]==lista[i][0]):
# #             print((lista[i][j])+"\n")
# #     print()
#
# for i in lista:
#     print(i[0])




















