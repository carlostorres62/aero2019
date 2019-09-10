import tkinter as tk
from tkinter import ttk
import time
import datetime as dt
from random import *

master = tk.Tk()
master.title("Aero Design")
master.geometry("1000x425+50+50")
master.resizable(0, 0)


scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL)
tree = ttk.Treeview(master, height=5, columns=5, yscrollcommand=scrollbar.set)

style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 15))   # Configures the size of the headings

height = 20         # Sets height size for tree
tree["height"] = height
tree["columns"] = ("one", "two", "three", "four", "five", "six")
tree.heading("#0", text="Data", anchor=tk.CENTER)
tree.heading("one", text="Time", anchor=tk.CENTER)
tree.heading("two", text="Altitude", anchor=tk.CENTER)
tree.heading("three", text="CDA", anchor=tk.CENTER)
tree.heading("four", text="Water", anchor=tk.CENTER)
tree.heading("five", text="Shelter", anchor=tk.CENTER)
tree.heading("six", text="Weight", anchor=tk.CENTER)

altP, tP, d1, d2 = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()

data = ttk.Label(master, text="DATA:", font=("Helvetica", 25), style="R.TLabel")
altitude = ttk.Label(master, text="Altitude:", font=("Helvetica", 20), style="B.TLabel")
altitudeVar = ttk.Label(master, textvariable=altP, font=("Helvetica", 20))
timeLabel = ttk.Label(master, text="Time:", font=("Helvetica", 20), style="B.TLabel")
timeVar = ttk.Label(master, textvariable=tP, font=("Helvetica", 20))
deploy1 = ttk.Label(master, text="Deploy 1: ", font=("Helvetica", 20), style="B.TLabel")
deploy1Var = ttk.Label(master, textvariable=d1, font=("Helvetica", 20))
deploy2 = ttk.Label(master, text="Deploy 2:", font=("Helvetica", 20), style="B.TLabel")
deploy2Var = ttk.Label(master, textvariable=d2, font=("Helvetica", 20))

style.configure("B.TLabel", foreground="Blue")
style.configure("R.TLabel", foreground="Red")

data.place(relx=3 / 4, rely=0.05)
altitude.place(relx=3 / 4, rely=1 / 5)
altitudeVar.place(relx=0.9, rely=1 / 5)
timeLabel.place(relx=3 / 4, rely=2 / 5)
timeVar.place(relx=0.9, rely=2 / 5)
deploy1.place(relx=3 / 4, rely=3 / 5)
deploy1Var.place(relx=0.9, rely=3 / 5)
deploy2.place(relx=3 / 4, rely=4 / 5)
deploy2Var.place(relx=0.9, rely=4 / 5)

# David
col_width = 100
tree.column("#0", anchor=tk.CENTER, width=col_width-50)
for col in tree["columns"]:
    tree.column(col, anchor=tk.CENTER, width=col_width)

scrollbar.config(command=tree.yview)

tree.grid(row=0, column=0, sticky=tk.W)
scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)  # positions the scrollbar at the right (sticky = coordinates)

nums = [i for i in range(51)]     # List comprehension to obtain list of numbers/ can be changed to desired number
tList = []      # Empty List created to store the actual time


def update():
    altP.set(randint(0, 100))
    tP.set(0)
    d1.set(randint(0, 100))
    d2.set(randint(0, 100))
    master.after(1000, update)


update()

for i in nums:
    if i == 0:
        pass
    else:
        hour = dt.datetime.now().hour    # Obtains the current hour
        minute = dt.datetime.now().minute   # Obtains the current minute
        second = dt.datetime.now().second   # Obtains the current second
        hTime = str(hour)
        if minute < 10:
            mTime = "0" + str(minute)    # Concatenate a 0 in front of number in case it is a single digit number
        else:
            mTime = str(minute)
        if second < 10:
            sTime = "0" + str(second)   # If second is 5 it would show "05"
        else:
            sTime = str(second)
        tList = [(hTime, mTime, sTime)]  # Stores the actual time in time list
        for hr, min, sec in tList:
            # Inserts the number of data and current time to tree
            tree.insert("", i, text=str(i), values=(hr + ":" + min + ":" + sec))
        tList = []  # Resets the time list
        tree.update()    # Updates the tree every time it loops


    def handle_click(event):         # Function to prevent resize on the headings
        if tree.identify_region(event.x, event.y) == "separator":
            return "break"
    tree.bind('<Button-1>', handle_click)

    # time.sleep(1)


master.mainloop()
