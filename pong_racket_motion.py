
from turtle import Turtle, Screen
my_scr = Screen()




class RacketCreator(Turtle):

    def __init__(self, set_x):
        super().__init__()
        # self.speed("fastest")
        self.shape("square")
        
        self.shapesize(3,1)
        self.color("white")
        self.penup()
        # my_scr.tracer(False)
        self.goto(set_x, 0)
        # my_scr.tracer(True)
        




    def RacketMotion1(self):

        def move_up():
            new_y= self.ycor() + 30
            if new_y < 300 :
                self.sety(new_y)


        def move_down():
            new_y= self.ycor() - 30
            if new_y > -300 :
                self.sety(new_y)


                
        my_scr.listen()

        my_scr.onkey(move_up, "q")
        my_scr.onkey(move_down, "a")

    
    def RacketMotion2(self):

        def move_up():
            new_y= self.ycor() + 30
            if new_y < 300 :
                self.sety(new_y)


        def move_down():
            new_y = self.ycor() - 30
            if new_y > -300:
                self.sety(new_y)

        my_scr.listen()

        my_scr.onkey(move_up, "p")
        my_scr.onkey(move_down, "l")






        