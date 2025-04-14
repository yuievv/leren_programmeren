# opdracht 08
import fruitmand

# Totaalgewicht
totaal = sum(fruit['weight'] for fruit in fruitmand.fruitmand)
print(f"Totaalgewicht fruitmand: {totaal} gram")

# Watermeloen toevoegen
fruitmand.fruitmand.append({
    'name': 'watermeloen',
    'weight': 2500, # in gram
    'color': 'green',
    'round': True
})

nieuw_totaal = sum(fruit['weight'] for fruit in fruitmand.fruitmand)
print(f"Totaalgewicht na toevoeging: {nieuw_totaal} gram")