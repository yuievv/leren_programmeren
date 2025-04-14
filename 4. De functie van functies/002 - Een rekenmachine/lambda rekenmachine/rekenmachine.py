from functions import addition, subtraction, multiplication, division

def main():
    first_round = True
    result = None
    
    while True:
        if first_round:
            menu = """Wat wilt u doen?
A) getallen optellen
B) getallen aftrekken
C) getallen vermenigvuldigen
D) getallen delen
E) getal ophogen
F) getal verlagen
G) getal verdubbelen
H) getal halveren
Kies: """
        else:
            menu = f"""Wat wilt u doen met de uitkomst ({result})?
A) iets optellen
B) iets aftrekken
C) iets vermenigvuldigen
D) door iets delen
E) ophogen
F) verlagen
G) verdubbelen
H) halveren
I) niets
Kies: """
        
        choice = input(menu).lower()
        
        if not first_round and choice == 'i':
            print("Einde berekening")
            break
        
        if choice not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            print("Ongeldige keuze, probeer opnieuw")
            continue
        
        if first_round or result is None:
            n1 = float(input("Welk getal? " if first_round else f"Wat is het volgende getal bij {result}? "))
        else:
            n1 = result
        
        if choice in ['e', 'f']:
            n2 = 1
        elif choice in ['g', 'h']:
            n2 = 2
        else:
            n2 = float(input(f"Welk getal {'optellen bij' if choice == 'a' else 'aftrekken van' if choice == 'b' else 'vermenigvuldigen met' if choice == 'c' else 'delen door'} {n1}? "))
        
        operation = {
            'a': addition,
            'b': subtraction,
            'c': multiplication,
            'd': division,
            'e': addition,
            'f': subtraction,
            'g': multiplication,
            'h': division
        }[choice]
        
        new_result = operation(n1, n2)
        
        if new_result is not None:
            operator = {
                'a': '+',
                'b': '-',
                'c': 'x',
                'd': ':',
                'e': '+',
                'f': '-',
                'g': 'x',
                'h': ':'
            }[choice]
            
            print(f"{n1} {operator} {n2} = {new_result}")
            print("-" * 50)
            result = new_result
        
        first_round = False

if __name__ == "__main__":
    main()