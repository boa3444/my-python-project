from turtle import *
import random

kitty = Turtle()
kitty.shape("arrow")
kitty.color("medium purple")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]


screen = Screen()

for side in range (3,11):
    if side == 7 or side == 9:
        continue

    print(side)
    turn_angle = 180 +  (((side-2)* 180) /side)
    print(turn_angle)
    for _ in range(side):
        kitty.color(random.choice(colors))
        kitty.fd(100)
        kitty.right(turn_angle)

screen.exitonclick()