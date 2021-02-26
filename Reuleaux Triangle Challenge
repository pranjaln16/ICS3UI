#The Reuleaux Triangle (consturcted with 'create_arc' command)
#October 2020
#Pranjal Nayak

import tkinter as tk 
from math import sin, radians

def create_reuleaux_triangle(canv, x, y, r, color='black'):
    x1 = x + r / 2
    y1 = y - r * sin(radians(60))
    #First Arc of the Reuleaux Triangle:
    canv.create_arc(x-r, y-r, x+r, y+r, extent=60, style='chord', fill="green")

    #Second Arc of the Reuleaux Triangle:
    canv.create_arc(x, y-r, x+r+r, y+r, start=120, extent=60, style='chord', fill="red")
    
    #Third Arc of the Reuleaux Triangle:
    canv.create_arc(x1-r, y1-r, x1+r, y1+r, start=240, extent=60, style='chord', fill="blue")

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(fill='both', expand=1)
create_reuleaux_triangle(canvas, 50, 200, 200, 'red')

root.mainloop
