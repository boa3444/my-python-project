from turtle import Turtle, Screen
import time

my_scr = Screen()


coordinates = [(0,0), (-20, 0), (-40,0)]



class Snake():
    def __init__(self):
        self.segments = []
        
    def body(self):

        for coordinate in coordinates:
            segment= Turtle("square")
            segment.color("white")
            segment.shapesize(1)
            segment.speed(3)
            self.segments.append(segment)
            segment.penup()
            segment.goto(coordinate)
                


        self.head = self.segments[0]
        return self.head


    def movement(self):
        head= self.head
        
        def turn_right():
            head.setheading(0)

        def turn_left():
            head.setheading(180)

        def turn_up():
            head.setheading(90)

        def turn_down():
            head.setheading(270)
        
            
        my_scr.listen()
            

        my_scr.onkey(turn_right, "Right")
        my_scr.onkey(turn_left, "Left")
        my_scr.onkey(turn_up, "Up")
        my_scr.onkey(turn_down, "Down")

            
            
                
                

        for i in range(2 ,0, -1):
                    go_to = head.pos() 
                    take_the_front = self.segments[i-1].pos()
                    self.segments[i].goto(take_the_front)

        self.head.fd(20)


