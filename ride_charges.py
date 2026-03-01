height= float(input("Height(cm): "))

# if (height > 120 ):
#     print("You can ride\n")
#     age = int(input("Age: "))
#     if (age > 18 ):
#         print("Pay $12")
#     elif ( age <= 18):
#         print("Pay $7")

# else:
#     print("Cant ride")

#&& like in c is invalid in python , in python we have and keyword
if ( height > 120):
    print("You can ride")

    age = int(input("Age: "))
    if ( age > 18):
        print("Pay $12")

    elif ( age <= 18):
        print("Pay $7")

elif ( height <= 120):
    print("Cant ride\n")
