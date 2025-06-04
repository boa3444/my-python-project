from turtle import Turtle, Screen, colormode
from turtlegraphicscolorslist import *
import random
colormode(255)
john_the_don = Turtle()
john_the_don.speed(0)
my_scr = Screen()
number_of_circles= 150
while number_of_circles>0:
    john_the_don.color(random.choice(turtle_colors))
    john_the_don.left(10)
    john_the_don.circle(100)
    number_of_circles-=1


my_scr.exitonclick()

