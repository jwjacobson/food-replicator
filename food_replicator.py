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

# Welcome message - no animation
def welcome():
    welcome_line1 = " Welcome to the Food Repository "
    welcome_line2 = "   Item Retrieval Interface!   "
    blank_line = " "*32
    print("\n")
    print("#"*50)
    print("#"*50)
    print(blank_line.center(50, "#"))
    print(welcome_line1.center(50, "#"))
    print(welcome_line2.center(50, "#"))
    print(blank_line.center(50, "#"))
    print("#"*50)
    print("#"*50)

# Welcome message - with animation
def welcome2():
    welcome_txt = " Welcome to the Food Repository! "
    print("\n")
    sprint("#"*50 + "\n")
    sprint("#"*50 + "\n")
    sprint(welcome_txt.center(50, "#") + "\n")
    sprint("#"*50 + "\n")
    sprint("#"*50 + "\n")

# function for printing dict output in a box - no animation
def box_print(x):
    width = 58
    blank_line = "#" + " "*(width - 2) + "#"
    title = "#" + "AVAILABLE TODAY".center(width - 2) + "#"
    print("\n")
    print("#"*width)
    print(blank_line)
    print(title)
    print(blank_line)
    
    longest_key = max(daily_offering.keys(), key=len)

    counter = 1
    for k, v in daily_offering.items():
        standard_entry = f"#    {counter}. {k}" +" "*10 + f"{v} credits"
        shorter_entry = f"#    {counter}. {k}" +" "*10 + " "*(len(longest_key) - len(k)) +f"{v} credits"
        standard_closer = " "*(width - len(standard_entry) - 1) + "#"
        shorter_closer = " "*(width - len(shorter_entry) - 1) + "#"
        if k == longest_key:
            print(standard_entry + standard_closer)
            counter += 1
        else:
            print(shorter_entry + shorter_closer)
            counter += 1
    print(blank_line)
    print("#"*width)

# function for printing dict output in a box - with animation 
def box_print2(x):
    width = 50
    blank_line = "#" + " "*(width - 2) + "#"
    title = "#" + "AVAILABLE TODAY".center(width - 2) + "#"
    sprint("\n")
    sprint("#"*width + "\n")
    print(blank_line)
    sprint(title + "\n")
    print(blank_line)
    
    longest_key = max(daily_offering.keys(), key=len)

    for k, v in daily_offering.items():
        standard_entry = "#   " + f"{k}" +" "*10 + f"{v}"
        shorter_entry = "#   " + f"{k}" +" "*10 + " "*(len(longest_key) - len(k)) +f"{v}"
        standard_closer = " "*(width - len(standard_entry) - 1) + "credits #"
        shorter_closer = " "*(width - len(shorter_entry) - 1) + " credits #"
        if k == longest_key:
            sprint(standard_entry + standard_closer + "\n")
        else:
            sprint(shorter_entry + shorter_closer + "\n")
    print(blank_line)
    sprint("#"*width + "\n")

def interactive():
    user_input = True
    while user_input:
        box_print(numbered_offering)
        balance()
        if credits < min(prices):
            print("You cannot afford anything else.")
            break
        prompt = input("Enter 1-9 to order or Q to quit ")
        if prompt.isdigit() == False and prompt.lower() != "q" or prompt == "0":
            print("Invalid input.")
        elif prompt.lower() == "q":
            user_input = False
        else:
            prompt = int(prompt)
            foodprice = numbered_offering.get(prompt)
            print(f"{foodprice[0].capitalize()} costs {foodprice[1]} credits.")
            if credits < foodprice[1]:
                print(f"Insufficient credits ({credits}).")
            else:
                approval = input("Order? (y/n) ")
                if approval.lower() == "y":
                    order.append(foodprice[0])
                    print(f"{foodprice[0].capitalize()} ordered.")
                    credits -= foodprice[1]
                    print(f"{foodprice[1]} credits deducted.")
                    total += foodprice[1]
                elif approval.lower() == "n":
                    user_input == True

def balance():
    print(f"You have {credits} credits.")
    
# Declare initial variables
preparations = {"canned", "boiled", "preserved", "fermented", "powdered", "gluten-free", "dehydrated", "pickled", "frozen", "salted", "reconstituted", "gelatinated", "irradiated", "salvaged", "cloned", "mutant"}
foods = {"lichen", "bananas", "hog jowl", "fish", "bird eggs", "pasta", "broth", "onions", "berries", "shellfish", "cheese", "cow's milk", "squash", "yeast protein", "tree bark", "slime", "rat"}
goods = set()
prices = set()
credits = 100
order = []
total = 0

# Create a random combination of elements each time the program is run
while len(preparations) > 8:                                #Not all elements are used each time for variety
    goods.add(preparations.pop() + " " + foods.pop())
while len(prices) < len(goods):
    prices.add((random.randint(10, 50)))     #Generate some prices
daily_offering = dict(zip(goods,prices))                    #Associate goods with prices
numbers = list(range(1, 10))
numbered_offering = dict(zip(numbers,daily_offering.items()))
print(numbered_offering)

welcome()

print("Orders input here will be retrieved from the warehouse,\
    \nand credits will be automatically deducted from your account.")

print(order)
print(total)
