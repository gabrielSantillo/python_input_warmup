thoughts = []


def thoughts_function():
    selection = input("What is your thought?\n")
    thoughts.append(selection)
    return thoughts


def print_thoughts():
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
    elif(selection == "2"):
        print_thoughts()
    else:
        print("Goodbye.")
        return



while True:
    selection_function()
