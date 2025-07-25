import smtplib
import datetime as dt
import random

my_email = 'newone1804@gmail.com'
password= 'siaubbwcclxhahdg'

quote_list = []


with open(r"C:\Users\newon\Downloads\Birthday Wisher (Day 32) start\quotes.txt") as quotes:
    # print('yes')
    for line in quotes:
        quote_list.append(line)

    final_quote = random.choice(quote_list)
    now= dt.datetime.now()
    weekday = now.weekday()
    # print(weekday)
    if weekday == 0:
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user = my_email, password= password )
        connection.sendmail(to_addrs= 'divyanshe@yahoo.com', from_addr= my_email, msg= f'Subject:QUOTE OF THE DAY\n\n{final_quote}')
