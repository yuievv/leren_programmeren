# Adreskaart generator

# Gebruikersgegevens
naam = input("Voer uw volledige naam in: ")
adres = input("Voer uw straatnaam en huisnummer in: ")
postcode = input("Voer uw postcode in (bijv. 1234 AB): ")
woonplaats = input("Voer uw woonplaats in: ")

# Adreskaart weergeven
print("\n\n ----------------------------------------------------")
print(f"|  Naam      : {naam.ljust(38)}|")
print(f"|  Adres     : {adres.ljust(38)}|")
print(f"|  Postcode  : {postcode.ljust(38)}|")
print(f"|  Woonplaats: {woonplaats.ljust(38)}|")
print(" ----------------------------------------------------")