choice = 'y'

while choice == 'y':
    a = int(input("Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\n"))

    if a == 1 or a == 2 or a == 3 or a == 4:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

        if a == 1:
            print(f"Addition of {x} and {y} is {x + y}")
        elif a == 2:
            print(f"Subtraction of {x} and {y} is {x - y}")
        elif a == 3:
            print(f"Multiplication of {x} and {y} is {x * y}")
        elif a == 4:
            if y != 0:
                print(f"Division of {x} and {y} is {x / y}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("The given choice is invalid.")

    choice = input("Enter 'y' to continue or 'n' to quit: ")
