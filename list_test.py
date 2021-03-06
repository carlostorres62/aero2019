import tkinter as tk
from tkinter import ttk
import time
from random import *


class ListTable:

    def __init__(self, masterList):
        self.masterList = masterList
        self.masterList.title("Aero Design")
        self.masterList.geometry("800x357+200+50")  # screen position (x, y)
        self.masterList.resizable(False, False)  # window doesn't resize
        self.style = ttk.Style()

        # scrolls vertically with orient and yscrollcommand function
        self.scrollbar = ttk.Scrollbar(masterList, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(masterList, height=5, columns="One", yscrollcommand=self.scrollbar.set)

        # master variables
        self.cda, self.water, self.shelter = True, False, False
        self.altL, self.weight, self.tL = 0, 0, 0
        self.altP, self.tP, self.d1, self.d2 = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()

        if not self.cda:
            self.cda = "Yes"
        else:
            self.cda = "No"
        if not self.water:
            self.water = "Yes"
        else:
            self.water = "No"
        if not self.shelter:
            self.shelter = "Yes"
        else:
            self.shelter = "No"

        self.flight = [("CDA", self.cda), ("Water", self.water), ("Shelter", self.shelter), ("Altitude", self.altL),
                       ("Weight", self.weight), ("Time", self.tL), ("Test 1", self.cda), ("Test 2", self.cda),
                       ("Test 3", self.altL), ("Test 4", self.altL)]

        self.data = ttk.Label(self.masterList, text="DATA:", font=("Helvetica", 25), style="R.TLabel")
        self.altitude = ttk.Label(self.masterList, text="Altitude:", font=("Helvetica", 20), style="B.TLabel")
        self.altitudeVar = ttk.Label(self.masterList, textvariable=self.altP, font=("Helvetica", 20))
        self.time = ttk.Label(self.masterList, text="Time:", font=("Helvetica", 20), style="B.TLabel")
        self.timeVar = ttk.Label(self.masterList, textvariable=self.tP, font=("Helvetica", 20))
        self.deploy1 = ttk.Label(self.masterList, text="Deploy 1: ", font=("Helvetica", 20), style="B.TLabel")
        self.deploy1Var = ttk.Label(self.masterList, textvariable=self.d1, font=("Helvetica", 20))
        self.deploy2 = ttk.Label(self.masterList, text="Deploy 2:", font=("Helvetica", 20), style="B.TLabel")
        self.deploy2Var = ttk.Label(self.masterList, textvariable=self.d2, font=("Helvetica", 20))

        self.data.place(relx=3/4, rely=0)
        self.altitude.place(relx=3/4, rely=1/5)
        self.altitudeVar.place(relx=0.9, rely=1/5)
        self.time.place(relx=3/4, rely=2/5)
        self.timeVar.place(relx=0.9, rely=2/5)
        self.deploy1.place(relx=3/4, rely=3/5)
        self.deploy1Var.place(relx=0.9, rely=3/5)
        self.deploy2.place(relx=3/4, rely=4/5)
        self.deploy2Var.place(relx=0.9, rely=4/5)

    def table(self):

        # variables set for the table
        self.tree.column("#0", width=275, minwidth=275)
        self.tree.column("#1", width=275, minwidth=275, anchor=tk.CENTER)

        # places the heading on gui
        self.tree.heading("#0", text="Components", anchor=tk.CENTER)
        self.tree.heading("#1", text="Flight 1", anchor=tk.CENTER)

        # places the text and values in the table created
        index = 0
        for string, var in self.flight:
            self.tree.insert("", index, text=string, values=var)
            index += 1

        self.scrollbar.config(command=self.tree.yview)

        self.tree.grid(row=0, column=0)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)
        # positions the scrollbar at the right (sticky=coordinates)

    def update(self):
        self.altP.set(randint(0, 100))
        self.tP.set(randint(0, 100))
        self.d1.set(randint(0, 100))
        self.d2.set(randint(0, 100))
        self.masterList.after(1500, self.update)

    def look(self):
        # sets the style of the strings in Treeview
        self.style.configure("Treeview.Heading", font=("Helvetica", 35))  # style for the heading
        self.style.configure("Treeview", font=("Helvetica", 30), rowheight=60)  # style for the rest of the table
        self.style.configure("B.TLabel", foreground="Blue")
        self.style.configure("R.TLabel", foreground="Red")


master = ListTable(tk.Tk())
master.table()
master.look()
master.update()
tk.mainloop()
