import random

def kamer_1():
    print("Je staat voor de ingang van de verlaten Tempel der Verloren Zielen.")
    print("Een koude wind giert langs je gezicht als je de donkere doorgang betreedt.")
    print("De stenen muren zijn bedekt met vreemde symbolen die zachtjes gloeien in het duister.")
    input("Druk op enter om verder te gaan...")

def kamer_2():
    print("\nJe komt in een ronde kamer met een groot standbeeld in het midden.")
    print("Op het standbeeld staat een mysterieuze inscriptie:")
    
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    op = random.choice(['+', '-', '*'])
    
    som = f"{num1} {op} {num2}"
    print(som)
    
    antwoord = int(input("Wat is het antwoord? "))
    
    if op == '+':
        correct = num1 + num2
    elif op == '-':
        correct = num1 - num2
    else:
        correct = num1 * num2
    
    if antwoord == correct:
        print("\nHet standbeeld komt tot leven en fluistert: 'Jij bent waardig...'")
        print("Een gouden sleutel verschijnt in je hand.")
        return True
    else:
        print("\nEen diepe stem echoot: 'Onwaardig...'")
        print("Het standbeeld vervaagt in het duister.")
        return False

def kamer_3():
    item = random.choice(['schild', 'zwaard'])
    
    if item == 'schild':
        print("\nJe vindt een glanzend mythisch schild tegen de muur.")
        print("Het voelt alsof het je bescherming geeft (+1 defence).")
        return {'defence': 1}
    else:
        print("\nEen vlijmscherp legendarisch zwaard steekt in een steen.")
        print("Je trekt het eruit en voelt je sterker (+2 attack).")
        return {'attack': 2}

def kamer_4():
    print("\nPlotseling stort een vervallen deur in en een zombie komt naar binnen strompelen!")
    print("Zijn ogen gloeien groen in het duister terwijl hij gromt.")
    
    player = {
        'health': 50,
        'attack': 5,
        'defence': 3
    }
    
    zombie = {
        'health': 30,
        'attack': random.randint(3, 8),
        'defence': 2
    }
    
    # Bereken zombie schade per hit
    zombie_dmg = zombie['attack'] - player['defence']
    if zombie_dmg <= 0:
        print("\nDe zombie kan je geen schade toebrengen door je verdediging!")
        print("Je loopt er rustig langs.")
        return player
    
    # Bereken speler schade per hit
    player_dmg = player['attack'] - zombie['defence']
    
    # Bereken aantal hits nodig
    zombie_hits = (player['health'] + zombie_dmg - 1) // zombie_dmg  # Naar boven afronden
    player_hits = (zombie['health'] + player_dmg - 1) // player_dmg
    
    if player_hits < zombie_hits:
        print("\nMet een laatste krachtige slag versla je de zombie!")
        print("Maar je hebt wel schade opgelopen...")
        player['health'] -= player_hits * zombie_dmg
        print(f"Je hebt nu {player['health']} health over.")
    else:
        print("\nDe zombie overweldigt je met zijn aanvallen...")
        print("Alles wordt zwart...")
        player['health'] = 0
    
    return player

def kamer_5(has_key):
    if has_key:
        print("\nJe staat voor een enorme schatkist versierd met edelstenen.")
        print("De gouden sleutel past perfect in het slot...")
        print("De kist gaat open en een helder licht vervult de kamer!")
        print("\n*** GEFELICITEERD! Je hebt de schat van de Tempel der Verloren Zielen gevonden! ***")
    else:
        print("\nJe staat voor een enorme schatkist, maar hebt geen sleutel...")
        print("Plotseling hoor je een luid gekraak als de vloer onder je wegzakt!")
        print("\n*** GAME OVER - Je bent gevallen in een valkuil! ***")

def main():
    kamer_1()
    
    has_key = kamer_2()
    
    stats = kamer_3()
    print(stats)  # Voor debug doeleinden
    
    player = kamer_4()
    
    if player['health'] > 0:
        kamer_5(has_key)
    else:
        print("\n*** GAME OVER - Je bent verslagen door de zombie! ***")

if __name__ == "__main__":
    main()