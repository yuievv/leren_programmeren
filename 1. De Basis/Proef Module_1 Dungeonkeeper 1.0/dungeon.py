import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
has_key = False

def fight_enemy(enemy_attack, enemy_defense, enemy_health, enemy_name):
    global player_health
    
    enemy_hit_damage = (enemy_attack - player_defense)
    if enemy_hit_damage <= 0:
        print(f'Jij hebt een te goede verdediging voor de {enemy_name}, hij kan je geen schade doen.')
        return True
    
    enemy_attack_amount = math.ceil(player_health / enemy_hit_damage)
    player_hit_damage = (player_attack - enemy_defense)
    player_attack_amount = math.ceil(enemy_health / player_hit_damage)

    if player_attack_amount < enemy_attack_amount:
        player_health -= player_attack_amount * enemy_hit_damage
        print(f'In {player_attack_amount} rondes versla je de {enemy_name}.')
        print(f'Je health is nu {player_health}.')
        return True
    else:
        print(f'Helaas is de {enemy_name} te sterk voor je.')
        print('Game over.')
        return False

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

num1 = random.randint(10, 25)
num2 = random.randint(-5, 75)
operator = random.choice(['+', '-', '*'])

if operator == '+':
    correct_answer = num1 + num2
elif operator == '-':
    correct_answer = num1 - num2
else:
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

# === [kamer 6] === #
zombie_attack = 1
zombie_defense = 0
zombie_health = 2
print('Je komt een donkere kamer binnen en hoort gegrom...')
print('Een zombie verschijnt!')

if not fight_enemy(zombie_attack, zombie_defense, zombie_health, 'zombie'):
    exit()
print('')
time.sleep(1)

# === [kamer 3] === #
item = random.choice(['schild', 'zwaard'])

if item == 'schild':
    player_defense += 1
else:
    player_attack += 2

print('Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel met daarop een {item}.')
print(f'Je pakt het {item} op en houd het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
print('Je ziet een gemene ork voor je!')

ork_attack = 2
ork_defense = 0
ork_health = 3

if not fight_enemy(ork_attack, ork_defense, ork_health, 'ork'):
    exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een vijand tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if has_key:
    print('Gebruikend met de sleutel open je de schatkist.')
    print('Gefeliciteerd! Je hebt de schat gevonden en het spel gewonnen!')
else:
    print('Je probeert de schatkist te openen maar hij zit op slot.')
    print('Zonder de sleutel kun je hem niet openen. Game over.')