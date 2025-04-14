# opdracht 06
import fruitmand
appel = next(fruit for fruit in fruitmand.fruitmand if fruit['name'] == 'appel')
print(appel['weight'])