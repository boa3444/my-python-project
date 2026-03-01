def add(num1, num2):
    """returns the addition of two nums"""

    return num1+ num2

def multiply(num1, num2):
    """returns the multiplication of two nums"""

    return num1 * num2

def divide(num1, num2):
    """returns the division of two nums"""

    return num1/ num2

def subtraction(num1, num2):
    """returns the addition of two nums"""

    return num1 -num2

wanna_continue= "y"
reference = {
    '+' : add,
    '-' : subtraction,
    '/': divide,
    '*' : multiply
}

while True:
    num1 = float(input("Type num1:"))
    num2= float(input("Type num2:"))

    operation = input("What mode of operation? (* , + , - , /):")
    if num2== 0 and operation== '/':
        print("Incompetent number 2 and operation for your division...")

    for symbol in reference:
        if symbol == operation:
            result = reference[symbol](num1 , num2)
            print(f"{num1} {operation} {num2} = {result}")

        

    wanna_continue = input("Another calculation? (y/n): ").lower()


    if wanna_continue=="n":
        print("Power off...")
        break


