from turtle import Turtle

class StateNameCreator(Turtle):
    def __init__(self, to_write):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state_name = to_write

    def teleport_name(self, x, y):
        self.goto(x, y)  
        self.write(self.state_name, align="center", font=("Arial", 8, "normal"))