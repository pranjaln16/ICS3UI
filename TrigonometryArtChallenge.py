#Random Geometric Design made from Trig Functions
#October 2020
#Pranjal Nayak

from tkinter import *
from math import sin, cos, radians
import time 
root = Tk()

#canvas dimensions:
w = 700
h = 450
canvas = Canvas(width=w, height=h, background='black')
canvas.pack()
colors = ['yellow', 'red', 'blue']

#putting together the drawing:
for lines in range(3, 19):

    #cycle through the list of colors (three colors):
    color = colors[lines % 3]
    root.title("lines = " + str(lines))
    radians = 360 / (lines * 57.5)

    for x in range(lines):

        for y in range(lines):

            #trig functions for the placement of each line:
            canvas.create_line((int)(sin(y * radians) * 225 + 300),(int)(cos(y * radians) * 145 + 170),
            (int)(sin(x * radians) * 225 + 300),(int)(cos(x * radians) * 145 + 170), fill=color)
            root.update()
            
    #time delay of each line drawn:
    time.sleep(1.3)

root.mainloop()
