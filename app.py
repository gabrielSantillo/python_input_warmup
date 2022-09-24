thoughts = []


def thoughts_function():
    selection = input("What is your thought?\n")
    thoughts.append(selection)
    return thoughts


def print_thoughts():
    if (len(thoughts) == 0):
        print("You don't have any thoughts yet.")
    else:
        for thought in thoughts:
            print(thought)


def selection_function():
    print("--------------------------------------------------------")
    print("\n1. Type your thoughts")
    print("2. See your thoughts")
    print("3. Finish typing thoughts\n")
    selection = input("Chose between 1, 2 or 3:\n")

    if (selection == "1"):
        thoughts_function()
    elif (selection == "2"):
        print_thoughts()
    elif (selection == "3"):
        print("Goodbye.")
        return False
    else:
        print("You should have typed only numbers between 1, 2 or 3. Please try again.")
        selection_function()

    return True

call_thoughts_function = selection_function()

while call_thoughts_function:
    continue_thoughts_function = selection_function()
    if not continue_thoughts_function:
        break