import turtle
import random
kaks = turtle.Turtle()
kaks.shape('turtle')
colors = ['violet', 'blue', 'green', 'red', 'gray', 'purple', 'pink', 'yellow', 'teal','white','black']
for c in range(360):
    color = random.choice(colors)
    kaks.forward(1)
    kaks.color(color)
    kaks.left(1)