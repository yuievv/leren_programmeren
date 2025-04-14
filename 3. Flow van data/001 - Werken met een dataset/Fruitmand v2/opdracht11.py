# opdracht 11
import fruitmand
beschikbare_kleuren = {fruit['color'] for fruit in fruitmand.fruitmand}

while True:
    kleur = input(f"Kies een kleur uit {beschikbare_kleuren}: ").lower()
    if kleur in beschikbare_kleuren: break
    print(f"De kleur {kleur} zit er niet in de fruitmand")

ronde = sum(1 for fruit in fruitmand.fruitmand if fruit['color'] == kleur and fruit['round'])
niet_ronde = sum(1 for fruit in fruitmand.fruitmand if fruit['color'] == kleur and not fruit['round'])

if ronde > niet_ronde:
    print(f"Er zijn {ronde - niet_ronde} meer ronde vruchten in {kleur}")
elif ronde < niet_ronde:
    print(f"Er zijn {niet_ronde - ronde} minder ronde vruchten in {kleur}")
else:
    print(f"Evenveel ronde ({ronde}) als niet-ronde ({niet_ronde}) vruchten in {kleur}")