import tkinter as tk
from tkinter import ttk
import time
import datetime as dt
from random import *
from serial import Serial


class Draft1:
    def __init__(self, master):

        # Standard configuration
        self.master = master
        self.master.title("Aero Design")
        self.master.geometry("1000x425+125+50")
        self.master.resizable(False, False)

        self.scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(master, height=5, columns=5, yscrollcommand=self.scrollbar.set)
        self.start_time = time.time()

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(None, 15))  # Configures the size of the headings

        # Jorge
        # Configuration of the tree's appeareance
        self.height = 20  # Sets height size for tree
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
        # Configuration of the GUI's appearence
        self.altP, self.tP, self.cda_D, self.water_D, self.shelter_D, self.weight_D = tk.IntVar(), tk.StringVar(), tk.StringVar(), \
                                                                                      tk.StringVar(), tk.StringVar(), tk.IntVar()

        self.data = ttk.Label(master, text="DATA:", font=("Helvetica", 25), style="R.TLabel")
        self.altitude = ttk.Label(master, text="Altitude:", font=("Helvetica", 20), style="B.TLabel")
        self.altitudeVar = ttk.Label(master, textvariable=self.altP, font=("Helvetica", 20))
        self.timeLabel = ttk.Label(master, text="Time:", font=("Helvetica", 20), style="B.TLabel")
        self.timeVar = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 20))
        self.cdaDeploy = ttk.Label(master, text="CDA:", font=("Helvetica", 20), style="B.TLabel")
        self.cdaDeployVar = ttk.Label(master, textvariable=self.cda_D, font=("Helvetica", 20))
        self.waterDeploy = ttk.Label(master, text="Water:", font=("Helvetica", 20), style="B.TLabel")
        self.waterDeployVar = ttk.Label(master, textvariable=self.water_D, font=("Helvetica", 20))
        self.shelterDeploy = ttk.Label(master, text="Shelter:", font=("Helvetica", 20), style="B.TLabel")
        self.shelterDeployVar = ttk.Label(master, textvariable=self.shelter_D, font=("Helvetica", 20))

        self.style.configure("B.TLabel", foreground="Blue")
        self.style.configure("R.TLabel", foreground="Red")

        # Variables needed for program functionality
        self.start = "On"
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.hTime = str(self.hour)
        self.mTime = str(self.minute)
        self.sTime = str(self.second)
        self.strTime = ""
        self.arduinoData = ""
        self.dataArray = []
        # Comment when Arduino is not connected, "COM" changes depending on computer port
        # self.serialData = Serial("COM4", 9600)

        # Controls structure and localization of GUI
        self.data.place(relx=3 / 4, rely=0.05)
        self.altitude.place(relx=3 / 4, rely=1 / 6)
        self.altitudeVar.place(relx=0.9, rely=1 / 6)
        self.timeLabel.place(relx=3 / 4, rely=2 / 6)
        self.timeVar.place(relx=0.85, rely=2 / 6)
        self.cdaDeploy.place(relx=3 / 4, rely=3 / 6)
        self.cdaDeployVar.place(relx=0.9, rely=3 / 6)
        self.waterDeploy.place(relx=3 / 4, rely=4 / 6)
        self.waterDeployVar.place(relx=0.9, rely=4 / 6)
        self.shelterDeploy.place(relx=3 / 4, rely=5 / 6)
        self.shelterDeployVar.place(relx=0.9, rely=5 / 6)

        # David
        # Configuration of scrollbar
        col_width = 100
        self.tree.column("#0", anchor=tk.CENTER, width=col_width - 50)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=col_width)

        self.scrollbar.config(command=self.tree.yview)

        self.tree.grid(row=0, column=0, sticky=tk.W)  # positions the scrollbar at the right (sticky = coordinates)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)

    def real_time(self):
        # Jorge
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
            self.second = "0" + str(self.second)  # If second is 5 it would show "05"
        else:
            self.second = str(self.second)
        self.strTime = self.hTime + ":" + self.mTime + ":" + self.second

    def refresh(self):
        # Carlos
        self.altP.set(randint(0, 100))
        self.cda_D.set(0)
        self.water_D.set(0)
        self.shelter_D.set(0)
        self.weight_D.set(randint(0, 100))
        self.tP.set(self.strTime)
        # self.master.after(1000, self.refresh)

    # Jorge
    def table(self):
        nums = [i for i in range(51)]  # List comprehension to obtain list of numbers/ can be changed to desired number
        if self.cda_D == 1:
            cda = True
        else:
            cda = False
        if self.water_D == 1:
            water = True
        else:
            water = False
        if self.shelter_D == 1:
            shelter = True
        else:
            shelter = False
        for i in nums:
            if i == 0:
                pass
            else:
                # Inserts the number of data and current time to tree

                self.real_time()
                self.tree.insert("", tk.END, text=str(i), values=(self.strTime, str(self.altP.get()),
                                                                  cda, water, shelter, str(self.weight_D.get())))
                self.master.after(1000, self.refresh(), self.tree.update())  # 937
                # time.sleep(1)

    # Function to receive data from Arduino and set variables
    def ardData(self):
        while self.start == "On":
            while self.serialData.inWaiting() == 0:
                pass
            self.arduinoData = Serial.readline()
            self.dataArray = self.arduinoData.split()
            self.altP.set(float(self.dataArray[0]))
            self.cda_D.set(float(self.dataArray[1]))
            self.water_D.set(float(self.dataArray[2]))
            self.shelter_D.set(float(self.dataArray[3]))

    # Jorge
    def handle_click(self, event):  # Function to prevent resize on the headings
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"


root = Draft1(tk.Tk())
root.refresh()
root.table()
# root.ardData()
root.tree.bind('<Button-1>', root.handle_click)
tk.mainloop()
