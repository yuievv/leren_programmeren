# opdracht 12
import fruitmand
kleur_vertaling = {
    'yellow': 'gele', 'green': 'groene', 'orange': 'oranje',
    'brown': 'bruine', 'red': 'rode', 'purple': 'paarse',
    'pink': 'roze', 'black': 'zwarte'
}

langste_fruit = max(fruitmand.fruitmand, key=lambda x: len(x['name']))
print(f'De "{langste_fruit["name"]}" ({len(langste_fruit["name"])} letters) heeft een {kleur_vertaling.get(langste_fruit["color"], langste_fruit["color"])} kleur en een gewicht van {langste_fruit["weight"]/1000:.3f} kg.')