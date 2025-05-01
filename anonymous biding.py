# logic of code
bid_dict = {}
def bid_f():
    user_name= input("Type your name:\n").lower()
    user_bid = int(input("Type your bid in dollars:\n$"))
    bid_dict.update({user_name: user_bid})
    
bid_f()

moreover= input("If there are any other bidders, type'y' for yes and 'n' for no.\n").lower()

while moreover== 'y':
    print("\n" * 1000)
    bid_f()
    moreover= input("If there are any other bidders, type'y' for yes and 'n' for no.\n")

bid_list = list(bid_dict.values())
bid_list.sort(reverse= True)
winner_bid_amount= str(bid_list[0])
for each_key in bid_dict:
    key= 0
    if winner_bid_amount == bid_dict[key]:
        key += key
        we_get = key


        print(f"The winner is {we_get} and the bidding amount is {winner_bid_amount}")




    
  



    