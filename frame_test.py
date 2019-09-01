from tkinter import *

master = Tk()
master.title("Aero Design")
master.geometry("600x500+350+50")  # screen size (width x height) and position (x, y)
master.resizable(width=False, height=False)  # screen can't resize

# test values
cda = False
water = False
shelter = False
alt = 0
weight = 0
time = 0

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

frame1 = Frame(master, height=500, width=580)
frame2 = Frame(master, height=500, width=20)

# frames doesn't resize
frame1.grid_propagate(0)
frame2.grid_propagate(0)

# dictionaries for table (with its rows and columns) to be created
flights = {
    1: {'Column1': 'CDA', 'Column2': cda},
    2: {'Column1': 'Water', 'Column2': water},
    3: {'Column1': 'Nerf', 'Column2': shelter},
    4: {'Column1': 'Altitude', 'Column2': alt},
    5: {'Column1': 'Weight', 'Column2': weight},
    6: {'Column1': 'Time', 'Column2': time}
}


def DataTable():
    # function if button is pressed (command)
    for column, row in enumerate(flights):
        Label(master).grid(row=1, column=0 + column)

    # creates the table of the flights
    for row, element in enumerate(flights.values()):
        for column, (key, value) in enumerate(element.items()):
            frame1.data = Label(frame1, text=value, font=("Helvetica", 45), bd=15)
            frame1.data.grid(row=1 + row, column=0 + column, sticky=W)

    frame1.button.destroy()  # button disappears


# positions the frames inside the screen
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1, sticky=N)

frame1.button = Button(master, text="Flight Data", fg="red", command=DataTable)
frame1.button.grid(row=0, column=0, sticky=N)  # positions the button inside frame1 (sticky = coordinates)

frame2.scrollbar = Scrollbar(master, width=20)
frame2.scrollbar.grid(row=0, column=1, sticky=N+S)  # positions the scrollbar inside frame2 (sticky = coordinates)

master.mainloop()
