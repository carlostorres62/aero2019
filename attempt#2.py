from tkinter import *
from tkinter.ttk import *
import time
import datetime as dt

master = Tk()
master.title("Aero Design")
master.resizable(0,0)


scrollbar = Scrollbar(master, orient=VERTICAL)
tree = Treeview(master, height=5, columns=5, yscrollcommand=scrollbar.set)

style = Style()
style.configure("Treeview.Heading", font=(None, 15))

height = 40
tree["height"] = height
tree["columns"] = ("one","two","three","four","five")
tree.heading("#0", text="Data", anchor=CENTER)
tree.heading("one", text="Time", anchor=CENTER)
tree.heading("two", text="Altitude (Feet)", anchor=CENTER)
tree.heading("three", text="ParamX", anchor=CENTER)
tree.heading("four", text="ParamY", anchor=CENTER)
tree.heading("five", text="ParamZ", anchor=CENTER)

scrollbar.config(command=tree.yview)

tree.grid(row=0, column=0, sticky=W)
scrollbar.grid(row=0, column=1, sticky=N + S)  # positions the scrollbar at the right (sticky = coordinates)

nums = [i for i in range(51)]
tList = []
for i in nums:
    if i == 0:
        pass
    else:
        hour = dt.datetime.now().hour
        minute = dt.datetime.now().minute
        second = dt.datetime.now().second
        hTime = str(hour)
        if minute < 10:
            mTime = "0" + str(minute)
        else:
            mTime = str(minute)
        if second < 10:
            sTime = "0" + str(second)
        else:
            sTime = str(second)
        tList = [(hTime, mTime, sTime)]
        for hr, min,sec in tList:
            tree.insert("", i, text = str(i) , values = (hr + ":" + min + ":" + sec))
        tList = []
        tree.update()


    def handle_click(event):
        if tree.identify_region(event.x, event.y) == "separator":
            return "break"


    tree.bind('<Button-1>', handle_click)
    tree.bind('<Motion>', handle_click)
    time.sleep(1)


master.mainloop()