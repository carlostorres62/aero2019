import tkinter as tk
import datetime as dt
from random import randint
from tkinter import ttk
from tkinter import font


class Draft1:
    def __init__(self, master):

        # Standard configuration
        self.master = master
        self.master.title("Aero Design")
        self.master.state('zoomed')
        self.master.configure(background="Dim Grey")

        self.screenHeight = self.master.winfo_screenheight()
        self.screenWidth = self.master.winfo_screenwidth()

        self.master.call("tk", "scaling", 1)

        self.style = ttk.Style()
        self.style.theme_use("classic")

        self.labelFont = font.Font(size=85)
        self.labelFont2 = font.Font(size=40)

        self.height = int((self.screenHeight / 20))  # Sets height size for tree
        col_width = int(self.screenWidth / 8)

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

        self.notebook = ttk.Notebook(self.master, height=self.screenHeight, width=self.screenWidth)

        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)

        self.tab2.configure(bg="Dim Grey")

        self.notebook.add(self.tab1, text="Data")
        self.notebook.add(self.tab2, text="Table")

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
        # Configuration of Data appearance
        self.dataNum, self.altP, self.tP, self.tP2 = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.cda_D1, self.cda_D2, self.cda_D3 = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.water_D, self.shelter_D = tk.StringVar(), tk.StringVar()

        print(self.screenHeight, self.screenWidth)
        print(self.master.winfo_screenmmheight(), self.master.winfo_screenmmwidth())

        self.timeLabel = ttk.Label(self.leftData, text="Time:", font=self.labelFont, style="G.TLabel", anchor=tk.CENTER)
        self.timeVar = ttk.Label(self.leftData, textvariable=self.tP, font=self.labelFont, style="W.TLabel")

        self.cdaDeploy1 = ttk.Label(self.leftData, text="CDA 1:", font=self.labelFont, style="B.TLabel")
        self.cdaDeployVar1 = ttk.Label(self.leftData, textvariable=self.cda_D1, font=self.labelFont, style="W.TLabel")
        self.timeLabelC1 = ttk.Label(self.leftData, text="Deploy Time:", font=self.labelFont2, style="R.TLabel",
                                     anchor=tk.E)
        self.timeVarC1 = ttk.Label(self.leftData, textvariable=self.tP2, font=self.labelFont2, style="Y.TLabel")

        self.cdaDeploy2 = ttk.Label(self.leftData, text="CDA 2:", font=self.labelFont, style="B.TLabel")
        self.cdaDeployVar2 = ttk.Label(self.leftData, textvariable=self.cda_D2, font=self.labelFont, style="W.TLabel")
        self.timeLabelC2 = ttk.Label(self.leftData, text="Deploy Time:", font=self.labelFont2, style="R.TLabel",
                                     anchor=tk.E)
        self.timeVarC2 = ttk.Label(self.leftData, textvariable=self.tP2, font=self.labelFont2, style="Y.TLabel")

        self.cdaDeploy3 = ttk.Label(self.leftData, text="CDA 3:", font=self.labelFont, style="B.TLabel")
        self.cdaDeployVar3 = ttk.Label(self.leftData, textvariable=self.cda_D3, font=self.labelFont, style="W.TLabel")
        self.timeLabelC3 = ttk.Label(self.leftData, text="Deploy Time:", font=self.labelFont2, style="R.TLabel",
                                     anchor=tk.E)
        self.timeVarC3 = ttk.Label(self.leftData, textvariable=self.tP2, font=self.labelFont2, style="Y.TLabel")

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

        # Time variables
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.hTime = str(self.hour)
        self.mTime = str(self.minute)
        self.sTime = str(self.second)
        self.strTime = ""
        self.strTime2 = ""

        self.notebook.pack()

        col_count, row_count = self.master.grid_size()
        for col in range(col_count):
            self.master.grid_columnconfigure(col, minsize=5)
        for row in range(row_count):
            self.master.grid_rowconfigure(row, minsize=5)

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

        # David
        # Configuration of scrollbar
        self.tree.column("#0", anchor=tk.CENTER, width=col_width - 25)
        for col in self.tree["columns"]:
            self.tree.column(col, anchor=tk.CENTER, width=col_width)

        self.scrollbar.config(command=self.tree.yview)

        self.tree.pack(side=tk.LEFT)
        self.scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        # positions the scrollbar at the right (sticky = coordinates)

        self.table()
        self.master.mainloop()

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
        self.tP2.set(self.strTime2)

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

    # Jorge
    def handle_click(self, event):  # Function to prevent resize on the headings
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"


root = Draft1(tk.Tk())