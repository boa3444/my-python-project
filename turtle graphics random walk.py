from turtle import Turtle, Screen
from turtlegraphicscolorslist import *
import random
john_the_don = Turtle()
my_scr = Screen()
my_scr.bgcolor("black")
john_the_don.shape("circle")
john_the_don.shapesize(1.0)
john_the_don.width(15)
# possible_steps = [0,15]
possible_angles = [0,90,180,270]
go_on = True
while go_on:
    def motion():
        john_the_don.color(random.choice(turtle_colors))
        john_the_don.fd(40)
        john_the_don.setheading(random.choice(possible_angles))
        
        
    motion()
my_scr.exitonclick()

