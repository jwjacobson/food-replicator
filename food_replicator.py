#!/usr/bin/python
import random

# function for printing dict output in a box
def box_print(x):
    max_length = 0
    for k, v, in daily_offering.items():
        entry_length = len(k) + len(v) + 9
        if entry_length > max_length:
            max_length = entry_length
    blank_line = "#" + " "*(max_length - 2) + "#"
    title = "#   TODAY'S OFFERING"
    print("\n")
    print("#"*max_length)
    print(blank_line)
    print(title + " "*(max_length - len(title) - 1) + "#")
    print(blank_line)
    for k, v in daily_offering.items():
        entry_length = len(k) + len(v) + 9
        if entry_length == max_length:
            print(f"#   {k} - {v} #")
        else:
            print(f"#   {k} - {v} " + " "*(max_length - entry_length) + "#")
    print(blank_line)
    print("#"*max_length)


preparations = {"canned", "boiled", "preserved", "fermented", "steamed", "gluten-free", "dried", "spiced", "fried", "frozen", "salted", "reconstituted", "vanilla-flavored"}
foods = {"olives", "bananas", "meat", "fish", "eggs", "pasta", "broth", "onions", "berries", "shellfish", "cheese", "cow's milk", "squash"}
goods = set()
prices = set()

# Create a random combination of provided elements each time the program is run
while len(preparations) > 3:                                #Not all elements are used each time for variety
    goods.add(preparations.pop() + " " + foods.pop())
while len(prices) < len(goods):
    prices.add(str(random.randint(2, 30)) + " credits")     #Generate some prices
daily_offering = dict(zip(goods,prices))                    #Associate goods with prices

box_print(daily_offering)


# print("\n")
# print("#"*50)
# print("######## Welcome to the Food Replicator! #########")
# print("#"*50)

# print("\nAll food from the Food Replicator is free.\
#     \nHowever, we do offer pricing emulation to simulate a scarcity-era 'shopping' experience.")

