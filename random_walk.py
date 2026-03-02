from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
angles= [90,180,270, 360]

screen = Screen()
screen.colormode(255)
perro = Turtle()
perro.pensize(10)
perro.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)


while 1:
    color = random_color()
    perro.color(color)
    perro.setheading(random.choice(angles))
    perro.fd(30)


screen.exitonclick()