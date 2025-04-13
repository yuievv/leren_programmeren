import random

# Genereer deck
kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
waarden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
deck = [f"{k} {w}" for k in kleuren for w in waarden] + ['joker'] * 2

random.shuffle(deck)  # Schud het deck

# Toon eerste 7 kaarten
print("De eerste 7 kaarten:")
for i, kaart in enumerate(deck[:7], 1):
    print(f"kaart {i}: {kaart}")


print(f"\ndeck ({len(deck[7:])} kaarten): {deck[7:]}")