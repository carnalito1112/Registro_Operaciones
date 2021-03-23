# -*- coding: utf-8 -*-

# Simple calendario con tkinter

from calendar import *
from tkinter import *
from datetime import *

# Obtenemos los valores del año y mes a mostrar
today = date.today()
year = format(today.month)
month = format(today.year)


def writeCalendar(year, month):
    # Asignamos el año y mes al calendario
    str1 = calendar.month(year, month)

    label1.configure(text=str1)


def mesAnterior():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1

    writeCalendar(year, month)


def mesSiguiente():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1

    writeCalendar(year, month)


root = Tk()
root.title("Calendario")

# Lo posicionamos en un label
label1 = Label(root, text="", font=('courier', 14, 'bold'), bg='white', justify=LEFT)
label1.grid(row=1, column=1)

# ponemos los botones dentro un Frame
frame = Frame(root, bd=5)
anterior = Button(frame, text="Anterior", command=mesAnterior)
anterior.grid(row=1, column=1, sticky=W)
siguiente = Button(frame, text="Siguiente", command=mesSiguiente)
siguiente.grid(row=1, column=2)
frame.grid(row=2, column=1)

writeCalendar(year, month)

# ejecutamos el evento loop
root.mainloop()