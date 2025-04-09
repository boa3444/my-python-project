def is_leap_year(year):
    '''
    if year is a leap year or not
    '''
     #docstring
    if year%4==0:
        if year %100==0:
            if year%400==0:
                return True
            elif year%400!=0:
                return False
        
        elif year %100!=0:
            return True
        
    elif year%4!=0:
        return False
    
    else:
        return 'invalid input'
user_input= (int(input("Type the year that you wanna check if its a leap year or not\n")))
print(f"The fact that your typed year is a leap year is: \n{is_leap_year(user_input)}")
        