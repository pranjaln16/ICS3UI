#PacMan Animation
#October 2020
#Pranjal Nayak

from tkinter import *
from time import*

myInterface = Tk()
screen = Canvas( myInterface, width=900, height=480, background = "midnight blue" )
screen.pack()

#PacMan properties
x = 0
y = 300
pacmanSize = 40
pacmanAngle = 60
total = 360- 2*(pacmanAngle)

#Food (for pacman to eat)
numFood = 9
d = 100
space = (1000-d)/numFood
food = []

for j in range (numFood):
    food.append(0)

#Food Settings
for n in range(numFood):
    food[n] = screen.create_oval(d+10,310,d-10,290,fill = "orange",outline ="black")
    d += space
    screen.update()


# NOTE: ('+=' is add AND / '-=' is subtract AND)
#PacMan movement (left to right):
for n in range(numFood+1):
    for a in range(10):
        pacman = screen.create_arc(x-pacmanSize, y-pacmanSize, x+pacmanSize, y+pacmanSize, start= pacmanAngle, extent = total,fill = "yellow",outline = "yellow")
        x+= 5
        pacmanAngle-= 6
        total = 360-2*(pacmanAngle)
        
        screen.update()
        sleep(0.03)
        screen.delete(pacman)
        
    for a in range(10):
        x+= 5
        pacmanAngle+= 6
        total = 360-2*(pacmanAngle)
        pacman = screen.create_arc(x-pacmanSize, y-pacmanSize, x+pacmanSize, y+pacmanSize, start = pacmanAngle, extent = total, fill = "yellow",outline = "yellow")
        screen.update()
        sleep(0.03)

        screen.update()
        screen.delete(pacman)
        screen.delete(food[n])
