from functions import is_prime, primes_up_to, first_n_primes, primes_between

def main():
    print("Priemgetallen programma")
    print("1: Check of een getal priem is")
    print("2: Toon alle priemgetallen tot een bepaald getal")
    print("3: Toon een bepaald aantal priemgetallen")
    print("4: Toon priemgetallen tussen twee getallen")
    
    choice = input("Kies een optie (1-4): ")
    
    if choice == "1":
        num = int(input("Voer een getal in: "))
        if is_prime(num):
            print(f"{num} is een priemgetal")
        else:
            print(f"{num} is geen priemgetal")
    
    elif choice == "2":
        num = int(input("Voer een maximum getal in: "))
        primes = primes_up_to(num)
        if primes:
            print(f"Priemgetallen tot en met {num}: {', '.join(map(str, primes))}")
        else:
            print(f"Geen priemgetallen gevonden tot en met {num}")
    
    elif choice == "3":
        num = int(input("Hoeveel priemgetallen wilt u zien? "))
        primes = first_n_primes(num)
        print(f"De eerste {num} priemgetallen zijn: {', '.join(map(str, primes))}")
    
    elif choice == "4":
        min_num = int(input("Voer het laagste getal in: "))
        max_num = int(input("Voer het hoogste getal in: "))
        primes = primes_between(min_num, max_num)
        if primes:
            print(f"Priemgetallen tussen {min_num} en {max_num}: {', '.join(map(str, primes))}")
        else:
            print(f"Geen priemgetallen gevonden tussen {min_num} en {max_num}")
    
    else:
        print("Ongeldige keuze")

if __name__ == "__main__":
    main()