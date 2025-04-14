from termcolor import colored
from personen_info import verzamel_gegevens

def bereken_volwassenheid(leeftijd):
    """Bepaalt de volwassenheid tekst op basis van leeftijd"""
    try:
        leeftijd_int = int(leeftijd)
        if leeftijd_int >= 18:
            return colored(f"die al {leeftijd_int - 18} jaar volwassen is", "green")
        else:
            return colored("die nog niet volwassen is", "yellow")
    except ValueError:
        return colored("met onbekende volwassenheid", "red")

def main():
    personen = verzamel_gegevens()
    
    print(colored("\n=== Resultaat ===", "red", attrs=["bold"]))
    for persoon in personen:
        volwassenheid = bereken_volwassenheid(persoon['age'])
        print(f"In {colored(persoon['city'], 'cyan')} woont {colored(persoon['name'], 'magenta')}, {volwassenheid}.")

if __name__ == "__main__":
    main()