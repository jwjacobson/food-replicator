choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

user_input = True
while user_input:
    prompt = input("Enter 1-9 to order or Q to quit ")
    if prompt.isdigit() == False and prompt.lower() != "q":
        print("Invalid input.")
    elif prompt.lower() == "q":
        user_input = False
    elif int(prompt) in choices:
        print(f"You chose {prompt}")
