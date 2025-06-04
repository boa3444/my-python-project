from turtle import *
import colorgram
import random
colormode(255)
colors = colorgram.extract(r'c:\Users\HP\Downloads\darkcolorpalette.jpg',24)
john_the_don = Turtle()
john_the_don.teleport(-350,-300)

john_the_don.speed(0)
my_scr = Screen()
immutable_colors = []
for item in colors:
        
            r = item.rgb.r
            g= item.rgb.g
            b= item.rgb.b
        
            immutable_colors.append((r,g,b))


for dot_count in range(1,301):
        

        # john_the_don.hideturtle()
        john_the_don.dot(20,random.choice(immutable_colors))
        john_the_don.penup()
        john_the_don.fd(40)
        if dot_count %12==0:
            john_the_don.setheading(90)
            john_the_don.fd(40) 
            john_the_don.setheading(180)
            john_the_don.fd(480)
            john_the_don.setheading(0)
            


my_scr.exitonclick()

