import tkinter as tk
from tkinter import ttk
import time
import datetime as dt
from serial import Serial


serialPort = "COM6"
baudRate = 9600

ser = Serial()