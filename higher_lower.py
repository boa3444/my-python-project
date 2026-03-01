import random

data_dict= {
    "Apple": 120000000,   # in USD
    "Google": 95000000,
    "Microsoft": 110000000,
    "Amazon": 130000000,
    "Tesla": 80000000
}


higher = ''
score= 0
break_point = False
names = list(data_dict.keys())


while not break_point:
    opt1 = random.choice(names)
    names.remove(opt1)
    opt2= random.choice(names)

    print(f"Compare A : {opt1}")
    print(f"With B: {opt2}")
    if data_dict[opt1] < data_dict[opt2]:
        higher = opt2
    elif  data_dict[opt1] > data_dict[opt2]:
        higher = opt1

    answer = input("Monthly income of B is 'higher' or 'lower' than A? ").lower()

    print("\n"*100)
    if answer == 'lower' and higher != opt2:
        score += 1
        print("You got it right!!")

    elif answer == 'higher' and higher == opt2:
        score += 1
        print("You got it right!!")

    else:
        break_point = True
        print("You couldn't get it right!!")


    print(f"Score : {score}")
    names.append(opt1)