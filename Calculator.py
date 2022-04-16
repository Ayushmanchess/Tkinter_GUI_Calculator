from tkinter import *


def add():

    First_number = float(e1.get())
    Second_number = float(e2.get())
    e3.delete(0, END)
    e3.insert(0, First_number + Second_number)

def sub():

    First_number = float(e1.get())
    Second_number = float(e2.get())
    e3.delete(0, END)
    e3.insert(0, First_number - Second_number)

def mul():

    First_number = float(e1.get())
    Second_number = float(e2.get())
    e3.delete(0, END)
    e3.insert(0, First_number * Second_number)

def div():

    First_number = float(e1.get())
    Second_number = float(e2.get())
    e3.delete(0, END)
    e3.insert(0, First_number / Second_number)            

root = Tk()
root.geometry("350x200")
root.title("Calculator")

e1 = Entry(root, width=35, borderwidth=5)
e1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e1.insert(0, "0")

e2 = Entry(root, width=35, borderwidth=5)
e2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
e2.insert(0, "0")


add = Button(root, text="Add", padx=10, pady=10, command=add)
add.grid(row=3, column=0)

sub = Button(root, text="Subtract", padx=10, pady=10, command=sub)
sub.grid(row=3, column=1)

mul = Button(root, text="Multiply", padx=10, pady=10, command=mul)
mul.grid(row=3, column=2)

div = Button(root, text="Divide", padx=10, pady=10, command=div)
div.grid(row=3, column=3)

e3 = Entry(root, width=35, borderwidth=5, font=("Arial", 10))
e3.grid(row=4, column=0, columnspan=3, padx=10, pady=20)
e3.insert(0, "0")

root.mainloop()