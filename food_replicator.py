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
    welcome_line2 = "      Retrieval Interface!      "
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
    print(len(welcome_line1))

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
        standard_entry = f"#    {counter}. {k}" +" "*10 + f"{v}"
        shorter_entry = f"#    {counter}. {k}" +" "*10 + " "*(len(longest_key) - len(k)) +f"{v}"
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
        standard_closer = " "*(width - len(standard_entry) - 1) + "#"
        shorter_closer = " "*(width - len(shorter_entry) - 1) + "#"
        if k == longest_key:
            sprint(standard_entry + standard_closer + "\n")
        else:
            sprint(shorter_entry + shorter_closer + "\n")
    print(blank_line)
    sprint("#"*width + "\n")

# Declare initial variables
preparations = {"canned", "boiled", "preserved", "fermented", "powdered", "gluten-free", "dehydrated", "spiced", "pickled", "frozen", "salted", "reconstituted", "gelatinated", "irradiated"}
foods = {"olives", "bananas", "meat", "fish", "bird eggs", "pasta", "broth", "onions", "berries", "shellfish", "cheese", "cow's milk", "squash", "yeast protein"}
goods = set()
prices = set()
credits = 100

# Create a random combination of elements each time the program is run
while len(preparations) > 5:                                #Not all elements are used each time for variety
    goods.add(preparations.pop() + " " + foods.pop())
while len(prices) < len(goods):
    prices.add(str(random.randint(10, 50)) + " credits")     #Generate some prices
daily_offering = dict(zip(goods,prices))                    #Associate goods with prices
numbers = list(range(1, 9))
numbered_offering = dict(zip(numbers,daily_offering.items()))
print(numbered_offering)

welcome()

print("Orders input here will be retrieved from the warehouse,\
    \nand credits will be automatically deducted from your account.")

print(f"You have {credits} credits.")

user_input = True
while user_input:
    prompt = input("\nWould you like to (V) view available foods or (Q) quit? ")
    if prompt.lower() == "v":
        box_print(numbered_offering)
        while user_input:    
            prompt = input("\nWould you like to (O) order a food or (Q) quit? ")
            if prompt.lower() == "o":
                choice = input("Which food will you order? ")
                if int(choice) in numbered_offering.keys():
                    print("Success")
                else:
                    print("Invalid input.")
            elif prompt.lower() == "q":
                user_input = False
            else:
                print("Invalid input.")
    elif prompt.lower() == "q":
        user_input = False
    else:
        print("Invalid input.")
