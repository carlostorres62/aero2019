from tkinter import *


master = Tk()
master.title("Aero Design")
master.geometry("650x500+350+50")

welcome = StringVar()
strLabel1 = Label(master, textvariable=welcome, borderwidth=30, font=("Helvetica", 75), fg="red")
strLabel2 = Label(master, textvariable=welcome, borderwidth=30, font=("Helvetica", 75), fg="blue")
strLabel3 = Label(master, textvariable=welcome, borderwidth=30, font=("Helvetica", 75), fg="green")
strLabel4 = Label(master, textvariable=welcome, borderwidth=30, font=("Helvetica", 75), fg="orange")
strLabel5 = Label(master, textvariable=welcome, borderwidth=30, font=("Helvetica", 75), fg="violet")
strLabel6 = Label(master, textvariable=welcome, borderwidth=30, font=("Helvetica", 75), fg="black")


def start():
    welcome.set("Hello")
    master.after(1500, end)


def end():
    welcome.set("World")
    master.after(1500, start)


def newLabel(label, numRow, numCol):
    label.grid(row=numRow, column=numCol)


newLabel(strLabel1, 0, 0)
newLabel(strLabel2, 1, 0)
newLabel(strLabel3, 2, 0)
newLabel(strLabel4, 0, 1)
newLabel(strLabel5, 1, 1)
newLabel(strLabel6, 2, 1)

start()
mainloop()
