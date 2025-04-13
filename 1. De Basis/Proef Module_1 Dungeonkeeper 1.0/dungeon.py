import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
has_key = False

# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 2] === #
print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
print('Het standbeeld heeft een sleutel vast.')
print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')

# Random som genereren
num1 = random.randint(10, 25)
num2 = random.randint(-5, 75)
operator = random.choice(['+', '-', '*'])

# Som berekenen
if operator == '+':
    correct_answer = num1 + num2
elif operator == '-':
    correct_answer = num1 - num2
else:  # operator == '*'
    correct_answer = num1 * num2

print(f'Daarboven zie je een som staan {num1}{operator}{num2}=?')
antwoord = int(input('Wat toest je in?'))

if antwoord == correct_answer:
    print('Het standbeeld laat de sleutel vallen en je pakt het op')
    has_key = True
else:
    print('Er gebeurt niets....')

print('Je ziet een deur achter het standbeeld.')
print('')
time.sleep(1)

# === [kamer 3] === #
# Random item kiezen
item = random.choice(['schild', 'zwaard'])

if item == 'schild':
    player_defense += 1
else:  # zwaard
    player_attack += 2

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je loopt tegen een zombie aan.')

zombie_hit_damage = (zombie_attack - player_defense)
if zombie_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
else:
    zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
    
    player_hit_damage = (player_attack - zombie_defense)
    player_attack_amount = math.ceil(zombie_health / player_hit_damage)

    if player_attack_amount < zombie_attack_amount:
        # Bereken nieuwe health van speler
        player_health -= player_attack_amount * zombie_hit_damage
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de zombie te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if has_key:
    print('Gebruikend met de sleutel open je de schatkist.')
    print('Gefeliciteerd! Je hebt de schat gevonden en het spel gewonnen!')
else:
    print('Je probeert de schatkist te openen maar hij zit op slot.')
    print('Zonder de sleutel kun je hem niet openen. Game over.')