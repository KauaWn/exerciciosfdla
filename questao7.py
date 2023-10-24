import turtle

kaks = turtle.Turtle()
kaks.color('black')

for _ in range(4):
    kaks.left(90)
    kaks.backward(30)

kaks.backward(200)
kaks.backward(40)
kaks.right(90)

for _ in range(3):
  kaks.forward(30)
  kaks.left(90)