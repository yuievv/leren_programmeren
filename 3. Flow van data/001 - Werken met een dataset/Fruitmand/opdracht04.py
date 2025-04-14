# opdracht 04
import fruitmand
import random

aantal = int(input("Hoeveel random fruitsoorten wilt u zien? "))
print([random.choice(fruitmand.fruitmand)['name'] for _ in range(aantal)])