import random

def kamer_1():
    print("Je staat voor de ingang van de verlaten Tempel der Verloren Zielen.")
    print("Een koude wind giert langs je gezicht als je de donkere doorgang betreedt.")
    input("Druk op enter om verder te gaan...")

def kamer_2():
    print("\nJe komt in een ronde kamer met een groot standbeeld in het midden.")
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    op = random.choice(['+', '-', '*'])
    
    som = f"{num1} {op} {num2}"
    print(f"Op het standbeeld staat: {som}")
    
    antwoord = int(input("Wat is het antwoord? "))
    
    if op == '+':
        correct = num1 + num2
    elif op == '-':
        correct = num1 - num2
    else:
        correct = num1 * num2
    
    if antwoord == correct:
        print("\nHet standbeeld geeft je een gouden sleutel!")
        has_key = True
    else:
        print("\nHet standbeeld negeert je...")
        has_key = False
    
    print("\nEr zijn twee uitgangen: links en rechts")
    keuze = input("Welke kant kies je? (links/rechts): ").lower()
    
    if keuze == "links":
        return has_key, "kamer6"
    else:
        return has_key, "kamer3"

def voer_gevecht_uit(speler, vijand, vijand_naam):
    print(f"\nEen {vijand_naam} valt je aan!")
    
    vijand_schade = max(1, vijand['attack'] - speler['defence'])
    speler_schade = max(1, speler['attack'] - vijand['defence'])
    
    vijand_hits = (speler['health'] + vijand_schade - 1) // vijand_schade
    speler_hits = (vijand['health'] + speler_schade - 1) // speler_schade
    
    if speler_hits < vijand_hits:
        print(f"\nJe verslaat de {vijand_naam}!")
        speler['health'] -= speler_hits * vijand_schade
        print(f"Je hebt nu {speler['health']} health over.")
        return True
    else:
        print(f"\nDe {vijand_naam} was te sterk...")
        return False

def kamer_6():
    zombie = {
        'health': 30,
        'attack': random.randint(3, 8),
        'defence': 2
    }
    
    speler = {
        'health': 50,
        'attack': 5,
        'defence': 3
    }
    
    if voer_gevecht_uit(speler, zombie, "zombie"):
        return "kamer3"
    return None

def kamer_3():
    item = random.choice(['schild', 'zwaard'])
    
    if item == 'schild':
        print("\nJe vindt een glanzend schild tegen de muur.")
        return {'defence': 1}, "kamer4"
    else:
        print("\nEen scherp zwaard steekt in een steen.")
        return {'attack': 2}, "kamer4"

def kamer_4():
    bewaker = {
        'health': 3,
        'attack': 2,
        'defence': 0
    }
    
    speler = {
        'health': 50,
        'attack': 5,
        'defence': 3
    }
    
    if voer_gevecht_uit(speler, bewaker, "tempelbewaker"):
        return "kamer5"
    return None

def kamer_5(has_key):
    if has_key:
        print("\nJe opent de schatkist en vindt de legendarische schat!")
        print("*** GEFELICITEERD! Je hebt gewonnen! ***")
    else:
        print("\nZonder sleutel kun je de schatkist niet openen...")
        print("*** GAME OVER ***")

def main():
    kamer_1()
    
    has_key, volgende_kamer = kamer_2()
    
    while volgende_kamer:
        if volgende_kamer == "kamer6":
            volgende_kamer = kamer_6()
        elif volgende_kamer == "kamer3":
            stats, volgende_kamer = kamer_3()
        elif volgende_kamer == "kamer4":
            volgende_kamer = kamer_4()
        elif volgende_kamer == "kamer5":
            kamer_5(has_key)
            break

if __name__ == "__main__":
    main()