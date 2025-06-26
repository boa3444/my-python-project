from turtle import Turtle

class Score(Turtle):
    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-430,250)
        self.pendown()
        self.write("Score: 0/50", font= ("Arial", 28, "normal"))
        
        
    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}/50", font= ("Arial", 28, "normal"))