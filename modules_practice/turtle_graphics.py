import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

my_screen.bgcolor("pink")
my_turtle.color("red")
my_turtle.shape("turtle")
my_turtle.fd(1000)

print(my_screen.canvheight)

# print(my_screen.getcanvas())
my_screen.exitonclick()