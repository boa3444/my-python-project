import random

auctions = ["Vase" ,"Cream" , "Pot" , "Horse", "Painting"]
details = {}
wanna_continue = "y"

at_auction = random.choice ( auctions)
print(f"The {at_auction} is at auction this time...Place your name and your bid for {at_auction}.")

while wanna_continue == "y":

    name = input("Input auctioneer's name:")
    bid = int(input("Whats your bid? $"))
    details[name] = bid

    wanna_continue = input("Any other bidder? (y/n): ")
    if wanna_continue == "y":
        print("\n"*100)

    elif wanna_continue== 'n':
        
        max = details[name]
        for bidders in details:
            if max < details[bidders]:

                max = details[bidders]

                highest_bidder = bidders
                highest_bid = max

        print(f"{highest_bidder} won by bidding an amount of ${highest_bid}.")

    else:
        print("Only type y or no")

            

