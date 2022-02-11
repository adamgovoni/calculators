#importing everthing from tkinter
from tkinter import *
#returns a partial function
from functools import partial


#function for when button is pressed it will pass over its value sending it to text field
def button_pressed(value):
    expression_field_value.set(expression_field_value.get() + str(value))

#equal button will evaluate code as a string and return the result to text field
def equals_pressed():
    try:
        result = eval(expression_field_value.get())
        expression_field_value.set(result)
    except ZeroDivisionError:
        expression_field_value.set("Division by zero error")

#Sets text field to empty string; clearing field.
def clear_pressed():
    expression_field_value.set("")


#creating the class for the calculator
if __name__ == "__main__":
    window = Tk()
    window.title("Basic Calculator")

    #creates the window containing the buttons and text field
    expression_field_value = StringVar()
    expression_field = Entry(window, width = 30, textvariable = expression_field_value)
    expression_field.grid(row = 0, column = 0, columnspan = 4)
    
    button_rows = [
        ["1", "2", "3", "*"],
        ["4", "5", "6", "/"],
        ["7", "8", "9", "+"],
        ["0", "-"],
    ]

    #takes nested list and takes the 'buttons' as each row and 'row' as each index of the row
    for row, buttons in enumerate(button_rows): # buttons = ["1", "2", "3", "*"]
        for col, button_value in enumerate(buttons):
            when_pressed = partial(button_pressed, button_value)
            button1 = Button(window, text=button_value, height = 3, width = 3, borderwidth = 1, command = when_pressed)
            button1.grid(row = row + 1, column = col if button_value != "-" else 3, sticky = "ew")


    clear_button = Button(window, text="C", height = 3, width = 3, borderwidth = 1, command = clear_pressed)
    clear_button.grid(row = 4, column = 1, sticky = "ew")

    equals_button = Button(window, text="=", height = 3, width = 3, borderwidth = 1, command = equals_pressed)
    equals_button.grid(row = 4, column = 2, sticky = "ew")

    # when_pressed = partial(button_pressed, "1")
    # button1 = Button(window, text="1", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button1.grid(row = 1, column = 0, sticky = "ew")

    # when_pressed = partial(button_pressed, "2")
    # button2 = Button(window, text="2", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button2.grid(row = 1, column = 1, sticky = "ew")

    # when_pressed = partial(button_pressed, "3")
    # button3 = Button(window, text="3", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button3.grid(row = 1, column = 2, sticky = "ew")

    # when_pressed = partial(button_pressed, "*")
    # multiplication_button = Button(window, text="*", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # multiplication_button.grid(row = 1, column = 3, sticky = "ew")

    # when_pressed = partial(button_pressed, "4")
    # button4 = Button(window, text="4", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button4.grid(row = 2, column = 0, sticky = "ew")

    # when_pressed = partial(button_pressed, "5")
    # button5 = Button(window, text="5", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button5.grid(row = 2, column = 1, sticky = "ew")

    # when_pressed = partial(button_pressed, "6")
    # button6 = Button(window, text="6", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button6.grid(row = 2, column = 2, sticky = "ew")

    # when_pressed = partial(button_pressed, "/")
    # division_button = Button(window, text="/", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # division_button.grid(row = 2, column = 3, sticky = "ew")

    # when_pressed = partial(button_pressed, "7")
    # button7 = Button(window, text="7", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button7.grid(row = 3, column = 0, sticky = "ew")

    # when_pressed = partial(button_pressed, "8")
    # button8 = Button(window, text="8", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button8.grid(row = 3, column = 1, sticky = "ew")

    # when_pressed = partial(button_pressed, "9")
    # button9 = Button(window, text="9", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button9.grid(row = 3, column = 2, sticky = "ew")

    # when_pressed = partial(button_pressed, "+")
    # addition_button = Button(window, text="+", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # addition_button.grid(row = 3, column = 3, sticky = "ew")

    # when_pressed = partial(button_pressed, "0")
    # button0 = Button(window, text="0", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # button0.grid(row = 4, column = 0, sticky = "ew")

    # clear_button = Button(window, text="C", height = 3, width = 3, borderwidth = 1, command = clear_pressed)
    # clear_button.grid(row = 4, column = 1, sticky = "ew")

    # equals_button = Button(window, text="=", height = 3, width = 3, borderwidth = 1, command = equals_pressed)
    # equals_button.grid(row = 4, column = 2, sticky = "ew")

    # when_pressed = partial(button_pressed, "-")
    # subtraction_button = Button(window, text="-", height = 3, width = 3, borderwidth = 1, command = when_pressed)
    # subtraction_button.grid(row = 4, column = 3, sticky = "ew")

    window.mainloop()