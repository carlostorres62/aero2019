import tkinter as tk
import datetime as dt
from tkinter import ttk
from tkinter import font
from serial import Serial
import time
import csv


class Flight2:
    def __init__(self, master):

        # Arduino configuration
        # "/dev/cu.usbserial-DN05KFL5"
        # "/dev/cu.usbmodem14201"
        # "COM6" or "COM10"
        self.port = "/dev/cu.usbserial-DN05KFL5"
        self.serial = Serial(self.port, 9600)

        # Standard configuration
        self.master = master
        self.master.title("Aero Design")
        self.master.state('zoomed')   # Sets the GUI to be full screen
        self.master.configure(background="Dim Grey")

        self.screenHeight = self.master.winfo_screenheight()  # Sets the height and width of the GUI to the
        self.screenWidth = self.master.winfo_screenwidth()    # height and width of corresponding computer screen

        self.master.call("tk", "scaling", 1)    # Scales the pixels so sizes do not vary on different computers

        self.style = ttk.Style()
        self.style.theme_use("classic")

        self.labelFont = font.Font(size=85)  # Sets font size, rules of the competition state that the font size
        self.labelFont2 = font.Font(size=40)  # of the display must be at least 0.5 inch in size.
        self.labelFont3 = font.Font(size=55)

        self.height = int((self.screenHeight / 20))  # Sets height size for the table
        col_width = int(self.screenWidth / 8)   # Sets width of columns for the table

        # Configures the style of the tree headings
        self.style.configure("Treeview.Heading", font=(None, 32))
        self.style.configure("Treeview", font=(None, 28), rowheight=40, fieldbackground="Dim Grey")

        # Configures the style of the tabs
        self.style.configure("TNotebook.Tab", font=("Helvetica", 20))
        self.style.configure("TNotebook", background="Dim Grey")

        # Configures the background and font colors
        self.style.configure("TLabel", background="Dim Grey")
        self.style.configure("B.TLabel", foreground="Blue")
        self.style.configure("R.TLabel", foreground="Red")
        self.style.configure("G.TLabel", foreground="Dark Green")
        self.style.configure("Y.TLabel", foreground="Gold")
        self.style.configure("W.TLabel", foreground="Black")
        self.style.configure("Vertical.TScrollbar", troughcolor="Dim Grey")

        # Allows the window to have two tabs
        self.notebook = ttk.Notebook(self.master, height=self.screenHeight, width=self.screenWidth)

        # Frames are used to create the tabs
        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)

        self.tab2.configure(bg="Dim Grey")

        # Adds and names the tabs
        self.notebook.add(self.tab1, text="Data")
        self.notebook.add(self.tab2, text="Table")

        # Frames within the tabs
        self.leftData = tk.Frame(self.tab1, height=self.screenHeight, width=self.screenWidth/2)
        self.rightData = tk.Frame(self.tab1, height=self.screenHeight, width=self.screenWidth/2)

        self.leftData.configure(bg="Dim Grey")
        self.rightData.configure(bg="Dim Grey")
        self.leftData.grid_propagate(False)
        self.rightData.grid_propagate(False)

        # Scrollbar and table initialization
        self.scrollbar = ttk.Scrollbar(self.tab2, orient=tk.VERTICAL, style="Vertical.TScrollbar")
        self.tree = ttk.Treeview(self.tab2, yscrollcommand=self.scrollbar.set)

        # Jorge
        # Configuration of the tree's appeareance
        self.tree["height"] = self.height
        self.tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven")
        self.tree.heading("#0", text="Data", anchor=tk.CENTER)
        self.tree.heading("one", text="Time", anchor=tk.CENTER)
        self.tree.heading("two", text="Altitude", anchor=tk.CENTER)
        self.tree.heading("three", text="Water", anchor=tk.CENTER)
        self.tree.heading("four", text="Habitat", anchor=tk.CENTER)
        self.tree.heading("five", text="CDA 1", anchor=tk.CENTER)
        self.tree.heading("six", text="CDA 2", anchor=tk.CENTER)
        self.tree.heading("seven", text="CDA 3", anchor=tk.CENTER)

        # Carlos
        self.dataNum = 0
        self.altP, self.tP, self.tP2, self.tP3 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.cda_D1, self.cda_D2, self.cda_D3 = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.water_D, self.shelter_D = tk.StringVar(), tk.StringVar()
        self.gate, self.close = tk.StringVar(), tk.StringVar()

        # Configuration of Data appearance with all previously created components
        self.timeLabel = ttk.Label(self.leftData, text="Time:", font=self.labelFont, style="G.TLabel", anchor=tk.CENTER)
        self.timeVar = ttk.Label(self.leftData, textvariable=self.tP, font=self.labelFont, style="W.TLabel")

        self.cdaDeploy1 = ttk.Label(self.leftData, text="CDA 1:", font=self.labelFont, style="B.TLabel")
        self.cdaDeployVar1 = ttk.Label(self.leftData, textvariable=self.cda_D1, font=self.labelFont, style="W.TLabel")
        self.timeLabelC1 = ttk.Label(self.leftData, text="Deploy Time:", font=self.labelFont2, style="R.TLabel",
                                     anchor=tk.E)
        self.timeVarC1 = ttk.Label(self.leftData, textvariable=self.tP3, font=self.labelFont2, style="Y.TLabel")

        self.cdaDeploy2 = ttk.Label(self.leftData, text="CDA 2:", font=self.labelFont, style="B.TLabel")
        self.cdaDeployVar2 = ttk.Label(self.leftData, textvariable=self.cda_D2, font=self.labelFont, style="W.TLabel")
        self.timeLabelC2 = ttk.Label(self.leftData, text="Deploy Time:", font=self.labelFont2, style="R.TLabel",
                                     anchor=tk.E)
        self.timeVarC2 = ttk.Label(self.leftData, textvariable=self.tP3, font=self.labelFont2, style="Y.TLabel")

        self.cdaDeploy3 = ttk.Label(self.leftData, text="CDA 3:", font=self.labelFont, style="B.TLabel")
        self.cdaDeployVar3 = ttk.Label(self.leftData, textvariable=self.cda_D3, font=self.labelFont, style="W.TLabel")
        self.timeLabelC3 = ttk.Label(self.leftData, text="Deploy Time:", font=self.labelFont2, style="R.TLabel",
                                     anchor=tk.E)
        self.timeVarC3 = ttk.Label(self.leftData, textvariable=self.tP3, font=self.labelFont2, style="Y.TLabel")

        self.altitude = ttk.Label(self.rightData, text="Altitude:", font=self.labelFont, style="G.TLabel")
        self.altitudeVar = ttk.Label(self.rightData, textvariable=self.altP, font=self.labelFont, style="W.TLabel")

        self.waterDeploy = ttk.Label(self.rightData, text="Water:", font=self.labelFont, style="B.TLabel", anchor=tk.E)
        self.waterDeployVar = ttk.Label(self.rightData, textvariable=self.water_D, font=self.labelFont,
                                        style="W.TLabel")
        self.timeLabelW = ttk.Label(self.rightData, text="Deploy Time:", font=self.labelFont2, style="R.TLabel",
                                    anchor=tk.E)
        self.timeVarW = ttk.Label(self.rightData, textvariable=self.tP2, font=self.labelFont2, style="Y.TLabel")

        self.shelterDeploy = ttk.Label(self.rightData, text="Habitat:", font=self.labelFont, style="B.TLabel",
                                       anchor=tk.E)
        self.shelterDeployVar = ttk.Label(self.rightData, textvariable=self.shelter_D, font=self.labelFont,
                                          style="W.TLabel")
        self.timeLabelS = ttk.Label(self.rightData, text="Deploy Time:", font=self.labelFont2, style="R.TLabel",
                                    anchor=tk.E)
        self.timeVarS = ttk.Label(self.rightData, textvariable=self.tP2, font=self.labelFont2, style="Y.TLabel")

        self.gateVar = ttk.Label(self.rightData, textvariable=self.gate, font=self.labelFont3, style="Y.TLabel")
        self.closeVar = ttk.Label(self.rightData, textvariable=self.close, font=self.labelFont3, style="Y.TLabel")

        # Arduino variables
        self.arduinoData = ""

        # Time variables
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.hTime = str(self.hour)
        self.mTime = str(self.minute)
        self.sTime = str(self.second)
        self.strTime = ""
        self.strTime2 = ""

        # Variable to store backup csv array
        self.csv_data = []

        # Function to display tabs
        self.notebook.pack()

        # Process to arrange sizing for rows and columns
        col_count, row_count = self.master.grid_size()
        for col in range(col_count):
            self.master.grid_columnconfigure(col, minsize=5)
        for row in range(row_count):
            self.master.grid_rowconfigure(row, minsize=5)

        # All grids necessary for GUI display
        # sticky is use to fix coordinates to desired location
        self.leftData.grid(row=0, column=0)
        self.rightData.grid(row=0, column=1)

        self.timeLabel.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.timeVar.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.altitude.grid(row=0, column=2, sticky=tk.E)
        self.altitudeVar.grid(row=0, column=3, sticky=tk.E)

        self.cdaDeploy1.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.cdaDeployVar1.grid(row=1, column=1, sticky=tk.W+tk.E)
        self.timeLabelC1.grid(row=2, column=0, sticky=tk.W+tk.E)
        self.timeVarC1.grid(row=2, column=1, sticky=tk.W+tk.E)

        self.cdaDeploy2.grid(row=3, column=0, sticky=tk.W+tk.E)
        self.cdaDeployVar2.grid(row=3, column=1, sticky=tk.W+tk.E)
        self.timeLabelC2.grid(row=4, column=0, sticky=tk.W+tk.E)
        self.timeVarC2.grid(row=4, column=1, sticky=tk.W+tk.E)

        self.cdaDeploy3.grid(row=5, column=0, sticky=tk.W+tk.E)
        self.cdaDeployVar3.grid(row=5, column=1, sticky=tk.W+tk.E)
        self.timeLabelC3.grid(row=6, column=0, sticky=tk.W+tk.E)
        self.timeVarC3.grid(row=6, column=1, sticky=tk.W+tk.E)

        self.waterDeploy.grid(row=1, column=2, sticky=tk.W+tk.E)
        self.waterDeployVar.grid(row=1, column=3, sticky=tk.W+tk.E)
        self.timeLabelW.grid(row=2, column=2, sticky=tk.W+tk.E)
        self.timeVarW.grid(row=2, column=3, sticky=tk.W+tk.E)

        self.shelterDeploy.grid(row=3, column=2, sticky=tk.W+tk.E)
        self.shelterDeployVar.grid(row=3, column=3, sticky=tk.W+tk.E)
        self.timeLabelS.grid(row=4, column=2, sticky=tk.W+tk.E)
        self.timeVarS.grid(row=4, column=3, sticky=tk.W+tk.E)

        self.gateVar.grid(row=5, column=2, sticky=tk.E)
        self.closeVar.grid(row=5, column=3, sticky=tk.W)

        # David
        # Configuration of scrollbar
        self.tree.column("#0", anchor=tk.CENTER, width=col_width - 25)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=col_width)

        self.scrollbar.config(command=self.tree.yview)

        self.tree.pack(side=tk.LEFT)
        self.scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        # positions the scrollbar at the right (sticky = coordinates)

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
        self.strTime2 = "  " + self.hTime + ":" + self.mTime + ":" + self.second  # for the position of smaller times
        self.tP.set(self.strTime)
        if self.arduinoData[1] == "0":
            self.tP2.set(self.strTime2)
        else:
            self.gate.set("Gate ")
            self.close.set("Closed")
        if self.arduinoData[2] == "0":
            self.tP3.set(self.strTime2)

    # Jorge
    def table(self):
        # Call of handle_click function when left click is pressed
        self.tree.bind('<Button-1>', self.handle_click)
        # Inserts the number of data and current time to tree with StringVar variables previously initialized
        self.tree.insert("", tk.END, text=self.dataNum, values=(self.strTime, self.altP.get(), self.water_D.get(),
                                                                self.shelter_D.get(), self.cda_D1.get(),
                                                                self.cda_D2.get(), self.cda_D3.get()))
        self.real_time()
        self.tree.update()

    # Function to receive data from Arduino and set variables
    def ard_data(self):
        # Connects to port where antenna is currently connected
        # self.serial = Serial("dev/cu.usbserial-DN05KFL5", 9600)
        """ While loop is used to iterate infinitely to keep receiving data from arduino.
        Try is used to WAIT until signal from arduino is received. If no signal is received the if condition is met. 
        If the 'message' varible is 0, then it breaks out of the loop and the function is called again
        in the 'after' function that is outside of the while loop
        When a signal is received the 'message' variable changes from 0 to 1 and the else condition is met.
        """
        while True:
            try:
                message = self.serial.inWaiting()
            except:
                self.master.after(100, self.ard_data)

            if message == 0:
                print("Waiting")
                time.sleep(1)
                break
            else:
                self.arduinoData = self.serial.readline() # Function that reads data sent from arduino
                self.arduinoData = self.arduinoData.decode().rstrip()  # remove b' and /r/n'
                self.arduinoData = str(self.arduinoData) # Converts the data from arduino to string
                self.arduinoData = self.arduinoData.split(",")
                # Set the value to the variables that will be displayed on the GUI with the data from arduino
                self.dataNum += 1
                self.altP.set(self.arduinoData[0])
                self.water_D.set(self.arduinoData[1])
                self.shelter_D.set(self.arduinoData[1])
                self.cda_D1.set(self.arduinoData[2])
                self.cda_D2.set(self.arduinoData[2])
                self.cda_D3.set(self.arduinoData[2])

                print(self.arduinoData)
                self.real_time()
                self.table()

                self.csv_data = [self.dataNum, self.arduinoData[0], self.arduinoData[1], self.arduinoData[2]]
                with open('backup.csv', 'a', newline="") as csvFile:
                    writer = csv.writer(csvFile)  # Creates csv file
                    writer.writerow(self.csv_data)
                csvFile.close()

        self.master.after(100, self.ard_data)

        # Jorge
    def handle_click(self, event):  # Function to prevent resize on the headings
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"


root = Flight2(tk.Tk())
# root.master.after(1000, root.ard_data)
root.ard_data()
root.master.mainloop()
