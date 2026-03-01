import  random

rsp = ["rock", "paper","scissors"]
user_score=0
terminal_score=0
condition_met= False

wanna_play = input("You wanna play?(y/n)").upper()
if ( wanna_play == "N"):
    print("Alright\n")
    exit()

while (wanna_play== "Y"):

    while not condition_met:
        user_chose = input("Type rock , paper or scissors:").lower()

        if user_chose not in rsp:
            print("WTF you inputted\n")
            user_chose = input("Type rock , paper or scissors:").lower()

        terminal_chose = random.choice(rsp)

        print(f"User chose :{user_chose}\nTerminal chose {terminal_chose}")
            
        if ( user_chose == terminal_chose):
            print("Draw\n")
            print(f"User score:{user_score}\nTerminal score:{terminal_score}")
            print("*****************")

        elif ( user_chose== rsp[0] and terminal_chose == rsp[1]):
            terminal_score +=1
            print("You lose")
            print(f"User score:{user_score}\nTerminal score:{terminal_score}")
            print("*****************")

        elif ( user_chose== rsp[1] and terminal_chose == rsp[2]):
            terminal_score +=1
            print("You lose")
            print(f"User score:{user_score}\nTerminal score:{terminal_score}")
            print("*****************")

        elif ( user_chose== rsp[2] and terminal_chose == rsp[0]):
            terminal_score +=1
            print("You lose")
            print(f"User score:{user_score}\nTerminal score:{terminal_score}")
            print("*****************")

        else:
            user_score += 1
            print("You won")
            print(f"User score:{user_score}\nTerminal score:{terminal_score}")
            print("*****************")

        if user_score == 3 or terminal_score ==3:
            condition_met= True
            print(f"Game's over with scores:\nUSER:{user_score}\nTERMINAL:{terminal_score}")
    
    wanna_play=input("You wanna continue playing?(y/n)").upper()

    if ( wanna_play == "N"):
        print("Alright\n")
        exit()
