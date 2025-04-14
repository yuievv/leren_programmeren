# opdracht 10
import fruitmand

# Sorteer op gewicht en converteer naar kg
gesorteerd_fruit = sorted(fruitmand.fruitmand, key=lambda x: x['weight'], reverse=True)

# Naam en gewicht printen in kg
for fruit in gesorteerd_fruit:
    print(f"{fruit['name']}: {fruit['weight']/1000:.3f} kg")