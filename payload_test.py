import tkinter as tk
from tkinter import ttk
from random import *


class Payload:

    def __init__(self, masterPayload):
        self.masterPayload = masterPayload
        self.masterPayload.title("Payloads")
        self.masterPayload.geometry("740x50+300+450")
        self.style = ttk.Style()

        self.altP, self.tP, self.d1, self.d2 = 0, 0, 0, 0

        self.data = ttk.Label(self.masterPayload, text="DATA:", font=("Helvetica", 20))
        self.altitude = ttk.Label(self.masterPayload, text="Altitude:", font=("Helvetica", 20), style="Label")
        self.altitudeVar = ttk.Label(self.masterPayload, text=self.altP, font=("Helvetica", 20))
        self.time = ttk.Label(self.masterPayload, text="Time:", font=("Helvetica", 20), style="Label")
        self.timeVar = ttk.Label(self.masterPayload, text=self.tP, font=("Helvetica", 20))
        self.deploy1 = ttk.Label(self.masterPayload, text="Deploy 1:", font=("Helvetica", 20), style="Label")
        self.deploy1Var = ttk.Label(self.masterPayload, text=self.d1, font=("Helvetica", 20))
        self.deploy2 = ttk.Label(self.masterPayload, text="Deploy 2:", font=("Helvetica", 20), style="Label")
        self.deploy2Var = ttk.Label(self.masterPayload, text=self.d2, font=("Helvetica", 20))

        self.data.grid(row=0, column=0)
        self.altitude.grid(row=0, column=1)
        self.altitudeVar.grid(row=0, column=2)
        self.time.grid(row=0, column=3)
        self.timeVar.grid(row=0, column=4)
        self.deploy1.grid(row=0, column=5)
        self.deploy1Var.grid(row=0, column=6)
        self.deploy2.grid(row=0, column=7)
        self.deploy2Var.grid(row=0, column=8)

    # def update(self):
    #     self.altP.set(randint(0, 100))
    #     self.tP.set(randint(0, 100))
    #     self.d1.set(randint(0, 100))
    #     self.d2.set(randint(0, 100))
    #     self.masterPayload.after(1500, self.update)

    def look(self):
        self.style.configure("Label", foreground="red")


master = Payload(tk.Tk())
# master.update()
master.look()
# tk.mainloop()
