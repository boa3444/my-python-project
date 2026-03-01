numbers = [10,203,2,4,3,2,3,4,45,5,1,0,19,118,1992]

max = numbers[0];
for num in numbers:
    if max < num:
        max = num

print(max)