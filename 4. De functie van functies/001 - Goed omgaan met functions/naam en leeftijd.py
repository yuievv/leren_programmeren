def vraag_naam_leeftijd_en_woonplaats():
    """Vraagt de gebruiker om naam, leeftijd en woonplaats en retourneert deze als dictionary"""
    naam = input("Voer uw naam in: ")
    leeftijd = input("Voer uw leeftijd in: ")
    woonplaats = input("Voer uw woonplaats in: ")
    return {'name': naam, 'age': leeftijd, 'city': woonplaats}

def verzamel_gegevens():
    """Verzamelt meerdere personen tot de gebruiker 'stop' invoert"""
    personen = []
    while True:
        stop_input = input("Toets enter om door te gaan of 'stop' om te printen: ")
        if stop_input.lower() == 'stop':
            break
        
        persoon = vraag_naam_leeftijd_en_woonplaats()
        personen.append(persoon)
    return personen

alle_gegevens = verzamel_gegevens()

for persoon in alle_gegevens:
    print(f"{persoon['name']}, die in {persoon['city']} woont, is {persoon['age']} jaar")