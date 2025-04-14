import random

def speel_ronde():
    geheim_getal = random.randint(1, 1000)
    aantal_beurten = 0
    print("\nEen nieuw getal is gekozen! Probeer het te raden.")

    while aantal_beurten < 10:
        try:
            gok = int(input(f"Beurt {aantal_beurten + 1}/10 - Doe een gok: "))
        except ValueError:
            print("Ongeldige invoer! Voer een getal in.")
            continue

        verschil = abs(geheim_getal - gok)

        if verschil < 20:
            print("Je bent heel warm!")
        elif verschil < 50:
            print("Je bent warm!")

        if gok == geheim_getal:
            print("Gefeliciteerd, je hebt het juiste getal geraden!")
            return True  
        elif gok < geheim_getal:
            print("Het geheime getal is hoger.")
        else:
            print("Het geheime getal is lager.")

        aantal_beurten += 1

    print(f"Helaas, je hebt het geheime getal ({geheim_getal}) niet geraden.")
    return False  

score = 0
max_ronden = 20

for ronde in range(1, max_ronden + 1):
    print(f"\n--- Ronde {ronde} ---")
    if speel_ronde():
        score += 1
    print(f"Score tot nu toe: {score}")

    if ronde < max_ronden:
        verder_spelen = input("Wil je nog een ronde spelen? (ja/nee): ").strip().lower()
        if verder_spelen != "ja":
            break

print(f"\nHet spel is afgelopen. Je eindscore is: {score}")
