print("WELCOME TO THE BLACKJACK GAME")
user_name = input("Type your name here ---> ").title()
print(f"Hello there, {user_name}!.")
user_input= input("PRESS ENTER TO CONTINUE THE GAME... ")
print("\n"*1000)


import random

user_money = int(input("Type the money you want to spend in this round : $"))
money= [100, 120, 200, 340, 500, 150,1000,1300,300,1200,450]


computer_money= random.choice(money)
print(f"Computer spends ${computer_money}")
user_next_round= input("PRESS ENTER TO CONTINUE TO THE NEXT ROUND... ")

possibles = [1,2,3,4,5,6,7,8,9,10,7,8,9,10,7,8,9,10,7,8,9,10,7,8,9,10]
user_cards_list = []
global user_score 
user_score = 0
global computer_score 
computer_score = 0
computer_cards_list = []

    
    
game_over = True
i=0
while game_over and i<=5:
    print("\n"*1000)
    unumber = random.choice(possibles)
    cnumber = random.choice(possibles)
    user_cards_list.append(unumber)
    user_score += unumber
    computer_cards_list.append(cnumber)
    computer_score += cnumber
    print(f"Your cards : {user_cards_list}      \t\t ||| \t\t Computer's first card is : {computer_cards_list[0]}")
    print(f"Your current total score: {user_score} \t\t ||| \t\t Computer's current total score : Unknown")
    
    
    
    #print(computer_score)
    user_input2= input("Do you wanna continue the blackjack game?.Type 'y' or 'n' ---> ").lower()
    if user_input2=='n' :
        game_over= False
        

        print(f"Your final score: {user_score} \t\t ||| \t\t Computer's final score : {computer_score}")
    
    else:
            i+=1
        
if user_score > 21 and computer_score <= 21:
            print("***YOU LOST THE GAME***")
            print(f"Computer won total ${user_money + computer_money}")

elif user_score<= 21 and computer_score>21:
            print("***YOU WON THE GAME.***")
            print(f"You just won ${user_money + computer_money}")
elif user_score<21 and computer_score<21 and user_score> computer_score:
        print("***YOU WON THE GAME.***")
        print(f"You just won ${user_money + computer_money}")
elif user_score<21 and computer_score<21 and user_score< computer_score:
        print("***YOU LOST THE GAME***")
        print(f"Computer won total ${user_money + computer_money}")

elif user_score>21 and computer_score>21 and user_score< computer_score:
        print("***YOU WON THE GAME.***")
        print(f"You just won ${user_money + computer_money}")
elif user_score>21 and computer_score>21 and user_score> computer_score:
        print("***YOU LOST THE GAME***")
        print(f"Computer won total ${user_money + computer_money}")

elif user_score == computer_score:
        print("It's a DRAW")
        print("**Try again**")
else:
        print("An ERROR has occured.")
        print("Please try again.")




            
    


    
    
    
    
    
    