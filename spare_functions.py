# These are alternate versions of functions that I didn't end up using in the final program.
# Welcome message - no animation
def welcome():
    welcome_line1 = " Welcome to the Food Repository "
    welcome_line2 = "   Item Retrieval Interface!    "
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
    print("\nYour order will be retrieved from the warehouse,\
    \nand credits automatically deducted from your account.")

# Summarize the order - no animation
def order_summary():
    width = 40
    blank_line = "#" + " "*(width - 2) + "#"
    title = "#" + "ORDER SUMMARY".center(width - 2) + "#"
    print("\n")
    print("#"*width)
    print(blank_line)
    print(title)
    print(blank_line)
    print("#" + "You bought:".center(width - 2) + "#")
    print(blank_line)
    if order:
        order_set = set()
        for item in order:
            if order.count(item) == 1:
                order_set.add(f"1 unit of {item}")
            elif order.count(item) == 2:
                order_set.add(f"2 units of {item}")
            else:
                oder_set.add(f"Several units of {item}")
        for item in order_set:
            print("#" + f"{item}".center(width - 2) + "#")
    else:
        print("#" + "Nothing".center(width - 2) + "#")
    print(blank_line)
    print("#" + f"You spent {total} credits.".center(width - 2) + "#")
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
