from turtle import Turtle
import random
from turtlegraphicscolorslist import turtle_colors
from arcarde_character import background
import string
# from arcarde_character import Character




class GameCars():
    def __init__(self , screen= background):
        self.game_cars = []
        

    def create_cars(self):
        whatever= random.choice(list(string.ascii_lowercase))

        if whatever == 'a' or whatever == 'z' or whatever == 'g' or whatever == 'l' or whatever == 'k' or whatever == 'y':
            car = Turtle("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(turtle_colors))
            self.y= random.randint(-240, 270)
            car.goto(300, self.y)
            self.game_cars.append(car)
            # background.update()

    def movement(self):
   
        for car in self.game_cars:
            car.backward(5)
            
            
            