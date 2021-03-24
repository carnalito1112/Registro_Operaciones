
from tkinter import *
from tkcalendar import *



ventana = Tk()
ventana.geometry("600x400")


calendario = Calendar(ventana, selectmode="day", date_pattern="d/m/yyyy")
calendario.pack(pady=20)

def grabar_fecha():
    fecha=calendario.get_date()
    my_label.config(text=fecha )

my_botton= Button(ventana, text= "obtener fecha", command=grabar_fecha)
my_botton.pack(pady=20)

my_label = Label(ventana, text="")
my_label.pack(pady=20)
ventana.mainloop()




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


