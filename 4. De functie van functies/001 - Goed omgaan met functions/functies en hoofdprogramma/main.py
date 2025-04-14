from personen_info import verzamel_gegevens

def main():
    personen = verzamel_gegevens()
    
    print("\n=== Resultaat ===")
    for persoon in personen:
        print(f"{persoon['name']}, die in {persoon['city']} woont, is {persoon['age']} jaar")

if __name__ == "__main__":
    main()