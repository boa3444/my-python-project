from turtle import Turtle, Screen

john_the_don = Turtle()
my_scr = Screen()
#triangle

sides_tri = 3
while sides_tri>0:
    john_the_don.color("red")
    john_the_don.forward(100)
    john_the_don.left(120)
    sides_tri-=1

#square
sides = 4
while sides>0 :
    john_the_don.color("orange")
    john_the_don.forward(100)
    john_the_don.left(90)
    sides -=1

#pentagon
sides_pent = 5
while sides_pent >0:
    john_the_don.color("brown")
    john_the_don.forward(100)
    john_the_don.left(72)
    sides_pent-=1

#hexagon
sides_hexa = 6
while sides_hexa >0:
    john_the_don.color("yellow")
    john_the_don.forward(100)
    john_the_don.left(60)
    
    sides_hexa-=1

#heptagon
sides_hepta = 7
while sides_hepta >0:
    john_the_don.color("purple")
    john_the_don.forward(100)
    john_the_don.left(51.4)
    sides_hepta-=1

#octagon
sides_octa = 8
while sides_octa >0:
    john_the_don.color("magenta")
    john_the_don.forward(100)
    john_the_don.left(45)
    sides_octa-=1

#nonagon
sides_nona = 9
while sides_nona>0:
    john_the_don.color("blue")
    john_the_don.forward(100)
    john_the_don.left(40)
    sides_nona-=1

#decagon
sides_deca = 10
while sides_deca >0:
    john_the_don.color("green")
    john_the_don.forward(100)
    john_the_don.left(36)
    sides_deca-=1
my_scr.exitonclick()


