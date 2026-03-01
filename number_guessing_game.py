import random

rand_num = random.randint(1 , 101)

start =1
end = 100
user_got_it = False

while not user_got_it:

    user_chose = int (input("Guess the num: "))
    if user_chose > rand_num:
        print("Too high")

    elif user_chose < rand_num :
        print("Too low")

    elif user_chose == rand_num:

        print("You got it!!")
        user_got_it = True