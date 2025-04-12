# Voornaam: Klaudia
# Achternaam: Dongen
# Opdracht: Pizza calculator

SMALL_PRIJS = 6.75
MEDIUM_PRIJS = 8.25
LARGE_PRIJS = 10.89

def vraag_aantal_pizza(afmeting):
    while True:
        try:
            aantal = int(input(f"Hoeveel {afmeting} pizza's wilt u? "))
            if aantal < 0:
                print("Aantal moet een positief getal zijn.")
            elif aantal == 0:
                return 0
            else:
                return aantal
        except ValueError:
            print("Dit is geen heel nummer!")

def bereken_prijs(aantal, prijs):
    return aantal * prijs

def print_bon(small_aantal, medium_aantal, large_aantal):
    print("************** Kassa Bon **************")
    totaal = 0
    
    if small_aantal > 0:
        small_prijs = bereken_prijs(small_aantal, SMALL_PRIJS)
        print(f"Pizza's small:\t\t{small_aantal} x {SMALL_PRIJS:.2f} = {small_prijs:.2f}")
        totaal += small_prijs
    
    if medium_aantal > 0:
        medium_prijs = bereken_prijs(medium_aantal, MEDIUM_PRIJS)
        print(f"Pizza's medium:\t\t{medium_aantal} x {MEDIUM_PRIJS:.2f} = {medium_prijs:.2f}")
        totaal += medium_prijs
    
    if large_aantal > 0:
        large_prijs = bereken_prijs(large_aantal, LARGE_PRIJS)
        print(f"Pizza's large:\t\t{large_aantal} x {LARGE_PRIJS:.2f} = {large_prijs:.2f}")
        totaal += large_prijs
    
    print("---------------------------------------")
    print(f"Te betalen:\t\t\t{totaal:.2f}")

def main():
    small_aantal = vraag_aantal_pizza("small")
    medium_aantal = vraag_aantal_pizza("medium")
    large_aantal = vraag_aantal_pizza("large")
    print_bon(small_aantal, medium_aantal, large_aantal)

if __name__ == "__main__":
    main()