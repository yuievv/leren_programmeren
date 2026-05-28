import functions


def get_number(prompt):
    while True:
        invoer = input(prompt)
        try:
            return float(invoer)
        except ValueError:
            print("Geen getal, probeer opnieuw.")


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
        n2 = get_number("Voer het tweede getal in: ")

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
    print("Wat wilt u doen?")
    print("A) getallen optellen")
    print("B) getallen aftrekken")
    print("C) getallen vermenigvuldigen")
    print("D) getallen delen")
    print("E) getal ophogen")
    print("F) getal verlagen")
    print("G) getal verdubbelen")
    print("H) getal halveren")
    while True:
        choice = input("Uw keuze: ").strip().lower()
        if choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            return choice
        print("Ongeldige keuze, probeer opnieuw.")


def ask_next_choice(uitkomst):
    uitkomst_str = str(int(uitkomst)) if uitkomst == int(uitkomst) else str(uitkomst)
    print(f"\nWil je wat met de uitkomst ({uitkomst_str}) doen?")
    print("A) iets optellen")
    print("B) iets aftrekken")
    print("C) met iets vermenigvuldigen")
    print("D) ergens door delen")
    print("E) ophogen")
    print("F) verlagen")
    print("G) verdubbelen")
    print("H) halveren")
    print("I) niets")
    while True:
        choice = input("Uw keuze: ").strip().lower()
        if choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'):
            return choice
        print("Ongeldige keuze, probeer opnieuw.")


# Stap 1: eerste keuze
choice = ask_first_choice()

# Stap 2: eerste getal opvragen
n1 = get_number("Voer het eerste getal in: ")

# Stap 3: berekening uitvoeren
uitkomst = verwerk_keuze(choice, n1)

# Stap 4: volgende berekeningen
while True:
    choice = ask_next_choice(uitkomst)

    if choice == 'i':
        print("Tot ziens!")
        break

    # Gebruik uitkomst als n1, vraag alleen n2 indien nodig
    uitkomst = verwerk_keuze(choice, uitkomst)