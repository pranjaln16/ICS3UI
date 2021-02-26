#Cabin Fever
#Pranjal Nayak
#October 2020

#I tried to recreate an image of my childhood. I lived the first chunk of my life in
#Winnipeg, Manitoba where I lived in a small cabin right by the Red River. I fondly remember
#the winter nights, so here is my best replication which I call, "Cabin Fever".

from tkinter import *
from math import *
from time import *
from random import *

myInterface = Tk()
screen = Canvas( myInterface, width=800, height=800, background = "grey8")
screen.pack()

#Stars 
xs = []
ys = []
stars = []
numStars = 600

#Postions (Stars)
for i in range(numStars):
    xs.append( randint(0,800 ))
    ys.append( randint(0,800 ))
    stars.append( 0 )
    stars[i] = screen.create_oval(xs[i]-1, ys[i]-1, xs[i]+1, ys[i]+1, fill="gold", outline = "black")


waves = screen.create_rectangle(0, 850, 850, 600, fill = "blue2", outline = "black")
pier = screen.create_rectangle(0, 600, 400, 595, fill = "grey39", outline = "black")
house = screen.create_rectangle(50, 595, 350, 500, fill = "khaki4", outline = "black")
window1 = screen.create_rectangle(75, 575, 125, 525, fill = "wheat3", outline = "black")
window2 = screen.create_rectangle(275, 575, 325, 525, fill = "wheat3", outline = "black")
door = screen.create_rectangle(175, 595, 225, 525, fill = "brown", outline = "black") 
roof = screen.create_polygon(25, 500, 50, 475, 350, 475, 375, 500, fill = "lemonchiffon4", outline = "black")
chimney = screen.create_rectangle(275, 475, 325, 400, fill = "dim grey", outline = "black")
icesheet = screen.create_rectangle(0, 630, 850, 600, fill = "steelblue2", outline = "black")
snowsheet = screen.create_rectangle(0, 605, 850, 600, fill = "snow", outline = "black")

#Snow
x = []
y = []
snowDrawings = []
numSnow = 600

#Current
wavex = []
wavey = []
waves = []

for i in range(600):
    x.append( randint(0,900 ))
    y.append( randint(0,850 ))
    snowDrawings.append( 0 )
    waves.append(0)
    wavex.append(randint(0, 800))
    wavey.append(randint(650, 800))
    waves.append(0)
    
    
while True:
    
    for i in range(15):
        waves[i] = screen.create_line(wavex[i], wavey[i], wavex[i]+95, wavey[i], fill = "black")
        wavex[i] = wavex[i] + 1
            
        if wavex[i] > 900:
            wavex[i] = -10            

    for i in range(numSnow):
        snowDrawings[i] = screen.create_oval(x[i]-2, y[i]-2, x[i]+2, y[i]+2, fill="white")
        x[i] = x[i] - 10
        if x[i] < 0:
            x[i] = 900

    screen.update()
    sleep(0.1)

    for i in range(600):
        screen.delete(snowDrawings[i])
        screen.delete(waves[i])
