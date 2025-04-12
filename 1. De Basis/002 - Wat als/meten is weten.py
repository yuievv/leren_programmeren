# Vraag de gebruiker om 2 gehele getallen
a = int(input("Voer het eerste getal (a) in: "))
b = int(input("Voer het tweede getal (b) in: "))

# Bepaal of a groter is dan b
if a > b:
    Max = a
    Min = b
    print(f'a is het grootste getal: {Max}')
# Bepaal of a kleiner is dan b
elif a < b:
    Min = a
    Max = b
    print(f'a is het kleinste getal: {Min}')
# Anders zijn ze gelijk
else:
    Min = a
    Max = b
    print('a en b zijn even groot')

# Print altijd het minimum en maximum
print(f'Het minimum is: {Min}')
print(f'Het maximum is: {Max}')