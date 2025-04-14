# opdracht 10
import fruitmand
for fruit in sorted(fruitmand.fruitmand, key=lambda x: x['weight'], reverse=True):
    print(f"{fruit['name']}: {fruit['weight']/1000:.3f} kg")