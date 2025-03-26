rock = '''


  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


'''

paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)


'''

scissor= '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


'''
print("PLAY rock , paper and scissors with the computer!!")

#user's input
user_input= input("Choose rock, paper or scissor!!!  ").lower()
if user_input== 'rock':                         
    print(rock)
elif user_input== 'paper':
    print(paper)
elif user_input== 'scissor':
    print(scissor)

print(f"YOU CHOSE: {user_input} " )



#computer plays random
lis= [rock,paper,scissor]
import random
random_action =  random.choice(lis)

print("COMPUTER CHOSE :"    + random_action )


if (user_input== 'paper' and random_action == scissor) or    \
   (user_input== 'scissor' and random_action == rock) or   \
    (user_input=='rock' and random_action== paper):
    print("YOU lose")

elif(user_input== random_action):
    print("Its a draw!!  Try again !!")

else: 
    print("You won!!  Congrats")

