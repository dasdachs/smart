#! /usr/bin/env python2
# -*- coding: utf-8 -*-
import random
import Tkinter
import tkMessageBox


# Secret number constant
SECRET_NUMBER = random.randint(1, 100)
# Tkinter window
window = Tkinter.Tk()
window.geometry("300x300")
# GUI elements
greeting = Tkinter.Label(window, text="Wellcome to the guessing game.")
start = Tkinter.Label(window, text="Guess the secret number!")
guess = Tkinter.Entry(window)
greeting.pack()
start.pack()
guess.pack()


# Button
def check_guess():
    try:
        value = int(guess.get())
        if value == SECRET_NUMBER:
            result_text = "CORRECT!"
        elif value > SECRET_NUMBER:
            result_text = "Your guess is too high."
        else:
            result_text = "Your guess is too low."
    except ValueError:
        result_text = "Enter a integer."
    tkMessageBox.showinfo("Result", result_text)


submit = Tkinter.Button(window, text="Submit", command=check_guess)
submit.pack()

if __name__ == "__main__":
    window.mainloop()
