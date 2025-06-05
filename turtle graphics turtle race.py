from turtle import Turtle, Screen

import random
my_scr = Screen()
my_scr.setup(500,500)
turtles = [Turtle() for _ in range(6)]       #####
turtle_colors = [
    "red", "blue", "green", "yellow", "orange", "purple",
    "pink", "black", "gray", "brown", "cyan", "magenta"
]

set_x = -170
set_y = -120



for turtle in turtles:
    turtle.shape("turtle")
    turtle.penup()
    turtle.shapesize(2)

    chosen_color = random.choice(turtle_colors)
    turtle.color(chosen_color)
    turtle_colors.remove(chosen_color)


    turtle.setpos(set_x, set_y)
    set_y += 65


user_bet = my_scr.textinput('Make a bet', 'Who do you think will be the winner?')

possible_steps = [1,2,3,4,5,6,7]
go_on= True
while go_on:
    for turtle in turtles:
        turtle.fd(random.choice(possible_steps))
        if turtle.xcor() >= 130:
            go_on = False
            print(f"The {turtle.color()[0]} turtle has won!!")
            break

            

if user_bet== turtle.color()[0]:
    print("***You were absolutely correct!! CONGRATULATIONS***")

else:
    print("Better luck next time...")

my_scr.exitonclick()
    




