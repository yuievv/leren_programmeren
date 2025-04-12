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
            else:
                return aantal
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw.")

def bereken_prijs(aantal, prijs):
    return aantal * prijs

def print_bon(small_aantal, medium_aantal, large_aantal):
    print("************** Kassa Bon **************")
    print(f"Pizza's small: {small_aantal} x {SMALL_PRIJS:.2f} = {bereken_prijs(small_aantal, SMALL_PRIJS):.2f}")
    print(f"Pizza's medium: {medium_aantal} x {MEDIUM_PRIJS:.2f} = {bereken_prijs(medium_aantal, MEDIUM_PRIJS):.2f}")
    print(f"Pizza's large: {large_aantal} x {LARGE_PRIJS:.2f} = {bereken_prijs(large_aantal, LARGE_PRIJS):.2f}")
    print("---------------------------------------")
    print(f"Totaalprijs: {bereken_prijs(small_aantal, SMALL_PRIJS) + bereken_prijs(medium_aantal, MEDIUM_PRIJS) + bereken_prijs(large_aantal, LARGE_PRIJS):.2f}")

def main():
    small_aantal = vraag_aantal_pizza("small")
    medium_aantal = vraag_aantal_pizza("medium")
    large_aantal = vraag_aantal_pizza("large")
    print_bon(small_aantal, medium_aantal, large_aantal)

main()