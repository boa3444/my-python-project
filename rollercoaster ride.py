height= int(input("Tell me your height-- "))
if height>=120:
    print("You can go in the ride")
    age= int(input("Whats your age? "))
    if age <= 12:
        print("Pay $5")
        bill = 5
    elif age<=18:
        print("Pay $7")
        bill = 7
    else:
        print("Pay $12")
        bill = 12
    photo= input("Do your want a photo? type 'y' for yes and 'n' for no.  ")
    if photo.lower() == "y":
        bill+= 3
        print(f"Your total bill is ${bill}")
    elif photo.lower() == "n":
        print("No photo. Okay thanks")

else:
    print("You cant")
