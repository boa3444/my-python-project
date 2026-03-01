# drawn cards are reusable

import random

MIN = 16
MIN_FOR_ACE = 10 # for it to turn 11
MAX=21
cards = [2,3,4,5,6,7,8,9,10,10,10, "ace"] # one or eleven for ace
fortune = ["hit" , "stand"]

def closer_to_MAX(num1 , num2):

    if num1 == MAX and num2 != MAX:
        return num1

    if num2 == MAX and num1 != MAX:
        return num2
    
    if num1 == num2 and num1 == MAX:
        return 0
    
    if num1 < MAX and num2 < MAX :
        if num1 < num2:
            return num2
        else:
            return num1
        
    elif num1 > MAX  and num2 > MAX:
        if num1 < num2:
            return num1
        else:
            return num2
        
    elif num1 > MAX and num2 < MAX:
        return num2
    else:
        return num1


#for computer
comp_cards = []
comp_cards_total_sum = 0

while comp_cards_total_sum < MAX:

    rand_card = random.choice(cards)
    if rand_card== "ace" and comp_cards_total_sum > MIN_FOR_ACE : #and comp_cards_total_sum< MAX:
       
        rand_card  = 1
        print(rand_card)

    elif rand_card == "ace" and comp_cards_total_sum <= MIN_FOR_ACE: #and comp_cards_total_sum< MAX:
        rand_card = 11
        print(rand_card)

    comp_cards.append(rand_card)
    comp_cards_total_sum = sum(comp_cards)

    # tactics to win

    if comp_cards_total_sum > 18:
        break

# print(comp_cards)


#for user
wanna_play = "y"

while wanna_play == "y":
    wanna_play = input("You wanna start the game? (y/n): ").lower()
    user_cards = []
    user_cards_total_sum = 0
    hit = "y"

    if wanna_play == "n":
        print("Sayonara...")
        exit()

    while hit == "y":

        rand_card_user = random.choice(cards)

        if rand_card_user == "ace" and user_cards_total_sum <= MIN_FOR_ACE:
            rand_card_user = 11

        elif rand_card_user == "ace" and user_cards_total_sum > MIN_FOR_ACE:
            rand_card_user = 1

        user_cards.append(rand_card_user)
        user_cards_total_sum = sum(user_cards)
        print("\n"*100)
        print(f"Your cards:{user_cards}")
        print(f"Computer cards : [{comp_cards[0]}, ?]")
        hit = input("You wanna draw another card again? (y/n): ").lower()
    

    print("\n" * 100)
    print(f"Your final cards : {user_cards}")
    print(f"Computer's final cards: {comp_cards}")

    winner = ""
    loser = ""
    winners_total = closer_to_MAX(user_cards_total_sum , comp_cards_total_sum)
    
    if winners_total == 0 :
        print("Its a DRAW!!")
        winner = "Nobody"
        losers_total = winners_total
        loser = "Nobody"
    elif comp_cards_total_sum == winners_total:
        winner = "Computer"
        loser = "You"
        losers_total = user_cards_total_sum
        print("You lost...")

    elif user_cards_total_sum == winners_total:
        winner = "You"
        loser = "Computer"
        losers_total = comp_cards_total_sum
        print("You won!!")

    print(f"{winner} won here with a total of {closer_to_MAX(user_cards_total_sum , comp_cards_total_sum)} while {loser} lost with a total of {losers_total}")

    wanna_play = input("You wanna play again? (y/n): ").lower()

    if wanna_play == "n":
        print("Sayonara...")
