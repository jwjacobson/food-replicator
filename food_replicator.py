#!/usr/bin/python
import random
import time
import sys

# character-by-character printing for analog effect.
# source: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line 
def sprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

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

def box_print2(x):
    width = 50
    blank_line = "#" + " "*(width - 2) + "#"
    title = "#" + "TODAY'S OFFERINGS".center(width - 2) + "#"
    sprint("\n")
    sprint("#"*width + "\n")
    print(blank_line)
    sprint(title + "\n")
    print(blank_line)
    
    longest_key = max(daily_offering.keys(), key=len)

    for k, v in daily_offering.items():
        standard_entry = "#   " + f"{k}" +" "*10 + f"{v}"
        shorter_entry = "#   " + f"{k}" +" "*10 + " "*(len(longest_key) - len(k)) +f"{v}"
        standard_closer = " "*(width - len(standard_entry) - 1) + "#"
        shorter_closer = " "*(width - len(shorter_entry) - 1) + "#"
        if k == longest_key:
            sprint(standard_entry + standard_closer + "\n")
        else:
            sprint(shorter_entry + shorter_closer + "\n")
    print(blank_line)
    sprint("#"*width + "\n")




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
    sprint("#"*50 + "\n")
    sprint("#"*50 + "\n")
    sprint(welcome_txt.center(50, "#") + "\n")
    sprint("#"*50 + "\n")
    sprint("#"*50 + "\n")


def welcome2():
    welcome_txt = " Welcome to the Food Replicator! "
    print("\n")
    sprint("#"*50 + "\n")
    sprint("#"*50 + "\n")
    sprint(welcome_txt.center(50, "#") + "\n")
    sprint("#"*50 + "\n")
    sprint("#"*50 + "\n")

welcome()
box_print2(daily_offering)

# print("\nAll food from the Food Replicator is free.\
#     \nHowever, we do offer pricing emulation to simulate a scarcity-era 'shopping' experience.")

