print("Welcome to the tip calculator!")
bill= input("What was the total bill? \n $")
tip = input ("How much tip would you like to give?")
people = input("How many people to split the bill?")
newbill= float(bill)
newtip= float(tip)
newpeople= float(people)
payment= (newbill+newtip)/ newpeople
print(f"So each person should pay: ${payment}")

