import random
print("Number guessing game...")
print(''' Rules:
 1. You will be given 5 hints.
 2. You have to guess and type it after the last hint.
 3. Read the hints thoroughly.
''')

user_input= input("Type your name.")
print(f"Welcome {user_input}")

list1= [1,2,3,4,5,6,7,8,9,10]

number= random.choice(list1)
print("The number has been chosen")
if 1<= number <= 10:
    print("HINT1 \n")
    print("Number lies between 1 and 10.")

to_continue= input("to continue type y for yes and n for no \n").lower()
if to_continue== 'y':
   print("THE GAME CONTINUES")

elif to_continue== 'n':
   print("GAME OVER. You lost")

else:
   print('Invalid input. /////ERROR/////')


#hints

if number%2 ==0 :
    print("HINT2 \n")
    print("Number is not odd and is even.")

if number%2 != 0:
    print("HINT2")
    print("Number is not even and is odd.")



to_continue= input("to continue type y for yes and n for no \n").lower()
if to_continue== 'y':
   print("THE GAME CONTINUES")

elif to_continue== 'n':
   print("GAME OVER. You lost")

else:
   print('Invalid input. /////ERROR/////')


if number - 2 >= 5:
   print("Number minus two >= 5")

elif number - 2 <= 5:
   print("Number minus two <= 5")

to_continue= input("to continue type y for yes and n for no \n").lower()
if to_continue== 'y':
   print("THE GAME CONTINUES")

elif to_continue== 'n':
   print("GAME OVER. You lost")

else:
   print('Invalid input. /////ERROR/////')


if number *2 <= 10:
   print("Number's twice is <= 10. ")

if number *2 >= 10:
   print("Number's twice is >= 10. ")

to_continue2= input("type y to type your guessed number and n to dicontinue the game.")


if to_continue2 == 'y':
   print("Game continues")
   user_number= int(input("Type your number here: \n"))

   if user_number == number:
         print("You are correct! \n CONGRATSS")

   elif user_number != number:
         print("You are not correct! \n Please try again. ")

   else: 
         print("Invalid input ... ERROR")



elif to_continue2 == 'n':
   print("Game disontinues")















