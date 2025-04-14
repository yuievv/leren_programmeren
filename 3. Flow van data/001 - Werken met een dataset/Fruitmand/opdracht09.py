# opdracht 09
import fruitmand

# Druif verwijderen
fruitmand.fruitmand[:] = [fruit for fruit in fruitmand.fruitmand if fruit['name'] != 'druif']

# Unieke kleuren tonen
unieke_kleuren = {fruit['color'] for fruit in fruitmand.fruitmand}
print(unieke_kleuren)