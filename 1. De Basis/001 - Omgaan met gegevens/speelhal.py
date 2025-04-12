from termcolor import colored

# Aantal personen
aantal_personen = 5

# Kosten p.p voor toegangsticket
toegangsticket_prijs = 7.45 

# Kosten voor VIP-VR-GameSeat p.p per 5 minuten
vip_prijs_per_5_min = 0.37 
aantal_minuten_vip = 45

# VIP-kosten p.p
aantal_5_minuten_blokken = aantal_minuten_vip / 5
vip_kosten_per_persoon = aantal_5_minuten_blokken * vip_prijs_per_5_min

# Totale kosten p.p
totale_kosten_per_persoon = toegangsticket_prijs + vip_kosten_per_persoon

# Totale kosten voor allemaal
totale_kosten = totale_kosten_per_persoon * aantal_personen

# Jij en 1 vriend betalen elk de helft van de totale kosten
bijdrage_per_persoon = totale_kosten / 2
aantal_betalende_personen = 2

# Resultaat met gekleurde variabelen
print(f'Dit gezellige dagje-uit met {colored(aantal_personen, "light_magenta")} mensen in de Speelhal met {colored(aantal_minuten_vip, "light_blue")} minuten VR kost je maar {colored(bijdrage_per_persoon, "red")} euro per persoon voor {colored(aantal_betalende_personen, "green")} mensen')