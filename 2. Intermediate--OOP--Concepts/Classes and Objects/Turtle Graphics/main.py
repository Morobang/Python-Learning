import turtle
import math

Rocket = turtle.Turtle()
Rocket.penup()
Rocket.backward(150)
Rocket.pendown()
Rocket.shape("turtle")
Rocket.color("Red", "Yellow")
Rocket.speed(0)

Rocket.begin_fill()
for i in range(1000):
    Rocket.forward(1)
    Rocket.left(math.sin(math.radians(90)))
Rocket.end_fill()

turtle.done()
