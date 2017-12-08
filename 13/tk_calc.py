#! /usr/bin/env python2
# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox


window = Tkinter.Tk()
window.geometry("500x300")

first_label = Tkinter.Label(window, text="Enter the first number")
first_number = Tkinter.Entry(window)
second_label = Tkinter.Label(window, text="Enter the second number")
second_number = Tkinter.Entry(window)

first_label.grid(row=0, column=0)
first_number.grid(row=0, column=1)
second_label.grid(row=3, column=0)
second_number.grid(row=3, column=1)


def get_numbers():
    try:
        x = float(first_number.get())
        y = float(second_number.get())
        return x, y
    except ValueError:
        tkMessageBox.showinfo("Error", "The input has to be numbers.")


def get_sum(x, y):
    return x + y


def get_minus(x, y):
    return x - y


def get_multi(x, y):
    return x * y


def get_div(x, y):
    return x / y


def get_result(operation):
    x, y = get_numbers()
    functions = {
        "+": get_sum,
        "-": get_minus,
        "*": get_multi,
        "/": get_div
    }
    result.set(functions[operation](x, y))


plus_button = Tkinter.Button(
    window, text="+", command=lambda: get_result("+")
)
minus_button = Tkinter.Button(
    window, text="-", command=lambda: get_result("-")
)
multiply_button = Tkinter.Button(
    window, text="*", command=lambda: get_result("*")
)
divide_button = Tkinter.Button(
    window, text="/", command=lambda: get_result("/")
)


plus_button.grid(row=1, column=0)
minus_button.grid(row=1, column=1)
multiply_button.grid(row=2, column=0)
divide_button.grid(row=2, column=1)


result = Tkinter.StringVar()
result_label = Tkinter.Entry(window, textvariable=result)
result_label.grid(row=4, column=0)

if __name__ == "__main__":
    window.mainloop()
