import json

with open("/home/divyanshee/Documents/python_practice/coffee_machine_data.json", 'r') as file:
    coffee_machine_data = json.load(file)

with open("/home/divyanshee/Documents/python_practice/coffee_flavours.json", 'r') as file:
    coffee_flavours_info = json.load(file)

with open("/home/divyanshee/Documents/python_practice/american_money.json", 'r') as file:
    american_money_dict = json.load(file)




def report_abt_machine():
    for key in coffee_machine_data:
        print(f"{key}: {coffee_machine_data[key]}")

condition_satisfied = False
machine_on = True

while machine_on:

    user_input = input("espresso, latte or cappuccino? ").lower()

    if user_input == "off":
        machine_on = False
        continue

    elif user_input =="report":
        report_abt_machine()
        continue

    #making sure the asked flavour is present or not
    else:
        if user_input in coffee_flavours_info:
            condition_satisfied = True

        if not condition_satisfied:
            print("WTF you just entered")
            continue



    for ingredient in coffee_machine_data:
        if ingredient == "cups" or ingredient == "money in pit":
            continue

        if coffee_flavours_info[user_input]["materials"][ingredient] > coffee_machine_data[ingredient]:
            print(f"Not sufficient {ingredient} for your {user_input}\nRestock needed")
            condition_satisfied = False
            break

    if not condition_satisfied :
        continue  #Back to asking for user_input_again

    u_penny = float(input("Penny:")) * 0.01
    u_nickel = float(input("Nickel:")) * 0.05
    u_dime = float(input("Dime:")) * 0.1
    u_quarter= float(input("Quarter:")) * 0.25



    u_total_money = u_quarter+u_dime+u_nickel+u_penny

    required_money = coffee_flavours_info[user_input]['materials']['money']

    print('\n'*5)

    # print(type(required_money))
    if required_money > u_total_money:
        print(f"Not enough money for {user_input}...")
        condition_satisfied= False

    elif required_money <= u_total_money:
        print(f"Here's your change: ${u_total_money-required_money}")
        coffee_machine_data["money in pit"] += required_money

    if not condition_satisfied:
        continue
    else:

        print(f"And here's your {user_input}.. Enjoy!")
        print("\n"*5)
        coffee_machine_data["cups"] -= 1
        for ingredient in coffee_machine_data:
            if ingredient == "cups" or ingredient == "money in pit":
                continue

            coffee_machine_data[ingredient] -= coffee_flavours_info[user_input]["materials"][ingredient]  

