import random

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


# box_print(numbered_offering)

print(numbered_offering.get(1))