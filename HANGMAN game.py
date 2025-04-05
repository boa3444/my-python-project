#decorations
print("Welcome to the HANGMAN GAME")
from hangman_list import logo
print(logo)
print("Rules:\n" \
"1. Guess the correct letters fitting in the given number of blanks\n" \
"2. You have 6 lives\n" \
"3. Each incorrect guess equals one death")
user_input2= input("Click y to start and n to escape.").lower()
for f in user_input2:
    if user_input2== 'y':
        print("***************************************************************************************************************************************************************************************")
        continue
    elif user_input2== 'n':
        break
    else:
        print("**Invalid input**")




#logic of game
import random
from hangman_list import word_list
from hangman_list import stages
user_has_to_guess= random.choice(word_list)
show_the_user = ''
for x in user_has_to_guess:
    show_the_user += '_'

print(f"You have to guess the forbidden word : {show_the_user}")


#To-do: make sure if the letter guessed is correct then print that letter and if not then '_'


lives= 6
correct_letters= []   
game_over = False
while not game_over and lives >= 0:  
    display = '' 
    user_input1 = input("Guess a letter: ").lower()
    for x in user_has_to_guess:
        if user_input1== x:
            display += x
            correct_letters.append(x)
            
        elif x in correct_letters:
            display+= x
        else:
            display+= '_'
    if user_input1 in user_has_to_guess:
        print("You managed to escape your death.")
        print(f"Live count: {lives}")
    if user_input1 not in user_has_to_guess:
        lives -=1
        print("Incorrect guess!!")
        print(f"--------Live count: {lives}---------")

    if '_' in display and lives == 0 :
        game_over= True
        print(f"--------Live count: {lives}---------")
        print(stages[lives])
        print("-------YOU LOST THE GAME--------")
        print("*****Try Again*****")
        break

        
        
    elif not '_' in display:
        print("**************** Yeaahhh!! You won the HANGMAN game ******************")
        print("---------------CONGRATS-----------------")
    
    print(display)
    
    print(stages[lives])
    print("***************************************************************************************************************************************************************************************")
    





    

