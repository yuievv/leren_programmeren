from termcolor import colored

# Input voor aantal personen en toegangsprijs
aantal_personen = int(input("Hoeveel personen gaan er? "))
toegangsticket_prijs = int(float(input("Toegangsprijs per persoon (in euro)? ")) * 100)

# Input voor VR-kosten
vip_prijs_per_5_min = int(float(input("Kosten VR-GameSeat per 5 minuten (in euro)? ")) * 100)
aantal_minuten_vip = int(input("Hoeveel minuten VR? "))

# Berekenen in centen
aantal_5_minuten_blokken = aantal_minuten_vip / 5
vip_kosten_per_persoon = int(aantal_5_minuten_blokken * vip_prijs_per_5_min)
totale_kosten_per_persoon = toegangsticket_prijs + vip_kosten_per_persoon
totale_kosten = totale_kosten_per_persoon * aantal_personen

# Verdeel kosten over 2 personen
aantal_betalende_personen = 2
bijdrage_per_persoon = totale_kosten // aantal_betalende_personen

# Omzetten naar euro voor weergave
toegang_euro = toegangsticket_prijs / 100
vip_prijs_euro = vip_prijs_per_5_min / 100
bijdrage_euro = bijdrage_per_persoon / 100

# Resultaat met gekleurde variabelen
print(f'Dit gezellige dagje-uit met {colored(aantal_personen, "light_magenta")} mensen in de Speelhal met {colored(aantal_minuten_vip, "light_blue")} minuten VR (€{vip_prijs_euro:.2f} per 5 min) kost je maar {colored(f"€{bijdrage_euro:.2f}", "red")} per persoon voor {colored(aantal_betalende_personen, "green")} mensen')