print(" Welcome to \"Divyanshi Ka Pizza Hut\" ")
user= input("What size of pizza do you want? ")
if user.upper() == "S":
    bill = 15
    print(f"Your bill is ${bill}")
    pepperoni = input ("Do you want pepperoni? Type Y for yes and N for no")
    if pepperoni.upper() == "Y":
        bill += 2
        print(f"Your total bill is ${bill}")
    elif pepperoni.upper() == "N":
        print( f"Your total bill is {bill}")


elif user.upper()== "M":
    bill = 20
    print(f"Your bill is ${bill}")
    pepperoni = input ("Do you want pepperoni? Type Y for yes and N for no  ")
    if pepperoni.upper() == "Y":
        bill += 3
        print(f" Your total bill is {bill}")

    elif pepperoni.upper() == "N":
        print (f" Your bill is ${bill}")

elif user.upper()== "L":
    bill = 25
    print(f"Your bill is {bill}")
    pepperoni = input ("Do you want pepperoni? Type Y for yes and N for no  ")
    if pepperoni.upper() == "Y":
        bill += 3
        print(f" Your total bill is ${bill}")

    elif pepperoni.upper() == "N":
        print(f" Your bill is ${bill}")


