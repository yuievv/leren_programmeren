# Wachtwoord
geheim_wachtwoord = "Hallo123"

# Aantal pogingen
pogingen = 0
max_pogingen = 5

while pogingen < max_pogingen:
    invoer = input("Voer het wachtwoord in: ")
    pogingen += 1
    
    # Wachtwoord controleren
    if invoer == geheim_wachtwoord:
        print(f"Goed gedaan! Je had {pogingen} poging(en) nodig.")
        break
else:
    print("Je mag niet meer inloggen. Maximum aantal pogingen bereikt.")