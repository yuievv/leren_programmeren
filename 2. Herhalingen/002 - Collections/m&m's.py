import random

# Beschikbare kleuren
kleuren = ("oranje", "blauw", "groen", "bruin")

# Vraag hoeveel M&M's er aan de zak toegevoegd moeten worden
aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))

# Maak een lege list (zak) en vul deze met willekeurige kleuren
zak_mms = []
for _ in range(aantal):
    willekeurige_kleur = random.choice(kleuren)
    zak_mms.append(willekeurige_kleur)

# Resultaat
print("\nDe inhoud van de zak met M&M's is:")
print(zak_mms)