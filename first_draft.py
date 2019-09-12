import tkinter as tk
from tkinter import ttk
import time
import datetime as dt
from random import *


class Draft1:
    def __init__(self, master):
        self.master = master
        self.master.title("Aero Design")
        self.master.geometry("1000x425+125+50")
        self.master.resizable(False, False)

        self.scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(master, height=5, columns=5, yscrollcommand=self.scrollbar.set)
        self.start_time = time.time()

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(None, 15))   # Configures the size of the headings

        self.height = 20         # Sets height size for tree
        self.tree["height"] = self.height
        self.tree["columns"] = ("one", "two", "three", "four", "five", "six")
        self.tree.heading("#0", text="Data", anchor=tk.CENTER)
        self.tree.heading("one", text="Time", anchor=tk.CENTER)
        self.tree.heading("two", text="Altitude", anchor=tk.CENTER)
        self.tree.heading("three", text="CDA", anchor=tk.CENTER)
        self.tree.heading("four", text="Water", anchor=tk.CENTER)
        self.tree.heading("five", text="Shelter", anchor=tk.CENTER)
        self.tree.heading("six", text="Weight", anchor=tk.CENTER)

        # Carlos
        self.altP, self.tP, self.d1, self.d2 = tk.IntVar(), tk.StringVar(), tk.IntVar(), tk.IntVar()

        self.data = ttk.Label(master, text="DATA:", font=("Helvetica", 25), style="R.TLabel")
        self.altitude = ttk.Label(master, text="Altitude:", font=("Helvetica", 20), style="B.TLabel")
        self.altitudeVar = ttk.Label(master, textvariable=self.altP, font=("Helvetica", 20))
        self.timeLabel = ttk.Label(master, text="Time:", font=("Helvetica", 20), style="B.TLabel")
        self.timeVar = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 20))
        self.deploy1 = ttk.Label(master, text="Deploy 1: ", font=("Helvetica", 20), style="B.TLabel")
        self.deploy1Var = ttk.Label(master, textvariable=self.d1, font=("Helvetica", 20))
        self.deploy2 = ttk.Label(master, text="Deploy 2:", font=("Helvetica", 20), style="B.TLabel")
        self.deploy2Var = ttk.Label(master, textvariable=self.d2, font=("Helvetica", 20))

        self.style.configure("B.TLabel", foreground="Blue")
        self.style.configure("R.TLabel", foreground="Red")

        self.hour = 0
        self.minute = 0
        self.second = 0
        self.hTime = str(self.hour)
        self.mTime = str(self.minute)
        self.sTime = str(self.second)
        self.strTime = ""
        self.list = []

        self.data.place(relx=3 / 4, rely=0.05)
        self.altitude.place(relx=3 / 4, rely=1 / 5)
        self.altitudeVar.place(relx=0.9, rely=1 / 5)
        self.timeLabel.place(relx=3 / 4, rely=2 / 5)
        self.timeVar.place(relx=0.85, rely=2 / 5)
        self.deploy1.place(relx=3 / 4, rely=3 / 5)
        self.deploy1Var.place(relx=0.9, rely=3 / 5)
        self.deploy2.place(relx=3 / 4, rely=4 / 5)
        self.deploy2Var.place(relx=0.9, rely=4 / 5)

        # David
        col_width = 100
        self.tree.column("#0", anchor=tk.CENTER, width=col_width-50)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=col_width)

        self.scrollbar.config(command=self.tree.yview)

        self.tree.grid(row=0, column=0, sticky=tk.W)  # positions the scrollbar at the right (sticky = coordinates)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)

    def real_time(self):
        self.hour = dt.datetime.now().hour  # Obtains the current hour
        self.minute = dt.datetime.now().minute  # Obtains the current minute
        self.second = dt.datetime.now().second  # Obtains the current second
        self.hTime = str(self.hour)
        if self.minute < 10:
            # Concatenate a 0 in front of number in case it is a single digit number
            self.mTime = "0" + str(self.minute)
        else:
            self.mTime = str(self.minute)
        if self.second < 10:
            self.sTime = "0" + str(self.second)  # If second is 5 it would show "05"
        else:
            self.sTime = str(self.second)
        self.list = [(self.hTime, self.mTime, self.sTime)]  # Stores the actual time in time list
        self.strTime = self.hTime + ":" + self.mTime + ":" + self.sTime

    def refresh(self):
        # Carlos
        self.altP.set(randint(0, 100))
        self.d1.set(randint(0, 100))
        self.d2.set(randint(0, 100))
        self.tP.set(self.strTime)
        # self.master.after(1000, self.refresh)

    def table(self):
        nums = [i for i in range(51)]  # List comprehension to obtain list of numbers/ can be changed to desired number
        for i in nums:
            if i == 0:
                pass
            else:
                for hr, minute, sec in self.list:
                    # Inserts the number of data and current time to tree
                    self.tree.insert("", i, text=str(i), values=(hr + ":" + minute + ":" + sec))
                self.list = []  # Resets the time list
                self.real_time()
            self.master.after(1000, self.tree.update(), self.refresh())

    def handle_click(self, event):         # Function to prevent resize on the headings
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"


root = Draft1(tk.Tk())
root.real_time()
root.refresh()
root.table()
root.tree.bind('<Button-1>', root.handle_click)
tk.mainloop()
