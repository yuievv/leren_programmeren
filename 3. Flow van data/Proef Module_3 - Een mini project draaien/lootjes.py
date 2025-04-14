import random

def lootjes_trekken(namen):
    while True:
        lootjes = namen[:]
        random.shuffle(lootjes)
        
        if all(namen[i] != lootjes[i] for i in range(len(namen))):
            return dict(zip(namen, lootjes))

print("Welkom bij het geheime lootjesprogramma!")

namen = []
while True:
    naam = input("Voer een naam in: ")
    
    if naam in namen:
        print("Deze naam is al toegevoegd. Probeer een andere naam.")
    else:
        namen.append(naam)
    
    if len(namen) >= 3:
        keuze = input("Wil je nog een naam toevoegen? (ja/nee): ").strip().lower()
        if keuze == "nee":
            break

verdeling = lootjes_trekken(namen)
print("\nDe lootjes zijn verdeeld! Je kunt nu opvragen wie je hebt getrokken.")

while True:
    opvraag = input("Voer je naam in om te zien wie je hebt getrokken (of typ 'stop' om te stoppen): ")
    if opvraag.lower() == "stop":
        break
    elif opvraag in verdeling:
        print(f"{opvraag}, jij hebt {verdeling[opvraag]} getrokken.")
    else:
        print("Deze naam zit niet in de lijst. Probeer opnieuw.")

print("\nEinde programma.")
