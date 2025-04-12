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

# Resultaat
print(f'De feestlunch kost je bij de bakker {te_betalen_bedrag:.2f} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!')