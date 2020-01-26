import tkinter as tk
from tkinter import ttk
import time
import datetime as dt
from serial import Serial


class Flight1:
    def __init__(self, master):

        self.serial = ""
        self.wait = 0

        self.master = master
        self.master.title("Aero Design")

        self.w, self.h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (self.w, self.h))
        self.master.resizable(False, False)

        self.y_scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(master, height=5, columns=5, yscrollcommand=self.y_scrollbar.set)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(None, 15))  # Configures the size of the headings

        self.height = 33  # Sets height size for tree
        self.tree["height"] = self.height
        self.tree["columns"] = ("one", "two", "three", "four", "five", "six")
        self.tree.heading("#0", text="Data", anchor=tk.CENTER)
        self.tree.heading("one", text="Time", anchor=tk.CENTER)
        self.tree.heading("two", text="Altitude", anchor=tk.CENTER)
        self.tree.heading("three", text="Water", anchor=tk.CENTER)
        self.tree.heading("four", text="Shelter", anchor=tk.CENTER)
        self.tree.heading("five", text="CDA 1", anchor=tk.CENTER)
        self.tree.heading("six", text="CDA 2", anchor=tk.CENTER)

        self.dataNum, self.altP, self.tP = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.cda_D1, self.cda_D2, self.cda_D3 = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.water_D, self.shelter_D = tk.StringVar(), tk.StringVar()

        self.data = ttk.Label(master, text="DATA:", font=("Helvetica", 60), style="R.TLabel")
        self.altitude = ttk.Label(master, text="Altitude:", font=("Helvetica", 60), style="B.TLabel")
        self.altitudeVar = ttk.Label(master, textvariable=self.altP, font=("Helvetica", 60))
        self.timeLabel = ttk.Label(master, text="Time:", font=("Helvetica", 60), style="B.TLabel")
        self.timeVar = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 60))
        self.cdaDeploy = ttk.Label(master, text="CDA1:", font=("Helvetica", 60), style="B.TLabel")
        self.cdaDeployVar = ttk.Label(master, textvariable=self.cda_D1, font=("Helvetica", 60))
        self.cda2Deploy = ttk.Label(master, text="CDA2:", font=("Helvetica", 60), style="B.TLabel")
        self.cda2DeployVar = ttk.Label(master, textvariable=self.cda_D2, font=("Helvetica", 60))
        self.cda3Deploy = ttk.Label(master, text="CDA:", font=("Helvetica", 60), style="B.TLabel")
        self.cda3DeployVar = ttk.Label(master, textvariable=self.cda_D3, font=("Helvetica", 60))
        self.waterDeploy = ttk.Label(master, text="Water:", font=("Helvetica", 60), style="B.TLabel")
        self.waterDeployVar = ttk.Label(master, textvariable=self.water_D, font=("Helvetica", 60))
        self.shelterDeploy = ttk.Label(master, text="Shelter:", font=("Helvetica", 60), style="B.TLabel")
        self.shelterDeployVar = ttk.Label(master, textvariable=self.shelter_D, font=("Helvetica", 60))

        self.style.configure("B.TLabel", foreground="Blue")
        self.style.configure("R.TLabel", foreground="Red")

        self.arduinoData = ""
        self.cda_altitude = -1
        self.cda2_altitude = -1
        self.water_altitude = -1
        self.shelter_altitude = -1

        self.hour = 0
        self.minute = 0
        self.second = 0
        self.hTime = str(self.hour)
        self.mTime = str(self.minute)
        self.sTime = str(self.second)
        self.strTime = ""

        self.data.place(relx=0.55, rely=0.05)
        self.altitude.place(relx=0.55, rely=1 / 6)
        self.altitudeVar.place(relx=0.8, rely=1 / 6)
        self.timeLabel.place(relx=0.55, rely=2 / 6)
        self.timeVar.place(relx=0.75, rely=2 / 6)
        self.cdaDeploy.place(relx=0.55, rely=3 / 6)
        self.cdaDeployVar.place(relx=0.8, rely=3 / 6)
        self.waterDeploy.place(relx=0.55, rely=4 / 6)
        self.waterDeployVar.place(relx=0.8, rely=4 / 6)
        self.shelterDeploy.place(relx=0.55, rely=5 / 6)
        self.shelterDeployVar.place(relx=0.8, rely=5 / 6)

        col_width = 100
        self.tree.column("#0", anchor=tk.CENTER, width=col_width - 50)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=col_width)

        self.y_scrollbar.config(command=self.tree.yview)

        self.tree.grid(row=0, column=0, sticky=tk.W)  # positions the scrollbar at the right (sticky = coordinates)
        self.y_scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)
        print("init")


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
            self.second = "0" + str(self.second)  # If second is 5 it would show "05"
        else:
            self.second = str(self.second)

        self.strTime = self.hTime + ":" + self.mTime + ":" + self.second
        self.tP.set(self.strTime)
        print("time")

    def table(self):
        self.tree.bind('<Button-1>', self.handle_click)
        # Inserts the number of data and current time to tree
        self.tree.insert("", tk.END, text=self.dataNum.get(), values=(self.strTime, self.altP.get() + " ft",
                                                                      self.water_D.get(), self.shelter_D.get(),
                                                                      self.cda_D1.get(), self.cda_D2.get(),
                                                                      self.cda_D3.get()))
        self.real_time()
        self.tree.update()
        print("table")

    def ard_data(self):

        self.serial = Serial("COM6", 9600)
       # self.wait = self.serial.write(1)

        while True:
            if self.serial.inWaiting() == 0:
                print("Waiting")
                time.sleep(1)
                pass

            self.arduinoData = self.serial.readline()
            self.arduinoData = self.arduinoData.decode().rstrip()  # remove b' and /r/n'
            self.arduinoData = str(self.arduinoData)
            self.arduinoData = self.arduinoData.split(",")
            #self.dataNum.set(self.arduinoData[0])
            self.altP.set(self.arduinoData[0])
            self.water_D.set(self.arduinoData[1])
            self.shelter_D.set(self.arduinoData[2])
            #self.cda_D1.set(self.arduinoData[4])
            #self.cda_D2.set(self.arduinoData[5])

            print(self.arduinoData)
            self.real_time()
            self.table()

            print("ard data")

    def handle_click(self, event):
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"
        print("handle")


root = Flight1(tk.Tk())
print("before try")


def refresh():

    try:
        root.ard_data()
        print("in try")
    except:
        print("Disconnected")
        tk.mainloop()


root.master.after(1000, refresh)
tk.mainloop()
