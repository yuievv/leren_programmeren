# opdracht 11
import fruitmand

# Unieke kleuren uithalen van fruitmand
beschikbare_kleuren = {fruit['color'] for fruit in fruitmand.fruitmand}

while True:
    kleur = input(f"Kies een kleur uit {beschikbare_kleuren}: ").lower()
    if kleur in beschikbare_kleuren:
        break
    print(f"De kleur {kleur} zit er niet in de fruitmand")

# Tel ronde en niet ronde vruchten van gekozen kleur
ronde = 0
niet_ronde = 0
for fruit in fruitmand.fruitmand:
    if fruit['color'] == kleur:
        if fruit['round']:
            ronde += 1
        else:
            niet_ronde += 1

# Verschil bepalen
verschil = abs(ronde - niet_ronde)
if ronde > niet_ronde:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
elif ronde < niet_ronde:
    print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
else:
    print(f"Er zijn {ronde} ronde vruchten en {niet_ronde} niet ronde vruchten in de kleur {kleur}")