DRANKJES_PRIJS = {'cola': 1.80, 'bier': 2.40, 'champagne': 12.30}
VIP_LIST = {'jeroen', 'jouke', 'rudi'}

def vraag_om_input(prompt):
    return input(prompt).strip().lower()

def check_toegang(leeftijd):
    if leeftijd < 18:
        print("Sorry, je mag niet naar binnen. Probeer het over", 18 - leeftijd, "jaar nog eens.")
        return False
    elif leeftijd == 18:
        print("Sorry, je mag niet naar binnen. Probeer het over", 3, "jaar nog eens.")
        return False
    return True

def bestel_drank(leeftijd, is_vip):
    while True:
        drank = vraag_om_input("Wat wil je drinken? (cola, bier, champagne) ")
        if drank in DRANKJES_PRIJS:
            if drank == "champagne" and not is_vip:
                print("Sorry, alleen VIPs mogen champagne bestellen.")
            elif drank in ["bier", "champagne"] and leeftijd < 21:
                print("Sorry, je mag geen alcohol bestellen onder de 21.")
            else:
                print(f"Hier is je {drank}, dat kost €{DRANKJES_PRIJS[drank]:.2f}")
        else:
            print("Sorry, dat drankje ken ik niet.")

        if vraag_om_input("Wil je nog iets anders drinken? (ja/nee) ") != "ja":
            break

leeftijd = int(vraag_om_input("Hoe oud ben je? "))
naam = vraag_om_input("Wat is je naam? ")
is_vip = naam in VIP_LIST

if check_toegang(leeftijd):
    if is_vip:
        bandje_kleur = "blauw" if leeftijd >= 21 else "rood"
        print(f"Je krijgt een {bandje_kleur} bandje.")
    bestel_drank(leeftijd, is_vip)

print("Einde programma.")