#decoration
user_name = input("Type your name here ---> ")
print(f"Welcome to the \"higher lower game\", {user_name}!")
print("Here are the rules:\n\n1. I will present you with information about two different items (e.g., celebrities, countries, etc.)."
      "\n2. Your task is to guess which item has a higher value for a specific statistic (e.g., Instagram followers, population, etc.)."
      "\n3. Type 'higher' if you think the first item has a higher value."
      "\n4. Type 'lower' if you think the second item has a higher value."
      "\n5. After your guess, I will reveal the answer and tell you if you were correct."
      "\n6. The game continues with the winner of the previous round and a new item."
      "\n7. The goal is to get as many correct guesses in a row as possible!\n\nGood luck!")
from higher_lower_gamedata import data
import random
#logic  of  the  game



game_not_over = True
score = 0
while game_not_over:    
    option_a = random.choice(data)
    data.remove(option_a)
    option_b = random.choice(data)
    print(f"Compare A : {option_a['name']} which is a {option_a['description']} , from {option_a['country']}.")
    print(f"With B : {option_b['name']} which is a {option_b['description']} , from {option_b['country']}." )

    answer = ''
    if option_a['follower_count']> option_b['follower_count']:
            answer = 'A'
    elif option_a['follower_count']< option_b['follower_count']:
            answer = 'B'
    else:
            print("Error")
            print("**Try again**")
    
    user_input = input("Choose 'A' or 'B'---> ").upper()
    if user_input== answer:
           score+=1
           print("You got this one right!.")
           print("\n"*10)
           #print("Current score : {score}")
    elif user_input!= answer:
           game_not_over = False
           print("Booo You got this one wrong. Thanks for playing!")
           print(f"Your final score is : {score} ")
           print("*"*90)
           user_continue= input("You wanna play again?. Type 'y' or 'n'.").lower()
           if user_continue== 'y':
                game_not_over= True
            
          
                  
                  
           
    

        
