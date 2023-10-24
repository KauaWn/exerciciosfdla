import turtle
import random

import turtle
import random

kaks = turtle.Turtle()
colors = ['blue', 'teal' , 'yellow' , 'black', 'violet', 'pink' , 'green']
kaks.pensize (2)

for _ in range (9):
    color = random.choice(colors)
    kaks.color(color)
    kaks.forward(100)
    kaks.backward(100)
    kaks.right(45)
for _ in range (8):
    color = random.choice(colors)
    kaks.color(color)
    kaks.right(50)
    kaks.forward(100)
    kaks.backward(100)
    kaks.right(50)