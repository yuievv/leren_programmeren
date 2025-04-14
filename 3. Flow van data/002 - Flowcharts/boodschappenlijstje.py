boodschappenlijst = {}

while True:
    artikel = input("Welk artikel wilt u toevoegen? ").strip().lower().capitalize()

    while True:
        try:
            hoeveelheid = int(input(f"Hoeveel {artikel} wilt u toevoegen? "))
            break
        except ValueError:
            print("Voer een geldig aantal in (een heel getal).")

    if artikel in boodschappenlijst:
        boodschappenlijst[artikel] += hoeveelheid
    else:
        boodschappenlijst[artikel] = hoeveelheid

    meer_boodschappen = input("Wilt u nog meer boodschappen toevoegen? (ja/nee): ").strip().lower()
    if meer_boodschappen != 'ja':
        break

print("\n-[Boodschappenlijst]-")
for artikel, hoeveelheid in boodschappenlijst.items():
    print(f"{hoeveelheid}x {artikel}")
print("-----------------------")
