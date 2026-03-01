height = float(input("Your height(cm): "))
print(height)
if ( height <= 120):
    print("Cant ride")
    exit()

elif ( height > 120):
    print("Can ride")
    
age = int (input("Your age: "))

want_pic= input("Want photos?").upper()

bill = 0


if (age <12):
    bill += 5

elif ( age >=12 and age <18):
    bill+= 7

elif ( age >= 18 and age <45):
    bill += 12

elif(age >= 45 and age <=55):
    bill += 0


if ( want_pic == "Y"):
    bill += 3
    print(f"Bill : {bill}")
elif (want_pic == "N"):
    print(f"Bill : {bill}")
