import random


letters=[chr(i) for i in range(ord('a'), ord('z') + 1)]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
           '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|']

pass_random = [letters, digits,symbols]
condition_satisfied = False

u_letter = int (input("Letters:"))
u_digits = int ( input("Numbers:"))
u_symbols = int (input ("Symbols:"))

characters_in_pass = u_digits+u_letter+u_symbols

l_count=0
d_count=0
s_count=0

pass_list = []

if u_digits == 0:
    pass_random.remove(digits)
elif u_letter==0:
    pass_random.remove(letters)

elif u_symbols==0:
    pass_random.remove(symbols)

    
while characters_in_pass > 0:

    random_chose_list = random.choice(pass_random)
    random_chose = random.choice(random_chose_list)
    # print(f"Random chose : {random_chose}")
    pass_list.append(random_chose)
    # print(pass_list)
    
    if random_chose in letters:
        l_count +=1

    elif random_chose in digits:
        d_count += 1

    elif random_chose in symbols:
        s_count+=1

    characters_in_pass -= 1


    
print(*pass_list)