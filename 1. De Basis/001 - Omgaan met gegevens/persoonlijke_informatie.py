naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht = input("Ben je een A) een jongen of B) een meisje? ").lower()
favoriete_kleur = input("Wat is je favoriete kleur? ")
favoriet_getal = int(input("Wat is je favoriete getal? "))
leeftijd_verschil = abs(leeftijd - favoriet_getal)
bezittelijk_voornaamwoord = 'haar' if geslacht == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{bezittelijk_voornaamwoord.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", favoriete_kleur)
print(f"Het verschil tussen {bezittelijk_voornaamwoord} leeftijd en {favoriet_getal} is:", leeftijd_verschil)