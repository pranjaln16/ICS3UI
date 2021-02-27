#Rainbow Target
#October 2020
#Pranjal Nayak

from tkinter import *
from random import *
from math import *

myWindow = Tk()
screen = Canvas(myWindow, width=600, height=600, background="white")
screen.pack()

#created dots
for f in range(15000):
   x = randint(0, 700)
   y = randint(0, 700)
   r = sqrt((300 - x) ** 2 + (300 - y) ** 2)

#creates dots of color when needed
   if r <= 100:
       c = "red"

   elif r <= 200:
       c = "blue"

   elif r <= 300:
       c = "green2"

   elif r <= 400:
       c = "black"

   elif r <= 500:
       c = "purple"

   dot = screen.create_oval(x, y, x + 4, y + 4, fill=c, outline=c)

screen.mainloop()
