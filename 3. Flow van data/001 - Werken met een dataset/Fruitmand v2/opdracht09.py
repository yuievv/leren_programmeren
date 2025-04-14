# opdracht 09
import fruitmand
fruitmand.fruitmand[:] = [fruit for fruit in fruitmand.fruitmand if fruit['name'] != 'druif']
print({fruit['color'] for fruit in fruitmand.fruitmand})