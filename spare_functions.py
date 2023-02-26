
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

