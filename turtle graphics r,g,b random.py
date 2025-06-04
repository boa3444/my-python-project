from turtle import Turtle, Screen, colormode
from turtlegraphicscolorslist import *
import random
colormode(255)
john_the_don = Turtle()
my_scr = Screen()

def coloring():
    r= random.randint(0,255)
    g=  random.randint(0,255)
    b=  random.randint(0,255)

    result_color = (r,g,b)
    return result_color


my_scr.bgcolor("black")
john_the_don.shape("circle")
john_the_don.shapesize(1.0)
john_the_don.width(15)
# possible_steps = [0,15]
possible_angles = [0,90,180,270]
for _ in range(200):
    
        john_the_don.color(coloring())
        john_the_don.fd(40)
        john_the_don.setheading(random.choice(possible_angles))
        
        
    
my_scr.exitonclick()

