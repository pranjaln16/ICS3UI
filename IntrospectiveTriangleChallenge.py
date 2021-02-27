#Introspective Triangle
#Ocotber 2020
#Pranjal Nayak

from tkinter import *
from random import*

myWindow = Tk()
screen = Canvas( myWindow, width=600, height=600, background = "black" )
screen.pack()

colour =["blue","white"]

#placments
x = 300
y = 0
x1 = 0
y1 = 600
x2 = 600
y2 = 600

#asks users how much they want to repeat
z = int(input("How many times (1 to 8) would you like the program to repeat?: "))

for i in range(z):
    triangle = screen.create_polygon(x,y,x1,y1,x2,y2 , fill = choice(colour),outline = "black")

#calculating the midpoints
    x4 = x1
    y4 = y1
    
    x1 = (x+x1)/2
    y1 = (y+y1)/2
    
    x = (x+x2)/2
    y = (y+y2)/2

    
    x2 = (x4+x2)/2
    y2 = (y4+y2)/2
