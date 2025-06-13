from turtle import Turtle, Screen
import random
import time

class PongBall(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1)
        self.goto(0, random.randint(-150, 150))
        self.color("black")
        # self.speed("normal")
        


    def turn1(self): 
            dx= self.xcor() + 10
            if self.ycor() >=0:
                dy= self.ycor() + 10
                self.goto(dx, dy)
            else:
                dy= self.ycor() - 10
                self.goto(dx, dy)  

            
            


    def turn2(self):
            dx= self.xcor() + 10
            if self.ycor() >=0:
                dy= self.ycor() + 10
                self.goto(dx, dy)
            else:
                dy= self.ycor() - 10
                self.goto(dx, dy)  

    # def initial_movement(self):
         



    

