print("Welkom bij het spel 'Wie is het'!")

# Vraag 1: Is de kaas geel?
geel_kaas = input("Is de kaas geel? (ja/nee): ")
if geel_kaas.lower() == "ja":
    # Vraag 2: Zitten er gaten in?
    gaten_kaas = input("Zitten er gaten in? (ja/nee): ")
    if gaten_kaas.lower() == "ja":
        # Vraag 3: Is de kaas belachelijk duur?
        dure_kaas = input("Is de kaas belachelijk duur? (ja/nee): ")
        if dure_kaas.lower() == "ja":
            print("De kaas is Emmethaler!")
        else:
            print("De kaas is Leerdammer!")
    else:
        # Vraag 3: Is de kaas hard als steen?
        hard_korst = input("Is de kaas hard als steen? (ja/nee): ")
        if hard_korst.lower() == "ja":
            print("De kaas is Parmigiano Riggiano!")
        else:
            print("De kaas is Goudse Kaas!")
else:
    # Vraag 2: Heeft de klas blauwe schimmel?
    schimmel_kaas = input("Heeft de klas blauwe schimmel? (ja/nee): ")
    if schimmel_kaas.lower() == "ja":
        # Vraag 3: Heeft de kaas korst
        franse_kaas = input("Heeft de kaas korst? (ja/nee): ")
        if franse_kaas.lower() == "ja":
            print("Blue de Rochbaron!")
        else:
            print("De kaas is Foume d'ambert!")
    else:
        # Vraag 3: Heeft de kaas korst?
        blauwe_kaas = input("Heeft de kaas korst? (ja/nee): ")
        if blauwe_kaas.lower() == "ja":
            print("De kaas is Camembert!")
        else:
            print("De kaas is Mozzarella!")