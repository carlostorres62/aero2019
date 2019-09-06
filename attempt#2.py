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
style.configure("Treeview.Heading", font=(None, 15))   #Configures the size of the headings

height = 40         #Sets height size for tree
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

nums = [i for i in range(51)]     #List comprehension to obtain list of numbers/ can be changed to desired number
tList = []      #Empty List created to store the actual time
for i in nums:
    if i == 0:
        pass
    else:
        hour = dt.datetime.now().hour    #Obtains the current hour
        minute = dt.datetime.now().minute   #Obtains the current minute
        second = dt.datetime.now().second   #Obtains the current second
        hTime = str(hour)
        if minute < 10:
            mTime = "0" + str(minute)    #Concatenate a 0 in front of number in case it is a single digit number
        else:
            mTime = str(minute)
        if second < 10:
            sTime = "0" + str(second)   #If second is 5 it would show "05"
        else:
            sTime = str(second)
        tList = [(hTime, mTime, sTime)] #Stores the actual time in time list
        for hr, min,sec in tList:
            tree.insert("", i, text = str(i) , values = (hr + ":" + min + ":" + sec))#Inserts the number of data and current time to tree
        tList = []  #Resets the time list
        tree.update()    #Updates the tree every time it loops


    def handle_click(event):         #Function to prevent resize on the headings
        if tree.identify_region(event.x, event.y) == "separator":
            return "break"
    tree.bind('<Button-1>', handle_click)
    
    
    time.sleep(1)
master.mainloop()
