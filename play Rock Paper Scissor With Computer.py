print(" \n \n \n \n \n\n")

print("WELCOME TO THE ROCK , PAPER OR SCISSOR GAME")
print('''
      
 _______
-'   ____)
      (_____)                     
      (_____)
      (____)
---.__(___)

      
 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
       
      
_______
--'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
          
         ''')








rock = ('''


 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

paper= ('''
   _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        ''')
        

scissor= ('''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
          
          ''')






user_input = input("Choose rock , paper or scissor! \n" ).lower()  
print(f"So you chose: \n {user_input.upper()}")



 #randomization of computer
import random
set= [rock, paper,scissor]
random_action_of_comp= random.choice(set)
print(f"Computer chose: {random_action_of_comp}")


#conditions and rules:
if (user_input== 'rock' and random_action_of_comp== paper) or \
      (user_input == 'paper' and random_action_of_comp== scissor) or \
    (user_input== 'scissor' and random_action_of_comp== rock):
     print("YOU LOSE!!! Try again!")

elif (user_input== 'rock' and  random_action_of_comp == rock ) or \
      (user_input == 'paper' and random_action_of_comp== paper) or \
    (user_input== 'scissor' and random_action_of_comp== scissor):
     print("Its a Draw")

else:
     print("You win! ")


     print("CONGRATS")

#bye statement
print("THANKYOU for playing ."
"Come back again to play")