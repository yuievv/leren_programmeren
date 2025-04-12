from studieadviestext import *

def hoofdprogramma():
    print(STUDIEDOKTER_TITEL)
    
    # Opdracht B: Vraag naar weken studie
    weken = int(input(AANTAL_WEKEN_VRAAG + ' '))
    extra_vragen_tonen = weken >= 10
    
    vragen = [
        COMPETENTIE_STELLING_1,
        COMPETENTIE_STELLING_2,
        COMPETENTIE_STELLING_3,
        COMPETENTIE_STELLING_4,
        COMPETENTIE_STELLING_5
    ]
    
    if extra_vragen_tonen:
        vragen.append(COMPETENTIE_STELLING_6)
        vragen.append(COMPETENTIE_STELLING_7)
    
    totaalscore = 0
    antwoorden = []
    
    # Stel vragen en verzamel antwoorden
    for vraag in vragen:
        print(vraag)
        print(OPTIES)
        antwoord = int(input('Jouw antwoord (0-4): '))
        while antwoord < 0 or antwoord > 4:
            print('Ongeldig antwoord. Kies een getal tussen 0 en 4.')
            antwoord = int(input('Jouw antwoord (0-4): '))
        antwoorden.append(antwoord)
        totaalscore += antwoord
    
    # Bereken statistieken
    aantal_vragen = len(vragen)
    gemiddelde_score = totaalscore / aantal_vragen
    
    # Opdracht C: Tel specifieke antwoorden
    altijd_aantal = antwoorden.count(0)
    vaak_aantal = antwoorden.count(1)
    regelmatig_aantal = antwoorden.count(2)
    
    totaal_speciale_antwoorden = altijd_aantal + vaak_aantal + regelmatig_aantal
    
    # Bepaal advies
    if gemiddelde_score <= 2 or (altijd_aantal + vaak_aantal) > aantal_vragen / 2:
        advies = COMPETENTIE_ADVIES_ZORGELIJK
    elif gemiddelde_score <= 3 or totaal_speciale_antwoorden > aantal_vragen / 2:
        advies = COMPETENTIE_ADVIES_TWIJFELACHTIG
    else:
        advies = COMPETENTIE_ADVIES_GERUSTSTELLEND
    
    # Toon resultaten
    print(COMPETENTIE_ADVIES_TITEL)
    print(f"Jouw score: {totaalscore} (gemiddelde: {gemiddelde_score:.1f})")
    print(advies)

if __name__ == "__main__":
    hoofdprogramma()