total_bill = float(input("Total bill: $"))

tip= float(input(f"How much percent of ${round(total_bill)} would you like to give? "))
people= float ( input ( "People splitting the bill: "))

tip_to_pay = total_bill * ( tip/100);

all_should_pay = tip_to_pay + total_bill;

print(f"Each should pay: ${round(all_should_pay/people, 2)}")