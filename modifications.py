import tkinter as tk
from tkinter import ttk
import datetime as dt
from random import *
# from serial import Serial


class Draft1:
    def __init__(self, master):

        # Standard configuration
        self.master = master
        self.master.title("Aero Design")

        # width and height of the respective computer
        self.w, self.h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (self.w, self.h))
        # self.master.resizable(False, False)
        self.master.configure(background="Dim Grey")

        self.style = ttk.Style()
        self.style.theme_use("classic")

        self.style.configure("Treeview.Heading", font=(None, 15))  # Configures the style of the headings
        self.style.configure("Treeview", background="Dim Grey", fieldbackground="Dim Grey", foreground="Black")

        self.style.configure("B.TLabel", foreground="Blue", background="Dim Grey", bordercolor="Black")
        self.style.configure("R.TLabel", foreground="Red", background="Dim Grey")
        self.style.configure("G.TLabel", foreground="Dark Green", background="Dim Grey")
        self.style.configure("Y.TLabel", foreground="Gold", background="Dim Grey")
        self.style.configure("W.TLabel", foreground="Black",  background="Dim Grey")
        self.style.configure("Vertical.TScrollbar", troughcolor="Dim Grey")

        # Scrollbar and table initialization
        self.scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, style="Vertical.TScrollbar")
        self.tree = ttk.Treeview(master, height=5, columns=5, yscrollcommand=self.scrollbar.set)

        # Jorge
        # Configuration of the tree's appeareance
        self.height = 30  # Sets height size for tree
        self.tree["height"] = self.height
        self.tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven")
        self.tree.heading("#0", text="Data", anchor=tk.CENTER)
        self.tree.heading("one", text="Time", anchor=tk.CENTER)
        self.tree.heading("two", text="Altitude", anchor=tk.CENTER)
        self.tree.heading("three", text="Water", anchor=tk.CENTER)
        self.tree.heading("four", text="Shelter", anchor=tk.CENTER)
        self.tree.heading("five", text="CDA 1", anchor=tk.CENTER)
        self.tree.heading("six", text="CDA 2", anchor=tk.CENTER)
        self.tree.heading("seven", text="CDA 3", anchor=tk.CENTER)

        # Carlos
        # Configuration of the GUI's appearance
        self.dataNum, self.altP, self.tP = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.cda_D1, self.cda_D2, self.cda_D3 = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.water_D, self.shelter_D = tk.StringVar(), tk.StringVar()

        self.timeLabel = ttk.Label(master, text="Time:", font=("Helvetica", 90), style="G.TLabel")
        self.timeVar = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 90), style="W.TLabel")
        self.altitude = ttk.Label(master, text="Altitude:", font=("Helvetica", 90), style="G.TLabel")
        self.altitudeVar = ttk.Label(master, textvariable=self.altP, font=("Helvetica", 90), style="W.TLabel")

        self.waterDeploy = ttk.Label(master, text="Water:", font=("Helvetica", 90), style="B.TLabel")
        self.waterDeployVar = ttk.Label(master, textvariable=self.water_D, font=("Helvetica", 90), style="W.TLabel")
        self.timeLabelW = ttk.Label(master, text="Deploy Time:", font=("Helvetica", 50), style="R.TLabel")
        self.timeVarW = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 50), style="Y.TLabel")

        self.shelterDeploy = ttk.Label(master, text="Shelter:", font=("Helvetica", 90), style="B.TLabel")
        self.shelterDeployVar = ttk.Label(master, textvariable=self.shelter_D, font=("Helvetica", 90), style="W.TLabel")
        self.timeLabelS = ttk.Label(master, text="- Deploy Time:", font=("Helvetica", 50), style="R.TLabel")
        self.timeVarS = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 50), style="Y.TLabel")
        
        self.cdaDeploy1 = ttk.Label(master, text="CDA 1:", font=("Helvetica", 90), style="B.TLabel")
        self.cdaDeployVar1 = ttk.Label(master, textvariable=self.cda_D1, font=("Helvetica", 90), style="W.TLabel")
        self.timeLabelC1 = ttk.Label(master, text="Deploy Time:", font=("Helvetica", 50), style="R.TLabel")
        self.timeVarC1 = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 50), style="Y.TLabel")
        
        self.cdaDeploy2 = ttk.Label(master, text="CDA 2:", font=("Helvetica", 90), style="B.TLabel")
        self.cdaDeployVar2 = ttk.Label(master, textvariable=self.cda_D2, font=("Helvetica", 90), style="W.TLabel")
        self.timeLabelC2 = ttk.Label(master, text="Deploy Time:", font=("Helvetica", 50), style="R.TLabel")
        self.timeVarC2 = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 50), style="Y.TLabel")
        
        self.cdaDeploy3 = ttk.Label(master, text="CDA 3:", font=("Helvetica", 90), style="B.TLabel")
        self.cdaDeployVar3 = ttk.Label(master, textvariable=self.cda_D3, font=("Helvetica", 90), style="W.TLabel")
        self.timeLabelC3 = ttk.Label(master, text="Deploy Time:", font=("Helvetica", 50), style="R.TLabel")
        self.timeVarC3 = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 50), style="Y.TLabel")

        # Arduino variables
        self.arduinoData = ""
        self.cda_altitude = -1
        self.cda2_altitude = -1
        self.water_altitude = -1
        self.shelter_altitude = -1

        # Time variables
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.hTime = str(self.hour)
        self.mTime = str(self.minute)
        self.sTime = str(self.second)
        self.strTime = ""

        # Sets the position of labels in GUI
        self.timeLabel.place(relx=0.05, rely=0.75)
        self.timeVar.place(relx=0.225, rely=0.75)
        self.altitude.place(relx=0.05, rely=0.86)
        self.altitudeVar.place(relx=0.295, rely=0.86)

        self.waterDeploy.place(relx=0.55, rely=0.01)
        self.waterDeployVar.place(relx=0.775, rely=0.01)
        self.timeLabelW.place(relx=0.575, rely=0.12)
        self.timeVarW.place(relx=0.79, rely=0.12)

        self.shelterDeploy.place(relx=0.55, rely=0.21)
        self.shelterDeployVar.place(relx=0.775, rely=0.21)
        self.timeLabelS.place(relx=0.565, rely=0.32)
        self.timeVarS.place(relx=0.8, rely=0.32)

        self.cdaDeploy1.place(relx=0.55, rely=0.41)
        self.cdaDeployVar1.place(relx=0.775, rely=0.41)
        self.timeLabelC1.place(relx=0.55, rely=0.52)
        self.timeVarC1.place(relx=0.775, rely=0.52)

        self.cdaDeploy2.place(relx=0.55, rely=0.61)
        self.cdaDeployVar2.place(relx=0.775, rely=0.61)
        self.timeLabelC2.place(relx=0.55, rely=0.72)
        self.timeVarC2.place(relx=0.775, rely=0.72)

        self.cdaDeploy3.place(relx=0.55, rely=0.81)
        self.cdaDeployVar3.place(relx=0.775, rely=0.81)
        self.timeLabelC3.place(relx=0.55, rely=0.92)
        self.timeVarC3.place(relx=0.775, rely=0.92)

        # David
        # Configuration of scrollbar
        col_width = 100
        self.tree.column("#0", anchor=tk.CENTER, width=col_width - 50)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=col_width)

        self.scrollbar.config(command=self.tree.yview)

        self.tree.grid(row=0, column=0, sticky=tk.W)  # positions the scrollbar at the right (sticky = coordinates)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)

        # runs the arduino function
        # self.ard_data()

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
        self.tP.set(self.strTime)

    def refresh(self):
        # Carlos
        self.dataNum.set(randint(0, 100))
        self.altP.set(randint(10000, 20000))
        self.water_D.set(randint(10000, 20000))
        self.shelter_D.set(randint(10000, 20000))
        self.cda_D1.set(randint(10000, 20000))
        self.cda_D2.set(randint(10000, 20000))
        self.cda_D3.set(randint(10000, 20000))
        self.tP.set(self.strTime)
        # self.master.after(1000, self.refresh)

    # Jorge
    def table(self):
        self.tree.bind('<Button-1>', self.handle_click)
        self.real_time()
        self.refresh()
        # Inserts the number of data and current time to tree
        self.tree.insert("", tk.END, text=self.dataNum.get(), values=(self.strTime, self.altP.get(),
                                                                      self.water_D.get(), self.shelter_D.get(),
                                                                      self.cda_D1.get(), self.cda_D2.get(),
                                                                      self.cda_D3.get()))
        self.master.after(1000, self.table)

    # Function to receive data from Arduino and set variables
    # def ardData(self):
    #     while self.start == "On":
    #         while self.serialData.inWaiting() == 0:
    #             pass
    #         self.arduinoData = Serial.readline()
    #         self.dataArray = self.arduinoData.split()
    #         self.altP.set(float(self.dataArray[0]))
    #         self.cda_D.set(float(self.dataArray[1]))
    #         self.water_D.set(float(self.dataArray[2]))
    #         self.shelter_D.set(float(self.dataArray[3]))

    # Jorge
    def handle_click(self, event):  # Function to prevent resize on the headings
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"


root = Draft1(tk.Tk())
root.table()
tk.mainloop()
