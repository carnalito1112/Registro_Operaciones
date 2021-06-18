
from tkinter import *
from datetime import date
from tkinter import ttk, messagebox
from sys import version_info



if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

from functools import partial

import Vista.Calendario as cal
import Modelo.Mod_operacion as Mop
import Controlador.imagen as ctrl_img
import Controlador.Registros as reg
import Controlador.DatosPrueba as datos_prue

class Plantilla:

    obj_img=ctrl_img.imagen()
    obj_registro=reg.ControlRegistros()
    obj_datos=datos_prue.ConEntrada()

    def ventana_Editar(self,item, ventana,tabla):
        #nueva operacion objeto
        obj_nuevo=Mop.Operacion()
        print(item)


        ##ventana
        venEntrada = Toplevel(ventana)
        # venEntrada.geometry("800x500")

        # declaracion de variables


        # objeto de la clase
        obj_calendario = cal.Calendarios()
        # objeto de la clase

        #asignamos a objeto registro fechas
        obj_nuevo.set_fecha_ini(item[0][1])
        obj_nuevo.set_fecha_fin(item[0][2])

        #asignamos al objeto la imagen de entrada
        obj_nuevo.set_ruta_img_entrada(item[0][6])
        obj_nuevo.set_ruta_img_salida(item[0][7])


        # botones declaracion
        btn_fecha_inicio = Button(venEntrada)
        btn_fecha_fin = Button(venEntrada)
        btn_guardar_registro = Button(venEntrada)
        btn_cancelar=Button(venEntrada)
        btn_img_entrada=Button(venEntrada)
        btn_img_salida = Button(venEntrada)
        # ----------contenido

        lbl_fecha_inicio = Label(venEntrada, text="Fecha entada:")
        lbl_fecha_inicio.config(fon=("Helvética", 11))
        lbl_fecha_inicio.grid(row=0, column=0, pady=10, padx=10)

        lbl_fecha_inicio_2 = Label(venEntrada, text=item[0][1])
        lbl_fecha_inicio_2.config(fon=("Helvética", 11))
        lbl_fecha_inicio_2.grid(row=0, column=1, pady=10, padx=10)

        # boton

        btn_fecha_inicio.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec_ini,venEntrada,lbl_fecha_inicio_2,obj_nuevo))
        btn_fecha_inicio.grid(row=0, column=2, pady=10, padx=10)

        lbl_fecha_fin = Label(venEntrada, text="Fecha entada:")
        lbl_fecha_fin.config(fon=("Helvética", 11))
        lbl_fecha_fin.grid(row=1, column=0, pady=10, padx=10)

        lbl_fecha_fin_2 = Label(venEntrada, text=item[0][2])
        lbl_fecha_fin_2.config(fon=("Helvética", 11))
        lbl_fecha_fin_2.grid(row=1, column=1, pady=10, padx=10)
        # boton

        btn_fecha_fin.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec_fin,venEntrada,lbl_fecha_fin_2,obj_nuevo))
        btn_fecha_fin.grid(row=1, column=2, pady=10, padx=10)

        lbl_desplegable = Label(venEntrada, text="Operacion: ")
        lbl_desplegable.config(fon=("Helvética", 11))
        lbl_desplegable.grid(row=2, column=0, pady=10, padx=10)

        lista_desple = ttk.Combobox(venEntrada, width=17)
        lista_desple.grid(row=2, column=1, pady=10, padx=10)
        if item[0][3]=="compra":
            opciones = ["compra", "venta"]
            lista_desple['values'] = opciones
            lista_desple.current(0)

        if item[0][3]=="venta":
            opciones = ["venta", "compra"]
            lista_desple['values'] = opciones
            lista_desple.current(0)

        #lbl de ganancia o perdida
        lbl_gan_per = Label(venEntrada, text="Ganancia o perdida")
        lbl_gan_per.config(fon=("Helvética", 11))
        lbl_gan_per.grid(row=3, column=0, pady=10, padx=10)

        txt_gan_per=Entry(venEntrada)
        txt_gan_per.insert(tk.END,item[0][4])
        txt_gan_per.config(fon=("Helvética", 11))
        txt_gan_per.grid(row=3, column=1, pady=10, padx=10)


        #imagen de entrada lbl
        lbl_img_ent=Label(venEntrada,text="Imagen entrada")
        lbl_img_ent.config(fon=("Helvética", 11))
        lbl_img_ent.grid(row=4, column=0, pady=10, padx=10)

        #imagen de direccion entrada lbl
        lbl_img_dir_entrada=Label(venEntrada,text=item[0][6])
        lbl_img_dir_entrada.config(fon=("Helvética", 11))
        lbl_img_dir_entrada.grid(row=4, column=1, pady=10, padx=10)

        #btn imagen de entrada
        btn_img_entrada.config(fon=("Helvética", 11), text="Seleccionar",command=partial(self.obj_img.recuperar_img_entrada,obj_nuevo,lbl_img_dir_entrada,venEntrada))
        btn_img_entrada.grid(row=4, column=2, pady=10, padx=10)

        #btn abrir imagen de entrada
        btn_abrir_img_ent=Button(venEntrada)
        btn_abrir_img_ent.config(fon=("Helvética", 11), text="Abrir",command=partial(self.obj_img.abrir_imagen_ent,item[0][6]))
        btn_abrir_img_ent.grid(row=4, column=3, pady=10, padx=10)

        # imagen de salida lbl
        lbl_img_sal = Label(venEntrada, text="Imagen entrada")
        lbl_img_sal.config(fon=("Helvética", 11))
        lbl_img_sal.grid(row=5, column=0, pady=10, padx=10)

        # imagen de direccion salida lbl
        lbl_img_dir_salida = Label(venEntrada,text=item[0][7])
        lbl_img_dir_salida.config(fon=("Helvética", 11))
        lbl_img_dir_salida.grid(row=5, column=1, pady=10, padx=10)

        # btn imagen de salida
        btn_img_salida.config(fon=("Helvética", 11), text="Seleccionar",command=partial(self.obj_img.recuperar_img_salida,obj_nuevo,lbl_img_dir_salida,venEntrada))
        btn_img_salida.grid(row=5, column=2, pady=10, padx=10)

        # btn abrir imagen de salida
        btn_abrir_img_sal = Button(venEntrada)
        btn_abrir_img_sal.config(fon=("Helvética", 11), text="Abrir",command=partial(self.obj_img.abrir_imagen_sal, obj_nuevo))
        btn_abrir_img_sal.grid(row=5, column=3, pady=10, padx=10)
        btn_abrir_img_sal.grid(row=5, column=3, pady=10, padx=10)

        # campo de texto LBL
        lbl_campo_texto = Label(venEntrada, text="Nota: ")
        lbl_campo_texto.config(fon=("Helvética", 11))
        lbl_campo_texto.grid(row=6, column=0, pady=10, padx=10)

        # campo de texto
        campotexto = Text(venEntrada)
        campotexto.insert(1.0,item[0][5])
        campotexto.grid(row=7, column=0, pady=10, padx=10, columnspan=2)
        campotexto.config(width=30, height=10)

        def guardar():
            valor = messagebox.askyesno("Guardar", "¿deseas guardarlo?")
            if valor:
                obj_nuevo.set_operacion(lista_desple.get())
                obj_nuevo.set_nota(campotexto.get("1.0", "end"))
                gan_per=txt_gan_per.get()
                try:
                    float(gan_per)
                    obj_nuevo.set_gan_perd(gan_per)
                except:
                    messagebox.showerror(title="Error en ganacia, perdida", message="El campo ganancia o perdida solo debe contener numeros")
                    venEntrada.destroy()

                #borramos la tabla
                for row in tabla.get_children():
                    tabla.delete(row)
                    # items.append(l[0])
                print(item[0][0])
                self.obj_registro.editar_registro(obj_nuevo,item[0][0])

                #reinsertamos datos en la tabla
                lista = self.obj_datos.datos_tabla()
                for l in lista:
                    tabla.insert(parent="", index="end", text=l[0], values=(l[1], l[2], l[3], l[4], l[5], l[6], l[7]))
                venEntrada.destroy()
            else:
                venEntrada.destroy()



        btn_guardar_registro.config(fon=("Helvética", 11), text="guadar", command=guardar)
        btn_guardar_registro.grid(row=8, column=1, pady=10, padx=10, columnspan=2)

        def salir():
            valor = messagebox.askyesno("Salir", "¿deseas salir?")
            if valor:
                venEntrada.destroy()
            else:
                venEntrada.wm_attributes("-topmost", True)




        btn_cancelar.config(fon=("Helvética", 11), text="Cancelar", command=salir)
        btn_cancelar.grid(row=8, column=2, pady=10, padx=10, columnspan=2)




    def ventana_Nuevo(self, ventana, tabla):
        #nueva operacion objeto
        obj_nuevo=Mop.Operacion()


        ##ventana
        venEntrada = Toplevel(ventana)
        # venEntrada.geometry("800x500")

        # declaracion de variables
        fecha_ini = str(date.today())
        fecha_fin = "0000-00-00"



        # objeto de la clase
        obj_calendario = cal.Calendarios()
        # objeto de la clase

        #asignamos a objeto registro fechas
        obj_nuevo.set_fecha_ini(fecha_ini)
        obj_nuevo.set_fecha_fin(fecha_fin)

        # asignamos una rutaa a ruta_img_salida
        obj_nuevo.set_ruta_img_salida("/root")

        # botones declaracion
        btn_fecha_inicio = Button(venEntrada)
        btn_guardar_registro = Button(venEntrada)
        btn_cancelar=Button(venEntrada)
        btn_img_entrada=Button(venEntrada)
        # ----------contenido

        lbl_fecha_inicio = Label(venEntrada, text="Fecha entada:")
        lbl_fecha_inicio.config(fon=("Helvética", 11))
        lbl_fecha_inicio.grid(row=0, column=0, pady=10, padx=10)

        lbl_fecha_inicio_2 = Label(venEntrada, text=fecha_ini)
        lbl_fecha_inicio_2.config(fon=("Helvética", 11))
        lbl_fecha_inicio_2.grid(row=0, column=1, pady=10, padx=10)

        # boton

        btn_fecha_inicio.config(fon=("Helvética", 11), text="Cambiar", command=partial(obj_calendario.plantilla_fec_ini,venEntrada,lbl_fecha_inicio_2,obj_nuevo))
        btn_fecha_inicio.grid(row=0, column=2, pady=10, padx=10)

        #lista desplegable lbl
        lbl_desplegable = Label(venEntrada, text="Operacion: ")
        lbl_desplegable.config(fon=("Helvética", 11))
        lbl_desplegable.grid(row=2, column=0, pady=10, padx=10)

        lista_desple = ttk.Combobox(venEntrada, width=17)
        lista_desple.grid(row=2, column=1, pady=10, padx=10)
        opciones = ["compra", "venta"]
        lista_desple['values'] = opciones
        lista_desple.current(1)


        # imagen de entrada lbl
        lbl_img_ent = Label(venEntrada, text="Imagen entrada")
        lbl_img_ent.config(fon=("Helvética", 11))
        lbl_img_ent.grid(row=3, column=0, pady=10, padx=10)

        # imagen de direccion entrada lbl
        lbl_img_dir_entrada = Label(venEntrada)
        lbl_img_dir_entrada.config(fon=("Helvética", 11))
        lbl_img_dir_entrada.grid(row=3, column=1, pady=10, padx=10)

        # btn imagen de salida
        btn_img_entrada.config(fon=("Helvética", 11), text="Seleccionar",command=partial(self.obj_img.recuperar_img_entrada,obj_nuevo,lbl_img_dir_entrada,venEntrada))
        btn_img_entrada.grid(row=3, column=2, pady=10, padx=10, columnspan=2)


        # campo de texto LBL
        lbl_campo_texto = Label(venEntrada, text="Nota: ")
        lbl_campo_texto.config(fon=("Helvética", 11))
        lbl_campo_texto.grid(row=4, column=0, pady=10, padx=10)

        # campo de texto
        campotexto = Text(venEntrada)
        campotexto.grid(row=4, column=1, pady=10, padx=10, columnspan=2)
        campotexto.config(width=30, height=10)

        def guardar():
            valor = messagebox.askyesno("Guardar", "¿deseas guardarlo?")
            if valor:
                obj_nuevo.set_operacion(lista_desple.get())
                obj_nuevo.set_nota(campotexto.get("1.0","end"))

                for row in tabla.get_children():
                    tabla.delete(row)
                    #items.append(l[0])

                self.obj_registro.nuevo_registro(obj_nuevo)

                lista= self.obj_datos.datos_tabla()
                for l in lista:
                    tabla.insert(parent="", index="end", text=l[0], values=(l[1], l[2], l[3], l[4], l[5], l[6], l[7]))
                venEntrada.destroy()
            else:
                venEntrada.destroy()

        btn_guardar_registro.config(fon=("Helvética", 11), text="guadar", command=guardar)
        btn_guardar_registro.grid(row=6, column=1, pady=10, padx=10, columnspan=2)

        def salir():
            valor = messagebox.askyesno("Salir", "¿deseas salir?")
            if valor:
                venEntrada.quit()
            else:
                venEntrada.wm_attributes("-topmost", True)

        btn_cancelar.config(fon=("Helvética", 11), text="Cancelar", command=salir)
        btn_cancelar.grid(row=6, column=2, pady=10, padx=10, columnspan=2)



