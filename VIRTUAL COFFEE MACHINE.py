#decoration of machine
print("""
██╗   ██╗██╗██████╗ ████████╗██╗   ██╗ █████╗ ██╗              ██████╗ ██████╗ ███████╗███████╗███████╗███████╗        ███████╗██╗  ██╗ ██████╗ ██████╗ 
██║   ██║██║██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║             ██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝        ██╔════╝██║  ██║██╔═══██╗██╔══██╗
██║   ██║██║██████╔╝   ██║   ██║   ██║███████║██║             ██║     ██║   ██║█████╗  █████╗  █████╗  █████╗          ███████╗███████║██║   ██║██████╔╝
╚██╗ ██╔╝██║██╔══██╗   ██║   ██║   ██║██╔══██║██║             ██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝          ╚════██║██╔══██║██║   ██║██╔═══╝ 
 ╚████╔╝ ██║██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗        ╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗        ███████║██║  ██║╚██████╔╝██║     
  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝         ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝        ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                                                                                        
""")
print("Welcome to Divyanshi's personal virtual coffee shop ☕🥞🍪!")
#logic of machine
from menu_of_virtual_coffee_machine import MENU
from menu_of_virtual_coffee_machine import resources

def hot_flavors():
    for k in MENU:
        print(f"☕{k}")
print("🍩Which hot coffee flavour would you like?🍩")
hot_flavors()
user_input = input("~")
money=0
while user_input:
    if user_input== 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    elif user_input== 'off':
        break
    else:   
        if user_input== "latte":
            if  MENU["latte"]["ingredients"]["water"]> resources["water"] :
                print("Sorry ,currently we do not have sufficient water...")
                print("Which coffee would you like?")
                hot_flavors()
                user_input= input("~~")
            
            elif MENU["latte"]["ingredients"]["milk"]> resources["milk"] :
                print("Sorry ,currently we do not have sufficient milk...")
                print("Which coffee would you like?")
                hot_flavors()
                
                user_input= input("~~")
            
            elif MENU["latte"]["ingredients"]["coffee"]> resources["coffee"] :
                print("Sorry ,currently we do not have sufficient coffee...")
                print("Which coffee would you like?")
                hot_flavors()
                user_input= input("~~")
        if user_input== "espresso":
            if MENU["espresso"]["ingredients"]["water"]> resources["water"] :
                print("Sorry ,currently we do not have sufficient water...")
                print("Which coffee would you like?")
                hot_flavors()
                
                user_input= input("~~")
        
            elif MENU["espresso"]["ingredients"]["coffee"]> resources["coffee"] :
                print("Sorry ,currently we do not have sufficient coffee...")
                print("Which coffee would you like?")
                hot_flavors()
                
                user_input= input("~~")
        
        if user_input== "cappuccino":
            if  MENU["cappuccino"]["ingredients"]["water"]> resources["water"] :
                print("Sorry ,currently we do not have sufficient water...")
                print("Which coffee would you like?")
                hot_flavors()
                
                user_input= input("~~")
        
            elif MENU["cappuccino"]["ingredients"]["milk"]> resources["milk"] :
                print("Sorry ,currently we do not have sufficient milk...")
                print("Which coffee would you like?")
                hot_flavors()
                user_input= input("~~")
            elif MENU["cappuccino"]["ingredients"]["coffee"]> resources["coffee"] :
                print("Sorry ,currently we do not have sufficient coffee...")
                print("Which coffee would you like?")
                hot_flavors()
                
                user_input= input("~~")

        user_coins_penny=0.01* float(input("Insert only coins .\nPenny: "))
        user_coins_dime= 0.10*float(input("Dime: "))
        user_coins_nickel= 0.05*float(input("Nickel: "))
        user_coins_quarter= 0.25*float(input("Quarter: "))
        sum_coins = user_coins_penny+ user_coins_dime + user_coins_nickel+ user_coins_quarter
        money+= sum_coins
        
        if user_input== "espresso":
            if sum_coins > MENU["espresso"]["cost"]:
                    change = sum_coins- MENU["espresso"]["cost"]
                    print(f"~ your ${change} change.")
            if sum_coins < MENU["espresso"]["cost"]:
                    print(f"SORRY BUT THAT WASN'T SUFFICIENT MONEY FOR YOUR {user_input}\nRefunding the inserted money now...")
            if sum_coins == MENU["espresso"]["cost"]:
                    print("Your money was sufficient. No change to give you.")
        if user_input== "latte":
            if sum_coins > MENU["latte"]["cost"]:
                    change = sum_coins- MENU["latte"]["cost"]
                    print(f"~ your ${change} change.")
            if sum_coins < MENU["latte"]["cost"]:
                    print(f"SORRY BUT THAT WASN'T SUFFICIENT MONEY FOR YOUR {user_input}\nRefunding the inserted money now...")
            if sum_coins == MENU["latte"]["cost"]:
                    print("Your money was sufficient. No change to give you.")
        if user_input== "cappuccino":
            if sum_coins > MENU["cappuccino"]["cost"]:
                    change = sum_coins- MENU["espresso"]["cost"]
                    print(f"~ your ${change} change.")
            if sum_coins < MENU["cappuccino"]["cost"]:
                    print(f"SORRY BUT THAT WASN'T SUFFICIENT MONEY FOR YOUR {user_input}\nRefunding the inserted money now...")
            if sum_coins == MENU["cappuccino"]["cost"]:
                    print("Your money was sufficient. No change to give you.")
            

#
    if user_input== 'espresso': 
        if MENU["espresso"]["ingredients"]["water"]< resources["water"] and MENU["espresso"]["ingredients"]["coffee"]< resources["coffee"] :
            print(f"Here is your {user_input}😀☕! Enjoy the day")
        elif MENU["espresso"]["ingredients"]["water"]== resources["water"]  or MENU["espresso"]["ingredients"]["coffee"]== resources["coffee"]  :
            print(f"Here is your {user_input}😀☕! Enjoy the day")
        
        
        
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        
    if user_input== "latte":
        if MENU["latte"]["ingredients"]["water"]< resources["water"] and  MENU["latte"]["ingredients"]["milk"]< resources["milk"] and MENU["latte"]["ingredients"]["coffee"]< resources["coffee"]:
            print(f"Here is your {user_input}😀☕! Enjoy the day")
        elif  MENU["latte"]["ingredients"]["milk"]== resources["milk"] or MENU["latte"]["ingredients"]["water"]== resources["water"] or  MENU["latte"]["ingredients"]["coffee"]== resources["coffee"]:
            print(f"Here is your {user_input}😀☕! Enjoy your day")
        
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        
        
        
    if user_input== "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"]< resources["water"] and  MENU["cappuccino"]["ingredients"]["milk"]< resources["milk"] and MENU["cappuccino"]["ingredients"]["coffee"]< resources["coffee"]:
            print(f"Here is your {user_input}😀☕! Enjoy the day")
        elif  MENU["cappuccino"]["ingredients"]["water"]== resources["water"] or MENU["cappuccino"]["ingredients"]["coffee"]== resources["coffee"] or  MENU["cappuccino"]["ingredients"]["milk"]== resources["milk"]:
            print(f"Here is your {user_input}😀☕! Enjoy your day")
        
       
            
        
        
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        
        
        

    
       
    print("🍩🥤Which hot coffee flavour would you like?🥤🍩")
    hot_flavors()
    user_input = input("~")
