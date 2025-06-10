
from turtle import Turtle

import random


class SnakeFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.penup()
        self.new_pos()


    def new_pos(self):
        new_x = random.randint(-300,300)
        new_y = random.randint(-300,300)
        self.goto(new_x, new_y)



    









