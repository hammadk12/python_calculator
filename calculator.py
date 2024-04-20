def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def addition():
    x = get_number("What's x? ")
    y = get_number("What's y? ")
    print(round(x + y, 2))

def subtraction():
    x = get_number("What's x? ")
    y = get_number("What's y? ")
    print(round(x - y, 2))

def multiplication():
    x = get_number("What's x? ")
    y = get_number("What's y? ")
    print(round(x * y, 2))

def division():
    x = get_number("What's x? ")
    y = get_number("What's y? ")
    print(round(x/y, 2))


def main():
    while True:
        print("\nWelcome to the Python Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        try:
            userInput = int(input("Choose your operation. Type the number choice only: "))
        except ValueError:
            print("Please enter a valid option.")
            continue

        if userInput == 1:
            addition()        
        elif userInput == 2:
            subtraction()
        elif userInput == 3:
            multiplication()
        elif userInput == 4:
            division()
        elif userInput == 5:
            break
main()