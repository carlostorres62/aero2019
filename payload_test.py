from tkinter import *
from random import *

master = Tk()
master.title("Payloads")
master.geometry("740x50+300+450")

alt, t, d1, d2 = StringVar(), StringVar(), StringVar(), StringVar()

data = Label(master, text="DATA:", borderwidth=10, font=("Helvetica", 20), fg="red")
altitude = Label(master, text="Altitude:", borderwidth=1, font=("Helvetica", 20), fg="black")
altitudeVar = Label(master, textvariable=alt, borderwidth=10, font=("Helvetica", 20), fg="blue")
time = Label(master, text="Time:", borderwidth=1, font=("Helvetica", 20), fg="black")
timeVar = Label(master, textvariable=t, borderwidth=10, font=("Helvetica", 20), fg="blue")
deploy1 = Label(master, text="Deploy 1:", borderwidth=1, font=("Helvetica", 20), fg="black")
deploy1Var = Label(master, textvariable=d1, borderwidth=10, font=("Helvetica", 20), fg="blue")
deploy2 = Label(master, text="Deploy 2:", borderwidth=1, font=("Helvetica", 20), fg="black")
deploy2Var = Label(master, textvariable=d2, borderwidth=10, font=("Helvetica", 20), fg="blue")


def update():
    alt.set(randint(0, 100))
    t.set(randint(0, 100))
    d1.set(randint(0, 100))
    d2.set(randint(0, 100))
    master.after(1500, update)


def newLabel(label, numRow, numCol):
    label.grid(row=numRow, column=numCol)


newLabel(data, 0, 0)
newLabel(altitude, 0, 1)
newLabel(altitudeVar, 0, 2)
newLabel(time, 0, 3)
newLabel(timeVar, 0, 4)
newLabel(deploy1, 0, 5)
newLabel(deploy1Var, 0, 6)
newLabel(deploy2, 0, 7)
newLabel(deploy2Var, 0, 8)

update()
# mainloop()
