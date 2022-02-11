from tkinter import *

if __name__ == "__main__":
    window = Tk()
    window.title("Basic Calculator")
    
    expression_field = Entry(window, width = 30)
    expression_field.grid(row = 0, column = 0, columnspan = 4)
    
    button1 = Button(window, text="1", height = 3, width = 3, borderwidth = 1)
    button1.grid(row = 1, column = 0, sticky = "ew")

    window.mainloop()