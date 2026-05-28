import functions


def get_number(prompt):
    while True:
        invoer = input(prompt)
        try:
            return float(invoer)
        except ValueError:
            print("No number, please try again.")


def format_result(n1, n2, choice, result):
    operators = {
        'a': '+', 'b': '-', 'c': 'x', 'd': ':',
        'e': '+', 'f': '-', 'g': 'x', 'h': ':'
    }
    operator = operators[choice]
    n1_str = str(int(n1)) if n1 == int(n1) else str(n1)
    n2_str = str(int(n2)) if n2 == int(n2) else str(n2)
    result_str = str(int(result)) if result == int(result) else str(result)
    print(f"{n1_str} {operator} {n2_str} = {result_str}")


def verwerk_keuze(choice, n1):
    if choice in ('e', 'f'):
        n2 = 1.0
    elif choice in ('g', 'h'):
        n2 = 2.0
    else:
        n2 = get_number("Enter the second number: ")

    if choice in ('a', 'e'):
        result = functions.addition(n1, n2)
    elif choice in ('b', 'f'):
        result = functions.subtraction(n1, n2)
    elif choice in ('c', 'g'):
        result = functions.multiplication(n1, n2)
    elif choice in ('d', 'h'):
        result = functions.division(n1, n2)

    format_result(n1, n2, choice, result)
    return result


def ask_first_choice():
    print("What would you like to do?")
    print("A) Add numbers")
    print("B) Subtract numbers")
    print("C) Multiply numbers")
    print("D) Divide numbers")
    print("E) Increment number")
    print("F) Decrement number")
    print("G) Double number")
    print("H) Halve number")
    while True:
        choice = input("Your choice: ").strip().lower()
        if choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            return choice
        print("Invalid choice, please try again.")


def ask_next_choice(uitkomst):
    uitkomst_str = str(int(uitkomst)) if uitkomst == int(uitkomst) else str(uitkomst)
    print(f"\nWould you like to do something with the result ({uitkomst_str})?")
    print("A) Add something")
    print("B) Subtract something")
    print("C) Multiply by something")
    print("D) Divide by something")
    print("E) Increment")
    print("F) Decrement")
    print("G) Double")
    print("H) Halve")
    print("I) Nothing")
    while True:
        choice = input("Your choice: ").strip().lower()
        if choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'):
            return choice
        print("Invalid choice, please try again.")


# Step 1: first choice
choice = ask_first_choice()

# Step 2: request the first number
n1 = get_number("Enter the first number: ")

# Step 3: perform the calculation and show the result
uitkomst = verwerk_keuze(choice, n1)

# Step 4: the following calculations
while True:
    choice = ask_next_choice(uitkomst)

    if choice == 'i':
        print("Goodbye!")
        break

    # Use the result as n1; only ask for n2 if necessary
    uitkomst = verwerk_keuze(choice, uitkomst)