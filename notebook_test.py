import tkinter as tk
import datetime as dt
from random import randint
from tkinter import ttk


class Draft1:
    def __init__(self, master):

        # Standard configuration
        self.master = master
        self.master.title("Aero Design")
        self.master.state('zoomed')
        self.master.configure(background="Dim Grey")

        self.style = ttk.Style()
        self.style.theme_use("classic")

        # font sizes (in Mac font must be +20)
        variant = 20
        self.fsize = 65 + variant
        self.fsize2 = 30 + variant


        # Configures the style of the tree headings
        self.style.configure("Treeview.Heading", font=(None, 25))
        self.style.configure("Treeview", font=(None, 20), rowheight=40, fieldbackground="Dim Grey")

        # Configures the style of the tabs
        self.style.configure("TNotebook.Tab", font=("Helvetica", 20))
        self.style.configure("TNotebook", background="Dim Grey")


        # Configures the background and font colors
        self.style.configure("DG.TLabel", background="Dim Grey")
        self.style.configure("B.TLabel", foreground="Blue", background="Dim Grey")
        self.style.configure("R.TLabel", foreground="Red", background="Dim Grey")
        self.style.configure("G.TLabel", foreground="Dark Green", background="Dim Grey")
        self.style.configure("Y.TLabel", foreground="Gold", background="Dim Grey")
        self.style.configure("W.TLabel", foreground="Black", background="Dim Grey")
        self.style.configure("Vertical.TScrollbar", troughcolor="Dim Grey")

        self.notebook = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.notebook, style="DG.TLabel")
        self.tab2 = ttk.Frame(self.notebook, style="DG.TLabel")

        self.notebook.add(self.tab1, text="Data")
        self.notebook.add(self.tab2, text="Table")

        # Scrollbar and table initialization
        self.scrollbar = ttk.Scrollbar(self.tab2, orient=tk.VERTICAL, style="Vertical.TScrollbar")
        self.tree = ttk.Treeview(self.tab2, yscrollcommand=self.scrollbar.set)

        # Jorge
        # Configuration of the tree's appeareance
        self.height = int((self.master.winfo_screenheight() / 20) - 22)  # Sets height size for tree
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

        print(int(self.master.winfo_screenwidth()))
        self.labelWidth = round(self.master.winfo_screenwidth()/192)
        self.labelWidth2 = int(self.master.winfo_screenwidth()/110) # + 22 in Mac


        self.timeLabel = ttk.Label(self.tab1, text="Time:", font=("Helvetica", self.fsize), style="G.TLabel",
                                   width=self.labelWidth, anchor=tk.E)
        self.timeVar = ttk.Label(self.tab1, textvariable=self.tP, font=("Helvetica", self.fsize), style="W.TLabel",
                                 width=self.labelWidth, anchor=tk.W)

        self.cdaDeploy1 = ttk.Label(self.tab1, text="CDA 1:", font=("Helvetica", self.fsize), style="B.TLabel",
                                    width=self.labelWidth, anchor=tk.E)
        self.cdaDeployVar1 = ttk.Label(self.tab1, textvariable=self.cda_D1, font=("Helvetica", self.fsize),
                                       style="W.TLabel", width=self.labelWidth, anchor=tk.W)
        self.timeLabelC1 = ttk.Label(self.tab1, text="Deploy Time:", font=("Helvetica", self.fsize2), style="R.TLabel",
                                     width=self.labelWidth2, anchor=tk.E)
        self.timeVarC1 = ttk.Label(self.tab1, textvariable=self.tP2, font=("Helvetica", self.fsize2), style="Y.TLabel",
                                   width=self.labelWidth2, anchor=tk.W)

        self.cdaDeploy2 = ttk.Label(self.tab1, text="CDA 2:", font=("Helvetica", self.fsize), style="B.TLabel",
                                    width=self.labelWidth, anchor=tk.E)
        self.cdaDeployVar2 = ttk.Label(self.tab1, textvariable=self.cda_D2, font=("Helvetica", self.fsize),
                                       style="W.TLabel", width=self.labelWidth, anchor=tk.W)
        self.timeLabelC2 = ttk.Label(self.tab1, text="Deploy Time:", font=("Helvetica", self.fsize2), style="R.TLabel",
                                     width=self.labelWidth2, anchor=tk.E)
        self.timeVarC2 = ttk.Label(self.tab1, textvariable=self.tP2, font=("Helvetica", self.fsize2), style="Y.TLabel",
                                   width=self.labelWidth2, anchor=tk.W)

        self.cdaDeploy3 = ttk.Label(self.tab1, text="CDA 3:", font=("Helvetica", self.fsize), style="B.TLabel",
                                    width=self.labelWidth, anchor=tk.E)
        self.cdaDeployVar3 = ttk.Label(self.tab1, textvariable=self.cda_D3, font=("Helvetica", self.fsize),
                                       style="W.TLabel", width=self.labelWidth, anchor=tk.W)
        self.timeLabelC3 = ttk.Label(self.tab1, text="Deploy Time:", font=("Helvetica", self.fsize2), style="R.TLabel",
                                     width=self.labelWidth2, anchor=tk.E)
        self.timeVarC3 = ttk.Label(self.tab1, textvariable=self.tP2, font=("Helvetica", self.fsize2), style="Y.TLabel",
                                   width=self.labelWidth2, anchor=tk.W)

        self.altitude = ttk.Label(self.tab1, text="Altitude:", font=("Helvetica", self.fsize), style="G.TLabel",
                                  width=self.labelWidth, anchor=tk.E)
        self.altitudeVar = ttk.Label(self.tab1, textvariable=self.altP, font=("Helvetica", self.fsize),
                                     style="W.TLabel", width=self.labelWidth-2, anchor=tk.W)

        self.waterDeploy = ttk.Label(self.tab1, text="Water:", font=("Helvetica", self.fsize), style="B.TLabel",
                                     width=self.labelWidth, anchor=tk.E)
        self.waterDeployVar = ttk.Label(self.tab1, textvariable=self.water_D, font=("Helvetica", self.fsize),
                                        style="W.TLabel", width=self.labelWidth-2, anchor=tk.W)
        self.timeLabelW = ttk.Label(self.tab1, text="Deploy Time:", font=("Helvetica", self.fsize2), style="R.TLabel",
                                    width=self.labelWidth2, anchor=tk.E)
        self.timeVarW = ttk.Label(self.tab1, textvariable=self.tP2, font=("Helvetica", self.fsize2), style="Y.TLabel",
                                  width=self.labelWidth2-5, anchor=tk.W)

        self.shelterDeploy = ttk.Label(self.tab1, text="Habitat:", font=("Helvetica", self.fsize), style="B.TLabel",
                                       width=self.labelWidth, anchor=tk.E)
        self.shelterDeployVar = ttk.Label(self.tab1, textvariable=self.shelter_D, font=("Helvetica", self.fsize),
                                          style="W.TLabel", width=self.labelWidth-2, anchor=tk.W)
        self.timeLabelS = ttk.Label(self.tab1, text="Deploy Time:", font=("Helvetica", self.fsize2), style="R.TLabel",
                                    width=self.labelWidth2, anchor=tk.E)
        self.timeVarS = ttk.Label(self.tab1, textvariable=self.tP2, font=("Helvetica", self.fsize2), style="Y.TLabel",
                                  width=self.labelWidth2-5, anchor=tk.W)

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

        self.timeLabel.grid(row=0, column=0)
        self.timeVar.grid(row=0, column=1)
        self.altitude.grid(row=0, column=2)
        self.altitudeVar.grid(row=0, column=3)

        self.cdaDeploy1.grid(row=1, column=0)
        self.cdaDeployVar1.grid(row=1, column=1)
        self.timeLabelC1.grid(row=2, column=0)
        self.timeVarC1.grid(row=2, column=1)

        self.cdaDeploy2.grid(row=3, column=0)
        self.cdaDeployVar2.grid(row=3, column=1)
        self.timeLabelC2.grid(row=4, column=0)
        self.timeVarC2.grid(row=4, column=1)

        self.cdaDeploy3.grid(row=5, column=0)
        self.cdaDeployVar3.grid(row=5, column=1)
        self.timeLabelC3.grid(row=6, column=0)
        self.timeVarC3.grid(row=6, column=1)

        self.waterDeploy.grid(row=1, column=2)
        self.waterDeployVar.grid(row=1, column=3)
        self.timeLabelW.grid(row=2, column=2)
        self.timeVarW.grid(row=2, column=3)

        self.shelterDeploy.grid(row=3, column=2)
        self.shelterDeployVar.grid(row=3, column=3)
        self.timeLabelS.grid(row=4, column=2)
        self.timeVarS.grid(row=4, column=3)

        # David
        # Configuration of scrollbar
        col_width = int(self.master.winfo_screenwidth() / 8)
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
