from turtle import Turtle, Screen
import time
from pong_racket_motion import RacketCreator
from pong_ball import PongBall
#two player game

#pong court
background = Screen()
background.bgcolor("green")
background.setup(600,600)
background.tracer(False)

# background.tracer(False)
net_y= 0
for each in range(8):
    
    each= Turtle("square")
    each.penup()
    each.color("black")
    each.shapesize(1, 0.3)
    each.teleport(0, net_y)
    net_y+= 33



new_y= 0
for each in range(9):
    
    each= Turtle("square")
    each.penup()
    each.color("black")
    each.shapesize(1, 0.3)
    each.teleport(0, new_y)
    new_y-= 33



#player's rackets

pongball= PongBall()


racket1 = RacketCreator(273)
racket2= RacketCreator(-280)

background.update()  #

#player controls
racket1.RacketMotion2()
racket2.RacketMotion1()


# game_on = True
# while game_on:
time.sleep(0.2)
pongball.turn2()



background.exitonclick()
