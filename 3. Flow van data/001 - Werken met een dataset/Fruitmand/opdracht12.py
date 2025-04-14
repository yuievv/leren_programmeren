# opdracht 12
import fruitmand

# Vertaalwoordenboek voor kleuren
kleur_vertaling = {
    'yellow': 'gele',
    'green': 'groene',
    'orange': 'oranje',
    'brown': 'bruine',
    'red': 'rode'
}

# Vind fruit met langste naam
langste_fruit = max(fruitmand.fruitmand, key=lambda x: len(x['name']))

print(f'De "{langste_fruit["name"]}" ({len(langste_fruit["name"])} letters) heeft een {kleur_vertaling[langste_fruit["color"]]} kleur en een gewicht van {langste_fruit["weight"]/1000} kg.')