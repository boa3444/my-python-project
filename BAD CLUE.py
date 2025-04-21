#materials that user has as options to guess
#material of game
from bad_clue_symbols import logo
print(logo)
from bad_clue_symbols import rules
print(rules)
print("*"*155)
user_input1= input("Press enter to continue ")

from bad_clue_symbols import slash
from bad_clue_symbols import cross
from bad_clue_symbols import correct

# / = partially correct
# O= all correct
# X = no correct
import random

seventeen_members = ["Seungcheol", "Jeonghan", "Joshua", "Jun", "Hoshi", "Wonwoo", "Woozi", "Dokyeom", "Mingyu", "Minghao", "Seungkwan", "Vernon", "Dino"]
weapons = ["knife","gun","rock","landmine","plough","rope","bomb","katana","stick", "metal rod"]
murder_places = ["bathroom", "bedroom", "living room", "kitchen", "terrace", "library", "garage"]
print(f"The possible murderers are :\n{seventeen_members}")
print(f"The possible weapons are :\n{weapons}")
print(f"The possible murder places are :\n{murder_places}")
murderer= random.choice(seventeen_members)
weapon= random.choice(weapons)
murder_place= random.choice(murder_places)

user_input1= input("Press enter to continue ")
print("\n"*4)
user_input_of_murderer= input("Enter the murderer that you have guessed: ").title()
user_input_of_weapon= input("Enter the weapon that you have guessed: ").lower()
user_input_of_murder_place= input("Enter the murder place that you have guessed: ").lower()
print(f"Your guess :\n{user_input_of_murderer} killed with a {user_input_of_weapon} in the {user_input_of_murder_place}")



game_over= True
while game_over:
    if user_input_of_murderer== murderer :
        if user_input_of_weapon == weapon:
            if user_input_of_murder_place== murder_place:
                print(correct)
                print(f"Yess!!! {murderer} killed with a {weapon} in the {murder_place}")
                game_over = False

            elif user_input_of_murder_place != murder_place:
                
                print(slash)

        elif user_input_of_weapon!= weapon:
            
            print(slash)

    elif user_input_of_murderer != murderer:
        
        
        if user_input_of_weapon == weapon:
            if user_input_of_murder_place== murder_place:
                print(slash)

            elif user_input_of_murder_place != murder_place:
                
                print(slash)
                

        elif user_input_of_weapon!= weapon:
            
            if user_input_of_murder_place== murder_place:
                print(slash)

            elif user_input_of_murder_place != murder_place:
                
                print(cross)
            
    else:
        print("\tERROR\t")
        print("Make sure you type the names correctly")


    if game_over:
        user_input1= input("Press enter to continue ")
        print("\n"*100)   
        print("***************Next guess time.***************")
        print(f"The possible murderers are :\n{seventeen_members}\n")
        print(f"The possible weapons are :\n{weapons}\n")
        print(f"The possible murder places are :\n{murder_places}\n")
        user_input_of_murderer= input("Enter the murderer that you have guessed: ").title()
        user_input_of_weapon= input("Enter the weapon that you have guessed: ").lower()
        user_input_of_murder_place= input("Enter the murder place that you have guessed: ").lower()
        print(f"Your guess :\n{user_input_of_murderer} killed with a {user_input_of_weapon} in the {user_input_of_murder_place}")

    else:
        print("\t***YAY! You won the legendary BAD CLUE game.***\t")
    

    