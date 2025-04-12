from termcolor import colored

# Aantal producten + prijzen
aantal_croissantjes = 17
prijs_croissantje = 0.39  
aantal_stokbroden = 2
prijs_stokbrood = 2.78 

# Kortingsbonnen
aantal_kortingsbonnen = 3
korting_per_bon = 0.50  

# Totale kosten berekenen
totale_kosten = (aantal_croissantjes * prijs_croissantje) + (aantal_stokbroden * prijs_stokbrood)
totale_korting = aantal_kortingsbonnen * korting_per_bon
te_betalen_bedrag = totale_kosten - totale_korting

# Resultaat met gekleurde variabelen
print(f'De feestlunch kost je bij de bakker {colored(te_betalen_bedrag, "light_magenta")} euro voor de {colored(aantal_croissantjes, "light_cyan")} croissantjes en de {colored(aantal_stokbroden, "red")} stokbroden als de {colored(aantal_kortingsbonnen, "yellow")} kortingsbonnen nog geldig zijn!')