from turtle import Turtle



def zebra_cross():

    set_x = 0
    set_y = 280

    for zc in range(10):
        zc = Turtle("square")
        zc.color("white")
        zc.shapesize(1.5,5)
        zc.penup()
        set_y -= 60
        zc.goto(set_x, set_y )
    