import random

# Beschikbare kleuren
kleuren = ["rood", "blauw", "groen", "geel", "bruin"]

# Vraag hoeveel M&M's er aan de zak toegevoegd moeten worden
aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))

# Maak een lege dictionary en vul deze
zak_mms = {}
for _ in range(aantal):
    kleur = random.choice(kleuren)
    zak_mms[kleur] = zak_mms.get(kleur, 0) + 1


print("\nDe inhoud van de zak met M&M's is:")
print(zak_mms)