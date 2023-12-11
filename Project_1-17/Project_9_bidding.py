from pic_art import bid_hammer
print(bid_hammer)

dict1 = {}
ask = True
while ask:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    dict1[name] = bid
    ask = input("Are there any other bidders? Type 'yes' or 'no': ")
    print(100*"\n")
    if ask == 'no':
        highest_bid = 0
        for key in dict1:
            if dict1[key] > highest_bid:
                highest_bid = dict1[key]
                max_key = key
        print(f"The winner is {max_key} with a bid of ${highest_bid}")
        ask = False



'''#there is no clear option or function to clear 
the console during runtime after each input'''