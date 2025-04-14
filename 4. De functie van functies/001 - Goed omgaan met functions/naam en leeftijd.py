def vraag_naam_en_leeftijd():
    """Vraagt de gebruiker om naam en leeftijd en retourneert deze als dictionary"""
    naam = input("Voer uw naam in: ")
    leeftijd = input("Voer uw leeftijd in: ")
    return {'name': naam, 'age': leeftijd}

def verzamel_gegevens():
    """Verzamelt meerdere namen en leeftijden tot de gebruiker 'stop' invoert"""
    personen = []
    while True:
        stop_input = input("Toets enter om door te gaan of 'stop' om te printen: ")
        if stop_input.lower() == 'stop':
            break
        
        persoon = vraag_naam_en_leeftijd()
        personen.append(persoon)
    return personen

alle_gegevens = verzamel_gegevens()

for persoon in alle_gegevens:
    print(f"{persoon['name']} is {persoon['age']} jaar")