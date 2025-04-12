from termcolor import colored

# Input voor aantallen en prijzen (in euro's)
aantal_croissantjes = int(input("Hoeveel croissantjes? "))
prijs_croissantje = int(float(input("Prijs per croissantje (in euro)? ")) * 100)
aantal_stokbroden = int(input("Hoeveel stokbroden? "))
prijs_stokbrood = int(float(input("Prijs per stokbrood (in euro)? ")) * 100)

# Input voor kortingsbonnen
aantal_kortingsbonnen = int(input("Hoeveel kortingsbonnen? "))
korting_per_bon = int(float(input("Waarde per kortingsbon (in euro)? ")) * 100)

# Berekenen in centen
totale_kosten = (aantal_croissantjes * prijs_croissantje) + (aantal_stokbroden * prijs_stokbrood)
totale_korting = aantal_kortingsbonnen * korting_per_bon
te_betalen_bedrag = totale_kosten - totale_korting

# Omzetten naar euro voor weergave
te_betalen_euro = te_betalen_bedrag / 100
aantal_croissantjes_euro = prijs_croissantje / 100
aantal_stokbroden_euro = prijs_stokbrood / 100
korting_per_bon_euro = korting_per_bon / 100

# Resultaat met gekleurde variabelen
# Resultaat met gekleurde variabelen
print(f'De feestlunch kost je bij de bakker {colored(f"€{te_betalen_euro:.2f}", "light_magenta")} voor de {colored(aantal_croissantjes, "light_cyan")} croissantjes à €{aantal_croissantjes_euro:.2f} en de {colored(aantal_stokbroden, "red")} stokbroden à €{aantal_stokbroden_euro:.2f} als de {colored(aantal_kortingsbonnen, "yellow")} kortingsbonnen van €{korting_per_bon_euro:.2f} nog geldig zijn!')