#!/usr/bin/python
import random

# function for printing dict output in a box
def box_print(x):
    width = 50
    blank_line = "#" + " "*(width - 2) + "#"
    title = "#" + "TODAY'S OFFERINGS".center(width - 2) + "#"
    print("\n")
    print("#"*width)
    print(blank_line)
    print(title)
    print(blank_line)
    
    longest_key = max(daily_offering.keys(), key=len)

    for k, v in daily_offering.items():
        standard_entry = "#   " + f"{k}" +" "*10 + f"{v}"
        shorter_entry = "#   " + f"{k}" +" "*10 + " "*(len(longest_key) - len(k)) +f"{v}"
        standard_closer = " "*(width - len(standard_entry) - 1) + "#"
        shorter_closer = " "*(width - len(shorter_entry) - 1) + "#"
        if k == longest_key:
            print(standard_entry + standard_closer)
        else:
            print(shorter_entry + shorter_closer)
    print(blank_line)
    print("#"*width)



preparations = {"canned", "boiled", "preserved", "fermented", "powdered", "gluten-free", "dehydrated", "spiced", "pickled", "frozen", "salted", "reconstituted", "gelatinated"}
foods = {"olives", "bananas", "meat", "fish", "bird eggs", "pasta", "broth", "onions", "berries", "shellfish", "cheese", "cow's milk", "squash"}
goods = set()
prices = set()

# Create a random combination of provided elements each time the program is run
while len(preparations) > 5:                                #Not all elements are used each time for variety
    goods.add(preparations.pop() + " " + foods.pop())
while len(prices) < len(goods):
    prices.add(str(random.randint(10, 50)) + " credits")     #Generate some prices
daily_offering = dict(zip(goods,prices))                    #Associate goods with prices


def welcome():
    welcome_txt = " Welcome to the Food Replicator! "
    print("\n")
    print("#"*50)
    print(welcome_txt.center(50, "#"))
    print("#"*50)

welcome()
box_print(daily_offering)

# print("\nAll food from the Food Replicator is free.\
#     \nHowever, we do offer pricing emulation to simulate a scarcity-era 'shopping' experience.")

