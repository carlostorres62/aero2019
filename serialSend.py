from serial import Serial

serial = Serial("COM6", 9600)
c = serial.write(1)


