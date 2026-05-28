from calculations import CALCULATIONS

def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid number, please try again.")

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

def process_choice(choice, n1):
    if choice in ('e', 'f'):
        n2 = 1.0
    elif choice in ('g', 'h'):
        n2 = 2.0
    else:
        n2 = get_number("Enter the second number: ")

    if choice in ('a', 'e'):
        result = CALCULATIONS['addition'](n1, n2)
    elif choice in ('b', 'f'):
        result = CALCULATIONS['subtraction'](n1, n2)
    elif choice in ('c', 'g'):
        result = CALCULATIONS['multiplication'](n1, n2)
    elif choice in ('d', 'h'):
        result = CALCULATIONS['division'](n1, n2)

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

def ask_next_choice(current_result):
    result_str = str(int(current_result)) if current_result == int(current_result) else str(current_result)
    print(f"\nDo you want to do something with the result ({result_str})?")
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

# Main execution flow
choice = ask_first_choice()
n1 = get_number("Enter the first number: ")
result = process_choice(choice, n1)

while True:
    choice = ask_next_choice(result)
    if choice == 'i':
        print("Goodbye!")
        break
    result = process_choice(choice, result)