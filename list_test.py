from tkinter import *
from tkinter.ttk import *

master = Tk()
master.title("Aero Design")
master.geometry("570x357+375+50")  # screen position (x, y)

# test variables
cda, water, shelter = False, False, False
alt, weight, time = 0, 0, 0

if not cda:
    cda = "No"
else:
    cda = "Yes"
if not water:
    water = "No"
else:
    water = "Yes"
if not shelter:
    shelter = "No"
else:
    shelter = "Yes"


def table():  # function if button is pressed (command)

    # scrolls vertically with orient and yscrollcommand function
    scrollbar = Scrollbar(master, orient=VERTICAL)

    tree = Treeview(master, height=5, columns="One", yscrollcommand=scrollbar.set)

    # variables set for the table
    flight = [("CDA", cda), ("Water", water), ("Shelter", shelter), ("Altitude", alt),
              ("Weight", weight), ("Time", time), ("Test 1", cda), ("Test 2", cda),
              ("Test 3", alt), ("Test 4", alt)]

    # sets the style of the strings in Treeview
    style = Style()
    style.configure("Treeview.Heading", font=("Helvetica", 35))  # style for the heading
    style.configure("Treeview", font=("Helvetica", 30), rowheight=60)  # style for the rest of the table

    tree.column("#0", width=275, minwidth=275)
    tree.column("#1", width=275, minwidth=275, anchor=CENTER)

    # places the heading on gui
    tree.heading("#0", text="Components", anchor=CENTER)
    tree.heading("#1", text="Variables", anchor=CENTER)

    # places the text and values in the table created
    index = 0
    for string, var in flight:
        tree.insert("", index, text=string, values=var)
        index += 1

    scrollbar.config(command=tree.yview)

    tree.grid(row=0, column=0, sticky=W)
    scrollbar.grid(row=0, column=1, sticky=N + S)  # positions the scrollbar at the right (sticky = coordinates)

    button.destroy()  # button disappears


button = Button(master, text="Flight Data", width=20, command=table)
button.place(relx=0.5, rely=0.5, anchor=CENTER)  # positions the button

master.mainloop()
