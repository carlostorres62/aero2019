import tkinter as tk
from tkinter import ttk
import time
import datetime as dt
from serial import Serial

serial = Serial("/dev/cu.usbmodem144201", 9600)


class Draft1:
    def __init__(self, master):

        # Standard configuration

        self.master = master
        self.master.title("Aero Design")

        self.w, self.h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (self.w, self.h))
        self.master.resizable(False, False)

        self.scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(master, height=5, columns=5, yscrollcommand=self.scrollbar.set)
        self.start_time = time.time()

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(None, 15))  # Configures the size of the headings

        # Jorge
        # Configuration of the tree's appeareance
        self.height = 33  # Sets height size for tree
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
        self.altP, self.tP, self.cda_D, self.water_D, self.shelter_D, self.weight_D = tk.StringVar(), tk.StringVar(), \
                                                                                      tk.StringVar(), tk.StringVar(), \
                                                                                      tk.StringVar(), tk.StringVar()

        self.dataNum = tk.StringVar()

        self.data = ttk.Label(master, text="DATA:", font=("Helvetica", 60), style="R.TLabel")
        self.altitude = ttk.Label(master, text="Altitude:", font=("Helvetica", 60), style="B.TLabel")
        self.altitudeVar = ttk.Label(master, textvariable=self.altP, font=("Helvetica", 60))
        self.timeLabel = ttk.Label(master, text="Time:", font=("Helvetica", 60), style="B.TLabel")
        self.timeVar = ttk.Label(master, textvariable=self.tP, font=("Helvetica", 60))
        self.cdaDeploy = ttk.Label(master, text="CDA:", font=("Helvetica", 60), style="B.TLabel")
        self.cdaDeployVar = ttk.Label(master, textvariable=self.cda_D, font=("Helvetica", 60))
        self.waterDeploy = ttk.Label(master, text="Water:", font=("Helvetica", 60), style="B.TLabel")
        self.waterDeployVar = ttk.Label(master, textvariable=self.water_D, font=("Helvetica", 60))
        self.shelterDeploy = ttk.Label(master, text="Shelter:", font=("Helvetica", 60), style="B.TLabel")
        self.shelterDeployVar = ttk.Label(master, textvariable=self.shelter_D, font=("Helvetica", 60))

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
        self.cda_altitude = -1
        self.water_altitude = -1
        self.shelter_altitude = -1


        # Controls structure and localization of GUI
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

        # David
        # Configuration of scrollbar
        col_width = 100
        self.tree.column("#0", anchor=tk.CENTER, width=col_width - 50)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=col_width)

        self.scrollbar.config(command=self.tree.yview)

        self.tree.grid(row=0, column=0, sticky=tk.W)  # positions the scrollbar at the right (sticky = coordinates)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)

        self.ard_data()

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

    # Jorge
    def table(self):
        self.tree.bind('<Button-1>', self.handle_click)
        # Inserts the number of data and current time to tree
        self.tree.insert("", tk.END, text=self.dataNum.get(), values=(self.strTime, self.altP.get() + " ft",
                                                                   self.cda_D.get(),
                                                                   self.water_D.get(),
                                                                   self.shelter_D.get(),
                                                                   self.weight_D.get()))
        self.real_time()
        self.tree.update()

    # Function to receive data from Arduino and set variables
    def ard_data(self):
        while self.start == "On":
            while serial.inWaiting() == 0:
                print("Waiting")
                time.sleep(1)
                pass
            self.arduinoData = serial.readline()
            self.arduinoData = self.arduinoData.decode().rstrip()  # remove b' and /r/n'
            self.arduinoData = str(self.arduinoData)
            self.arduinoData = self.arduinoData.split(",")
            self.dataNum.set(self.arduinoData[0])
            self.altP.set(self.arduinoData[1])
            # print(self.arduinoData[2])
            # print(self.arduinoData[3])
            # print(self.arduinoData[4])
            if self.arduinoData[2] == str(0):
                # print("ard[2] == 0")
                self.cda_D.set(0)
            else:
                if self.cda_altitude == -1:
                    # print("ard[2] != 0")
                    self.cda_altitude = self.altP.get()
                    self.cda_D.set(self.cda_altitude)
                else:
                    pass
            if self.arduinoData[3] == str(0):
                self.water_D.set(0)
            else:
                if self.water_altitude == -1:
                    self.water_altitude = self.altP.get()
                    self.water_D.set(self.water_altitude)
                else:
                    pass

            if self.arduinoData[4] == str(0):
                self.shelter_D.set(0)
            else:
                if self.shelter_altitude == -1:
                    self.shelter_altitude = self.altP.get()
                    self.shelter_D.set(self.shelter_altitude)
                else:
                    pass
            self.weight_D.set(self.arduinoData[5])
            print(self.arduinoData)
            self.real_time()
            self.table()
            self.master.update()



    # Jorge
    def handle_click(self, event):  # Function to prevent resize on the headings
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"


root = Draft1(tk.Tk())
tk.mainloop()
