import random

print("Welkom bij het lootjes programma!")

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

while True:
    lootjes = namen[:]
    random.shuffle(lootjes)  

    geldig = True
    for i in range(len(namen)):
        if namen[i] == lootjes[i]:
            geldig = False
            break

    if geldig:
        break  

print("\nDe lootjesverdeling is:")
for i in range(len(namen)):
    print(f"{namen[i]} heeft getrokken: {lootjes[i]}")

print("\nEinde programma.")
