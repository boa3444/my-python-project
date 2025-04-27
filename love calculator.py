def calculate_love_score(name1, name2):
    total_times_each_letter1  = 0
    for x in 'true':
        times = 0
        if x in name1 :
            times += name1.count(x)
            
        if x in name2:
            times+= name2.count(x)
        
        
            
        total_times_each_letter1 += times
    
    
    total_times_each_letter2  = 0
    for x in 'love':
        times = 0

        if x in name1 :
            times+= name1.count(x)
            
            
        if x in name2:
            times+= name2.count(x)
            
        total_times_each_letter2 += (times)
            
        
    total_times_all_letter = str(total_times_each_letter1) + str(total_times_each_letter2)
    print(f"Your love precentage is : \n {total_times_all_letter}")
            
name1= input("Type first name\n")
name2 = input('Type second name\n')
calculate_love_score(name1, name2)
