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
        return True
    else:
        print("\nHet standbeeld negeert je...")
        return False

def voer_gevecht_uit(speler, vijand, vijand_naam):
    print(f"\nEen {vijand_naam} valt je aan!")
    
    # Bereken schade per hit
    vijand_schade = max(1, vijand['attack'] - speler['defence'])
    speler_schade = max(1, speler['attack'] - vijand['defence'])
    
    # Bereken benodigde hits
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
    
    return voer_gevecht_uit(speler, zombie, "zombie")

def kamer_3():
    item = random.choice(['schild', 'zwaard'])
    
    if item == 'schild':
        print("\nJe vindt een glanzend schild tegen de muur.")
        return {'defence': 1}
    else:
        print("\nEen scherp zwaard steekt in een steen.")
        return {'attack': 2}

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
    
    return voer_gevecht_uit(speler, bewaker, "tempelbewaker")

def kamer_5(has_key):
    if has_key:
        print("\nJe opent de schatkist en vindt de legendarische schat!")
    else:
        print("\nZonder sleutel kun je de schatkist niet openen...")

def main():
    kamer_1()
    
    has_key = kamer_2()
    
    if not kamer_6():
        print("Game over - De zombie was te sterk!")
        return
    
    stats = kamer_3()
    print(stats)
    
    if not kamer_4():
        print("Game over - De tempelbewaker versloeg je!")
        return
    
    kamer_5(has_key)

if __name__ == "__main__":
    main()