#Flying Animation 
#October2020
#Pranjal Nayak

#In this animation, there is a hot air balloon flying through the air, it collides with a tower.
#When it collides with the tower, all the air is deflating, where the balloon seeps down to the bottom.

from tkinter import *
from math import *
from time import *
from random import *

myInterface = Tk()
screen = Canvas( myInterface, width=1280, height=720, background = "black" )
screen.pack()

#gridlines
#spacing = 50

#for x in range(0, 1250, spacing): 
# screen.create_line( x, 25, x, 1250, fill="blue")
# screen.create_text( x, 5, text=str(x), font="Times 9", anchor = N)

#for y in range(0, 1250, spacing):
# screen.create_line( 25, y, 1250, y, fill="blue")
# screen.create_text( 5, y, text=str(y), font="Times 9", anchor = W)


#arrays for the star background 
xs = []
ys = []
starDrawings = []
numStars = 750

#star positions
for i in range(numStars):
    xs.append( randint(0,1250 ))
    ys.append( randint(0,1250 ))
    starDrawings.append( 0 )
    starDrawings[i] = screen.create_oval(xs[i]-2, ys[i]-2, xs[i]+2, ys[i]+2, fill="white")

#fixed flying positions
x = 100
y = 100

#ground
screen.create_rectangle(0, 600, 1280, 1280, fill = "chartreuse3")
screen.create_rectangle(0, 630, 1280, 1280, fill = "saddle brown")


#house 1
screen.create_rectangle(50, 600, 200, 450, fill = "dark goldenrod")
screen.create_rectangle(100, 600, 150, 500, fill = "gold")
screen.create_rectangle(100, 450, 150, 350, fill= "brown")
screen.create_polygon(100, 350, 50, 450, 100, 450, fill= "brown")
screen.create_polygon(150, 350, 200, 450, 150, 450, fill= "brown")

#house 2
screen.create_rectangle(300, 600, 450, 450, fill = "dark goldenrod")
screen.create_rectangle(350, 600, 400, 500, fill = "gold")
screen.create_rectangle(350, 450, 400, 350, fill= "brown")
screen.create_polygon(350, 350, 300, 450, 350, 450, fill= "brown")
screen.create_polygon(400, 350, 450, 450, 400, 450, fill= "brown")

#house 3
screen.create_rectangle(550, 600, 700, 450, fill = "dark goldenrod")
screen.create_rectangle(600, 600, 650, 500, fill = "gold")
screen.create_rectangle(600, 450, 650, 350, fill= "brown")
screen.create_polygon(600, 350, 550, 450, 600, 450, fill= "brown")
screen.create_polygon(650, 350, 700, 450, 650, 450, fill= "brown")

#house 4
screen.create_rectangle(800, 600, 950, 450, fill = "dark goldenrod")
screen.create_rectangle(850, 600, 900, 500, fill = "gold")
screen.create_rectangle(850, 450, 900, 350, fill= "brown")
screen.create_polygon(850, 350, 800, 450, 900, 450, fill= "brown")
screen.create_polygon(900, 350, 950, 450, 900, 450, fill= "brown")

#tower 
screen.create_rectangle(1050, 600, 1200, 450, fill = "dark goldenrod")
screen.create_rectangle(1100, 600, 1150, 500, fill = "gold")
crashWall = screen.create_rectangle(1050, 450, 1200, 100, fill = "brown")
screen.create_rectangle(1100, 200, 1150, 150, fill = "gold")
screen.create_rectangle(1100, 300, 1150, 250, fill = "gold")
screen.create_rectangle(1100, 400, 1150, 350, fill = "gold")


#animation:

#1st stage: flying
for i in range(60):
    body = screen.create_rectangle(x, y+100, x+150, y, fill = "gold")   
    tip = screen.create_polygon(x+150, y+100, x+200, y+50, x+150, y, fill = "blue")
    
    screen.update()
    sleep(0.03)
#speed
    screen.delete(body, tip)
    x += 15

#2nd stage: crash/break
body = screen.create_rectangle(x, y+100, x+150, y, fill = "gold")   
tip = screen.create_polygon(x+150, y+100, x+200, y+50, x+150, y, fill = "blue")

screen.update()
sleep(0.6)
screen.delete(body, tip)

#3rd stage: falling

#falling fixed positions:
a = 700
b = 100

#fall to ground:
for i in range(100):
    bodyFall = screen.create_rectangle(a+250, b+150, a+350, b, fill = "light goldenrod")
    tipFall = screen.create_polygon(a+250, b+150, a+300, b+200, a+350, b+150, fill = "royal blue")
    
    screen.update()
    sleep(0.03)
    screen.delete(bodyFall, tipFall)
    b += 10
