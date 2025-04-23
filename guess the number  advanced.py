#logic of game
import random
user_need_to_guess = random.choice(list(range(1,101)))
user_input1= input("Choose your difficulty level: \"easy\", \"moderate\", \"hard\" ---> ").lower()
def myf(user_input1):
    if user_input1== 'easy':
        i= 10
    elif user_input1== 'moderate':
        i=7
    elif user_input1== 'hard':
        i=5
    else:
        print("PLEASE CHECK YOUR INPUT AGAIN")
        print("**Error**")
    game_not_over = True
    while game_not_over :
        
            print("-"*50)
            if i >0:   
                print(f"You have {i} attempts.")
                user_actual_guess = int(input("Your guess: "))
            if i== 0 :
                print("Booo! You lost.\n*Try again*")
                game_not_over= False
            
            elif user_actual_guess > user_need_to_guess and game_not_over :
                print("TOO HIGH")
                if i>1:
                    print("*Try again*")
            elif user_actual_guess < user_need_to_guess and game_not_over :
                print("TOO LOW")
                if i>1:
                    print("*Try again*")

            elif user_actual_guess == user_need_to_guess and game_not_over :
                print("Yayy! You guessed it right!")
                print("Thanks for playing the game.")
                game_not_over= False
            
            
            else:
                print("Was that a number??")
                print("If not then please *try again*")
            i-=1
                
myf(user_input1)
