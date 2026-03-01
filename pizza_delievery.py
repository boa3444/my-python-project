size= input("Size of pizza ( S , L , M): ").upper()

pepperoni = input("You want pepperonni in it? (y/n): ").upper()

extra_cheese = input("You want extra cheese?(y/n): ").upper()

total_bill = 0

if ( size == "S"):
    total_bill += 15
    if ( pepperoni == "Y"):
        total_bill += 2

    if ( extra_cheese == "Y"):
        total_bill += 1
    
    print(f"Total bill : {total_bill}")
    exit()

elif ( size == "M"):
    total_bill+= 20


elif ( size == "L"):
    total_bill+= 25

else:
    print("Type a valid size of pizza.")
    exit()


if ( pepperoni == "Y"):
    total_bill += 3

if ( extra_cheese == "Y"):
    total_bill += 1

print(f"Total bill : {total_bill}")
