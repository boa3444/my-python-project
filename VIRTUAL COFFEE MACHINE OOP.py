print("WELCOME TO THE VIRTUAL COFFEE MACHINE THAT IS DESIGNED THROUGH OOP.")
#logic of machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
main_menu = Menu()
coffee_machine = CoffeeMaker()
user_wants = input(main_menu.get_items())
drink= main_menu.find_drink(user_wants)
# print(drink.cost)
if drink and coffee_machine.is_resource_sufficient(drink):
    if money_machine.make_payment(drink.cost):
        coffee_machine.make_coffee(drink)

elif user_wants== 'report':
    coffee_machine.report()

else:
    print("Please enter some valid input.")
    