print('Welk seizoen vind jij het fijnst?', 
      "A) Lente", 
      "B) Zomer", 
      "C) Herfst", 
      "D) Winter")
keuze = input('? ')

if (gekozen_seizoen == 'a' or 'c'):
    print('Dus jij vindt een tussenseizoen het fijnst...')
elif (gekozen_seizoen != 'a', 'c', 'd'):
    weer_type = 'warm'
else:
    weer_type = 'koud'

if len(weer_type) > 0:
    print(f'Dus jij houd van {weer_type} weer!')
else:
    print('Dit is geen te kiezen optie!')
