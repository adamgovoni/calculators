from __future__ import division
from tkinter import *
from turtle import clear

if __name__ == "__main__":
    window = Tk()
    window.title("Basic Calculator")
    
    expression_field = Entry(window, width = 30)
    expression_field.grid(row = 0, column = 0, columnspan = 4)
    
    button1 = Button(window, text="1", height = 3, width = 3, borderwidth = 1)
    button1.grid(row = 1, column = 0, sticky = "ew")

    button2 = Button(window, text="2", height = 3, width = 3, borderwidth = 1)
    button2.grid(row = 1, column = 1, sticky = "ew")

    button3 = Button(window, text="3", height = 3, width = 3, borderwidth = 1)
    button3.grid(row = 1, column = 2, sticky = "ew")

    multiplication = Button(window, text="*", height = 3, width = 3, borderwidth = 1)
    multiplication.grid(row = 1, column = 3, sticky = "ew")

    button4 = Button(window, text="4", height = 3, width = 3, borderwidth = 1)
    button4.grid(row = 2, column = 0, sticky = "ew")

    button5 = Button(window, text="5", height = 3, width = 3, borderwidth = 1)
    button5.grid(row = 2, column = 1, sticky = "ew")

    button6 = Button(window, text="6", height = 3, width = 3, borderwidth = 1)
    button6.grid(row = 2, column = 2, sticky = "ew")

    division = Button(window, text="/", height = 3, width = 3, borderwidth = 1)
    division.grid(row = 2, column = 3, sticky = "ew")

    button7 = Button(window, text="7", height = 3, width = 3, borderwidth = 1)
    button7.grid(row = 3, column = 0, sticky = "ew")

    button8 = Button(window, text="8", height = 3, width = 3, borderwidth = 1)
    button8.grid(row = 3, column = 1, sticky = "ew")

    button9 = Button(window, text="9", height = 3, width = 3, borderwidth = 1)
    button9.grid(row = 3, column = 2, sticky = "ew")

    addition = Button(window, text="+", height = 3, width = 3, borderwidth = 1)
    addition.grid(row = 3, column = 3, sticky = "ew")

    button0 = Button(window, text="0", height = 3, width = 3, borderwidth = 1)
    button0.grid(row = 4, column = 0, sticky = "ew")

    clear = Button(window, text="C", height = 3, width = 3, borderwidth = 1)
    clear.grid(row = 4, column = 1, sticky = "ew")

    equals = Button(window, text="=", height = 3, width = 3, borderwidth = 1)
    equals.grid(row = 4, column = 2, sticky = "ew")

    subtraction = Button(window, text="-", height = 3, width = 3, borderwidth = 1)
    subtraction.grid(row = 4, column = 3, sticky = "ew")

    window.mainloop()