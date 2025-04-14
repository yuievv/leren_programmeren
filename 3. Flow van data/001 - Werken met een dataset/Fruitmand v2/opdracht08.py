# opdracht 08
import fruitmand
totaal = sum(fruit['weight'] for fruit in fruitmand.fruitmand)
print(f"Totaalgewicht fruitmand: {totaal} gram")

fruitmand.fruitmand.append({
    'name': 'watermeloen',
    'weight': 2500,
    'color': 'green',
    'round': True
})

print(f"Totaalgewicht na toevoeging: {totaal + 2500} gram")