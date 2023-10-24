import turtle
import random
kaks = turtle.Turtle()
colors = ['violet', 'blue' , 'green' , 'red']
kaks.pensize(2)
for _ in [1, 2, 3]:
    color = random.choice(colors)
    kaks.color(color)
    kaks.forward(100)
    kaks.left(120)