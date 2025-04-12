# Vraag de gebruiker om 2 gehele getallen
a = int(input("Voer het eerste getal (a) in: "))
b = int(input("Voer het tweede getal (b) in: "))

# Bepaal of a groter is dan b
if a > b:
    Max = a
    print(f'a is het grootste getal: {Max}')
# Bepaal of a kleiner is dan b
elif a < b:
    Min = a
    print(f'a is het kleinste getal: {Min}')