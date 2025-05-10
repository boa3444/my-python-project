from turtle import Turtle ,Screen
user_input= int(input("how many rounds you want it to take?"))
tom = Turtle()

def myf():
    for x in range(user_input):
        print(f"Loop iteration: {x}")
        tom.circle(50)
        

        
        

tom.shapesize(3)
tom.shape('turtle')
tom.color('magenta')
myscr = Screen()
myscr.bgcolor("pink")

myf()
myscr.exitonclick()

