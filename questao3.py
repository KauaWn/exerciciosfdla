import turtle

kaks = turtle.Turtle()
kaks.shape('triangle')
kaks.pensize(2)

for color in ['black', 'purple', 'violet', 'pink']:
    kaks.color(color)
    kaks.forward(130)
    kaks.right(90)