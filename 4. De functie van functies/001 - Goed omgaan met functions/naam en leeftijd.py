def vraag_naam_en_leeftijd():
    """Vraagt de gebruiker om naam en leeftijd en retourneert deze als dictionary"""
    naam = input("Voer uw naam in: ")
    leeftijd = input("Voer uw leeftijd in: ")
    return {'name': naam, 'age': leeftijd}

gegevens = vraag_naam_en_leeftijd()
print(f"{gegevens['name']} is {gegevens['age']} jaar")