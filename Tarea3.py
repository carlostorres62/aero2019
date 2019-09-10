import calendar
from random import randint
from tkinter import *
from tkinter import font, ttk
from tkinter.ttk import *
import time
import datetime as dt
import tkinter as tk
import pandas as pd


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)



        self.title("Aero Design")

        w, h = self.winfo_screenwidth(), self.winfo_screenheight()

        self.geometry("%dx%d+0+0" % (w, h))
        self.resizable(0, 0)

        self.configure(background="white")

        master = tk.Frame(self)

        master.configure(background="pink")

        master.pack(side="top", fill="both") #expand=true

        # self.frames = {}

        # for F in (StartPage, DataPage):
        frame = DataPage(self, master)

            # self.frames[F] = frame
        frame.pack(fill=X)
        # frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(StartPage)


    # def show_frame(self, cont):
    #     frame = self.frames[cont]

        frame.tkraise()

class DataPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        # print(parent.configure())
        self.configure(bg="yellow")

        treeFrame = Frame(self)
        # treeFrame.geometry("500x500")
        treeFrame.pack_propagate(0)

        treeFrame.pack(side=LEFT)

        # treeFrame.grid(row=0, column=0)

        yscrollbar = Scrollbar(treeFrame, orient=VERTICAL)
        # xscrollbar = Scrollbar(treeFrame, orient=HORIZONTAL)

        self.tree = Treeview(treeFrame, height=5, columns=5, yscrollcommand=yscrollbar.set)

        style = Style()
        style.configure("Treeview.Heading", font=(None, 15))  # Configures the size of the headings

        height = 40 # Sets height size for tree
        # width = treeFrame["width"]
        # self.tree["width"] = width
        self.tree["height"] = height
        self.tree["columns"] = ("one", "two", "three", "four", "five")
        self.tree.heading("#0", text="Data", anchor=CENTER)
        self.tree.heading("one", text="Time", anchor=CENTER)
        self.tree.heading("two", text="Altitude (Feet)", anchor=CENTER)
        self.tree.heading("three", text="ParamX", anchor=CENTER)
        self.tree.heading("four", text="ParamY", anchor=CENTER)
        self.tree.heading("five", text="ParamZ", anchor=CENTER)

        col_width = 160
        print("treeFrame width: "+str(col_width))

        for col in self.tree['columns']:
            # self.tree.heading(col, text="Column {}".format(col), anchor=tk.CENTER)
            self.tree.column(col, anchor=tk.CENTER, width=col_width)  # s


        yscrollbar.config(command=self.tree.yview)
        # xscrollbar.config(command=self.tree.xview)


        self.tree.grid(row=0, column=0, sticky=W)
        yscrollbar.grid(row=0, column=1, sticky=N + S)  # positions the scrollbar at the right (sticky = coordinates)
        # xscrollbar.grid(row=1, column=1, sticky=N + S)

        labelFrame = LabelFrame(self, text="Informacion super mega importante")
        # labelFrame.grid(row=0, column=2, sticky=E)

        labelFrame.pack(side=RIGHT, fill=Y)
        labelFrame.propagate(0)

        # parent.grid_columnconfigure(0, weight=1) #importante
        # parent.grid_columnconfigure(1, weight=1)
        # parent.grid_columnconfigure(2, weight=0)

        self.grid_columnconfigure(0, weight=1)  # importante
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        label = LabelPair(labelFrame, "CDA Released", "NO")
        label.grid(row=0,column=0)
        label = LabelPair(labelFrame, "Payload Released", "NO")
        label.grid(row=1, column=0)

        clock = Clock(labelFrame)
        clock.grid(row=2, column=0)

        self.df = pd.read_csv("test.csv")

        self.update()

        def handle_click(event):  # Function to prevent resize on the headings
            if self.tree.identify_region(event.x, event.y) == "separator":
                return "break"

        self.tree.bind('<Button-1>', handle_click)


    def update(self):

        new_row = {'Speed': randint(0,10), 'Height': randint(0,10), 'Weight': randint(0,10)}
        # append row to the dataframe
        self.df = self.df.append(new_row, ignore_index=True)

        speed = list(self.df['Speed'])
        height = list(self.df["Height"])
        weight = list(self.df["Weight"])

        self.tree.delete(*self.tree.get_children())
        for i in range(len(speed)):
            self.tree.insert("", i, text=str(i), values=(speed[i], height[i], weight[i]))

        self.after(5000, self.update)



class LabelPair(Frame):
    def __init__(self, parent, name, num):
        Frame.__init__(self, parent)



        letra = font.Font(family='Helvetica', size=24, weight='bold')

        self.label = Label(self, text=name, font=letra)
        self.label.pack(side=LEFT, fill=X)

        self.number = Label(self, text=num, font=letra)
        self.number.pack(side=RIGHT, fill=X)

class Clock(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.start_time = time.time()


        self.start_min = dt.datetime.now().minute
        self.start_second = dt.datetime.now().second

        letra = font.Font(family='Helvetica', size=24, weight='bold')

        self.label = Label(self, text="Time: ", font=letra)
        self.label.pack(side=LEFT, fill=X)

        self.number = Label(self, text=0, font=letra)
        self.number.pack(side=RIGHT, fill=X)

        self.update()

    def update(self):
        elapsed_time = time.time() - self.start_time

        minutos = str(int(elapsed_time/60))
        segundos = str(int(elapsed_time%60))

        if int(segundos)<10:
            num = minutos + " : " + "0"+segundos
        else:

            num = minutos + " : " + segundos
        self.number.configure(text=num)
        self.after(1000, self.update)


app = App()
app.mainloop()