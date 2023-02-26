#!/usr/bin/python
import random
import time
import sys
from termcolor import colored, cprint

# character-by-character printing for analog effect.
# source: https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line 
def sprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

# Welcome message - with animation
def welcome2():
    welcome_line1 = " Welcome to the Food Repository "
    welcome_line2 = "   Item Retrieval Interface!    "
    blank_line = " "*32
    print("\n")
    sprint("#"*50 + "\n")
    sprint("#"*50 + "\n")
    sprint(blank_line.center(50, "#") + "\n")
    sprint(welcome_line1.center(50, "#") + "\n")
    sprint(welcome_line2.center(50, "#") + "\n")
    sprint(blank_line.center(50, "#") + "\n")
    sprint("#"*50 + "\n")
    sprint("#"*50 + "\n")
    print("\nYour order will be retrieved from the warehouse,\
    \nand credits automatically deducted from your account.")

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
    width = 58
    blank_line = "#" + " "*(width - 2) + "#"
    title = "#" + "AVAILABLE TODAY".center(width - 2) + "#"
    print("\n")
    sprint("#"*width + "\n")
    print(blank_line)
    sprint(title + "\n")
    print(blank_line)
    
    longest_key = max(daily_offering.keys(), key=len)

    counter = 1
    for k, v in daily_offering.items():
        standard_entry = f"#    {counter}. {k}" +" "*10 + f"{v} credits"
        shorter_entry = f"#    {counter}. {k}" +" "*10 + " "*(len(longest_key) - len(k)) +f"{v} credits"
        standard_closer = " "*(width - len(standard_entry) - 1) + "#"
        shorter_closer = " "*(width - len(shorter_entry) - 1) + "#"
        if k == longest_key:
            sprint(standard_entry + standard_closer + "\n")
            counter += 1
        else:
            sprint(shorter_entry + shorter_closer + "\n")
            counter += 1
    print(blank_line)
    sprint("#"*width + "\n")

def balance():
    print(f"You have {credits} credits.")

def interactive():
    global credits
    global total
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
            print(f"1 unit of {foodprice[0]} costs {foodprice[1]} credits.")
            if credits < foodprice[1]:
                cprint(f"\nInsufficient credits ({credits})", "red", attrs=["bold"])
                print("Choose something else.")
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

# Summarize the order - with animation
def order_summary2():
    width = 40
    blank_line = "#" + " "*(width - 2) + "#"
    title = "#" + "ORDER SUMMARY".center(width - 2) + "#"
    print("\n")
    sprint("#"*width + "\n")
    sprint(blank_line + "\n")
    sprint(title + "\n")
    sprint(blank_line + "\n")
    sprint("#" + "You bought:".center(width - 2) + "#" + "\n")
    sprint(blank_line + "\n")
    if order:
        order_set = set()
        for item in order:
            if order.count(item) == 1:
                order_set.add(f"1 unit of {item}")
            elif order.count(item) == 2:
                order_set.add(f"2 units of {item}")
            else:
                order_set.add(f"Several units of {item}")
        for item in order_set:
            sprint("#" + f"{item}".center(width - 2) + "#" + "\n")
    else:
        print("#" + "Nothing".center(width - 2) + "#" + "\n")
    print(blank_line)
    sprint("#" + f"You spent {total} credits.".center(width - 2) + "#\n")
    print(blank_line)
    print("#"*width)

# Declare initial variables
preparations = {"canned", "boiled", "preserved", "fermented", "powdered", "gluten-free", "dehydrated", "pickled", "frozen", "salted", "reconstituted", "gelatinated", "irradiated", "salvaged", "cloned", "mutant"}
foods = {"lichen", "bananas", "hog jowl", "mudfish", "bird eggs", "pasta", "broth", "onions", "berries", "shellfish", "cheese", "cow's milk", "squash", "yeast protein", "tree bark", "slime", "rat"}
goods = set()
prices = set()
credits = 100
order = []
total = 0

# Create a random combination of elements each time the program is run
while len(preparations) > 8:                                #Not all elements are used each time for variety
    goods.add(preparations.pop() + " " + foods.pop())
while len(prices) < len(goods):
    prices.add((random.randint(10, 50)))                    #Generate some prices
daily_offering = dict(zip(goods,prices))                    #Associate goods with prices
numbers = list(range(1, 10))
numbered_offering = dict(zip(numbers,daily_offering.items()))
print(numbered_offering)




welcome2()
interactive()
order_summary2()