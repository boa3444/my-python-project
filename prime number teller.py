user= int(input("Number: "))
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
 
   
    for i in range(2, num):
        
        if num % i == 0:
            return False
 
   
    return True
print(is_prime(user))
start = True
while start:   
    user_input = input("Wanna continue? ")
    while user_input == 'yes':
        user= int(input("Number: "))
        print(is_prime(user))
        user_input = input("Wanna continue? ")
    else:
        start = False
        print("Thank-you")

    
        
        
    
        
        
