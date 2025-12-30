


coffee_menu = {
    "espresso": {
        "materials": {
            "milk":0,
            "water": 50,
            "coffee": 18,
            "money" : 1.50
        }
    },
    "latte": {
        "materials": {
            "milk": 200,
            "water":150,
            "coffee": 24,
            "money" : 2.50
        }
    },
    "cappuccino": {
        "materials": {
            "milk":100,
            "water": 250,
            "coffee": 24,
            "money" : 3
        }
    }
}
money_dict= {
            "penny": 0.01,
            "nickel": 0.05,
            "dime": 0.10,
            "quarter": 0.25
    }

coffee_machine_materials={
    "milk" : 500,
    "coffee" : 100,
    "water" :500,
    "cups" : 10,
    "money in pit" : 0    
}


def report():
    for key in coffee_machine_materials:
        print(f"{key}: {coffee_machine_materials[key]}")
          

total_coffee_serves= 0
user_wants  = ""
ingredient_insufficient = False

########
while True:

    user_wants = input("What would you like? (espresso/latte/cappuccino): ").lower()


    if user_wants == "report":
        report()
        continue
        
    elif user_wants == "off":
        print(f"I served {total_coffee_serves} happy cup of coffee today...\nSayonara!")
        break

    if coffee_machine_materials["cups"] == 0:
        print(f"Insufficient cups..\nNeed a restock of cups")
        continue 


    u_penny = float(input("Penny: "))
    u_dime= float(input("Dime: "))
    u_nickel= float(input("Nickel: "))
    u_quarter= float(input("Quarter: "))


    total_money = (u_penny * money_dict["penny"]) +( u_dime * money_dict["dime"])+ (u_nickel * money_dict["nickel"] )+ (u_quarter * money_dict["quarter"])

    req_money = coffee_menu[user_wants]["materials"]["money"]

    # print(req_money)

    if total_money < req_money :
        print(f"Insufficient money for {user_wants}")
        print("Your money will be refunded...")
        continue

    elif total_money >= req_money:
        change =total_money- req_money 
        coffee_machine_materials["money in pit"] += req_money   # money thats required has been given to machine


    #to check the suffiency of ingredients in coffee machine
    for ingredient in coffee_machine_materials:

        if ingredient == "money in pit" or ingredient =="cups":
            continue   # since these two arent in coffee menu materials of coffees

        if coffee_machine_materials[ingredient] < coffee_menu[user_wants]["materials"][ingredient]:
            print(f"Insufficient {ingredient} for your {user_wants}")
            print("Restock needed")
            ingredient_insufficient = True
            break

    if ingredient_insufficient :
        continue
    #Minus the used ingredients in the last coffee
    for ingredient in coffee_machine_materials:
        if ingredient == "money in pit" or ingredient =="cups":
            continue
        coffee_machine_materials[ingredient] -= coffee_menu[user_wants]["materials"][ingredient]

    print("\n"*100)
    print(f"Here's your {user_wants} ☕ and ${round(change,2)}")
    total_coffee_serves += 1
