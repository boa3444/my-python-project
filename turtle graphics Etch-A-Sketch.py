from turtle import Turtle, Screen
t= Turtle()
my_scr = Screen()
t.shape("turtle")
t.color("white")
my_scr.bgcolor("black")
t.pensize(5)

def forwards():
    t.fd(20)

def backwards():
    t.backward(20)

def anticlockwise():
    t.lt(5)

def clockwise():
    t.rt(5)
def cleareverything():
    t.clear()
my_scr.listen()
my_scr.onkey(key= "Up", fun= forwards)
my_scr.onkey(key="Down", fun= backwards)
my_scr.onkey(key= "Right", fun = clockwise)
my_scr.onkey(key="Left", fun = anticlockwise)
my_scr.onkey(key= "space", fun = cleareverything )
my_scr.exitonclick()