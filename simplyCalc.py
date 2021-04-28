#!usr/bin/python3
# Simple tkinter Calculator

from tkinter import *
from tkinter import font as tkFont


# Clear function
def clearScreen():
    display.set("")


# Display function
def dataDisplay(key):
    if display.get() == "ERROR":
        clearScreen()
    word = display.get() + key
    display.set(word)


# Answer function
def calculate():
    try:
        word = eval(display.get())
        display.set(word)
    except:
        word = "ERROR"
        display.set(word)


root = Tk()

# Geometry settings
root.geometry("260x256")
root.title("Calc")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)

# Font
text_font = tkFont.Font(family='Arial', size=15, weight=tkFont.NORMAL)

# Display
display = StringVar()
display_area = Entry(root, width=46, bd=15, textvariable=display, relief=FLAT,
                     justify="right", font=text_font, bg="gray80")
display_area.grid(row=0, column=0, columnspan=4)

# First row
percent_btn = Button(root, text="%", width=5, font=text_font, relief=FLAT,
                     bg="light grey", fg="black", command=lambda: dataDisplay(" / 100"))
percent_btn.grid(row=1, column=0, sticky="E")

pow_of_two_btn = Button(root, text="x^2", width=5, font=text_font, relief=FLAT,
                        bg="light grey", fg="black", command=lambda: dataDisplay(" ** 2"))
pow_of_two_btn.grid(row=1, column=1, sticky="w")

clear_btn = Button(root, text="Clear", width=11, font=text_font, relief=FLAT,
                 bg="dark grey", command=clearScreen)
clear_btn.grid(row=1, column=2, columnspan=2)

# Second row
seven_btn = Button(root, text="7", width=5, font=text_font, relief=FLAT,
                   bg="ghost white", fg="black", command=lambda: dataDisplay("7"))
seven_btn.grid(row=2, column=0, sticky="e")

eight_btn = Button(root, text="8", width=5, font=text_font, relief=FLAT,
                   bg="ghost white", fg="black", command=lambda: dataDisplay("8"))
eight_btn.grid(row=2, column=1, sticky="w")

nine_btn = Button(root, text="9", width=5, font=text_font, relief=FLAT,
                  bg="ghost white", fg="black", command=lambda: dataDisplay("9"))
nine_btn.grid(row=2, column=2)

division_btn = Button(root, text="/", width=5, font=text_font, relief=FLAT,
                    bg="light grey", fg="black", command=lambda: dataDisplay("/"))
division_btn.grid(row=2, column=3)

# Third row
four_btn = Button(root, text="4", width=5, font=text_font, relief=FLAT,
                  bg="ghost white", fg="black", command=lambda: dataDisplay("4"))
four_btn.grid(row=3, column=0, sticky="e")

five_btn = Button(root, text="5", width=5, font=text_font, relief=FLAT,
                  bg="ghost white", fg="black", command=lambda: dataDisplay("5"))
five_btn.grid(row=3, column=1, sticky="w")

six_btn = Button(root, text="6", width=5, font=text_font, relief=FLAT,
                 bg="ghost white", fg="black", command=lambda: dataDisplay("6"))
six_btn.grid(row=3, column=2)

multi_btn = Button(root, text="*", width=5, font=text_font, relief=FLAT,
                 bg="light grey", fg="black", command=lambda: dataDisplay("*"))
multi_btn.grid(row=3, column=3)

# Fourth row
one_btn = Button(root, text="1", width=5, font=text_font, relief=FLAT,
                 bg="ghost white", fg="black", command=lambda: dataDisplay("1"))
one_btn.grid(row=4, column=0, sticky="e")

two_btn = Button(root, text="2", width=5, font=text_font, relief=FLAT,
                 bg="ghost white", fg="black", command=lambda: dataDisplay("2"))
two_btn.grid(row=4, column=1, sticky="w")

three_btn = Button(root, text="3", width=5, font=text_font, relief=FLAT,
                   bg="ghost white", fg="black", command=lambda: dataDisplay("3"))
three_btn.grid(row=4, column=2)

minus_btn = Button(root, text="-", width=5, font=text_font, relief=FLAT,
                   bg="light grey", fg="black", command=lambda: dataDisplay("-"))
minus_btn.grid(row=4, column=3)

# Fifth row
dot_btn = Button(root, text=".", width=5, font=text_font, relief=FLAT,
                 bg="ghost white", fg="black", command=lambda: dataDisplay("."))
dot_btn.grid(row=5, column=0, sticky="e")

zero_btn = Button(root, text="0", width=5, font=text_font, relief=FLAT,
                  bg="ghost white", fg="black", command=lambda: dataDisplay("0"))
zero_btn.grid(row=5, column=1, sticky="w")

equal_btn = Button(root, text="=", width=5, bg="light sky blue", relief=FLAT,
                   fg="white", font=text_font, command=calculate)
equal_btn.grid(row=5, column=2)

plus_btn = Button(root, text="+", width=5, font=text_font, relief=FLAT,
                  bg="light grey", fg="black", command=lambda: dataDisplay("+"))
plus_btn.grid(row=5, column=3)

root.mainloop()
