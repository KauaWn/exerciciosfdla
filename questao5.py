import random
import turtle
kaks = turtle.Turtle()
colors = ['black', 'blue' , 'gray' , 'pink']
kaks.pensize(2)
kaks.goto(50,0)
for _ in [1, 2, 3]:
    color = random.choice(colors)
    kaks.color(color)
    kaks.forward(50)
    kaks.right(120)
kaks.home()
for _ in [1, 2, 3, 4]:
  color = random.choice(colors)
  kaks.color(color)
  kaks.forward(150)
  kaks.right(90)