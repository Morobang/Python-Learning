from turtle import Turtle , Screen
import another_module


print(another_module.variable)

timmy = Turtle()
rocket = Turtle()
timmy.shape("turtle")
timmy.color("brown")
timmy.forward(100)
rocket.backward(100)
rocket.left(60)
rocket.forward(100)

my_screen = Screen()
print(my_screen.canvwidth)
my_screen.exitonclick()