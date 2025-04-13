import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
player_rupees = 0
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

# === [kamer 7] === #
print('In een kleine kamer zie je iets glinsteren op de grond...')
if random.randint(1, 10) != 1:  # 1 in 10 chance for no rupee
    print('Je raapt het op: het is een rupee!')
    player_rupees += 1
    print(f'Je hebt nu {player_rupees} rupee.')
else:
    print('Het glinsterende voorwerp verdwijnt plotseling als je het probeert op te pakken!')
    print('Er ligt hier niets meer.')

print('Je ziet twee deuren: één rechtdoor en één naar rechts.')
keuze_7 = input('Welke kant ga je op? (rechtdoor/rechts): ').lower()

if keuze_7 == 'rechtdoor':
    # === [kamer 2] === #
    print('Je stapt door de deur en ziet een standbeeld met een rupee.')
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    print(f'Som op het standbeeld: {num1}{operator}{num2}=?')
    antwoord = int(input('Wat toets je in? '))

    if antwoord == correct_answer:
        print('Het standbeeld laat een rupee vallen.')
        player_rupees += 1
        print(f'Je hebt nu {player_rupees} rupees.')
    else:
        print('Er gebeurt niets...')

    print('Je ziet twee deuren: één links en één boven.')
    keuze = input('Welke kies je? (links/boven): ').lower()

    if keuze == 'links':
        # === [kamer 6] === #
        print('Je loopt een donkere kamer in...')
        print('Een zombie komt strompelend op je af!')

        if not fight_enemy(1, 0, 2, 'zombie'):
            exit()
        print('')
        time.sleep(1)

# === [kamer 8] === #
print('Je betreedt een kamer met een mysterieuze gokmachine.')
keuze_gok = input('Wil je gokken met de machine? (ja/nee): ').lower()

if keuze_gok == 'ja':
    print('Je trekt aan de hendel...')
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    total = roll_1 + roll_2
    print(f'Dobbelstenen: {roll_1} + {roll_2} = {total}')

    if total > 7:
        player_rupees *= 2
        print(f'Geluk! Je rupees worden verdubbeld. Je hebt nu {player_rupees} rupees.')
    elif total < 7:
        player_health -= 1
        print('Pech! Je verliest 1 health.')
        if player_health <= 0:
            print('Je bent overleden door de gokmachine. Game over.')
            exit()
        else:
            print(f'Je health is nu {player_health}.')
    else:
        player_rupees += 1
        player_health += 4
        print('Jackpot! Je krijgt 1 rupee en 4 health.')
        print(f'Je hebt nu {player_rupees} rupees en {player_health} health.')
else:
    print('Je laat de gokmachine met rust.')

# === [kamer 9] === #
print('Je komt in een betoverde kamer. De muren lijken te bewegen...')
effect = random.choice(['defense', 'health'])
if effect == 'defense':
    player_defense += 1
    print('Je voelt je beschermender! Je defense is met 1 verhoogd.')
else:
    player_health += 2
    print('Je voelt je vitaler! Je health is met 2 verhoogd.')
print(f'Je stats zijn nu: health={player_health}, defense={player_defense}, rupees={player_rupees}')

# === [kamer 3] === #
print('Je loopt een kamer binnen met een goblin achter een tafel.')
print('"Welkom, reiziger!" zegt hij. "Ik heb zwaarden, schilden en zelfs een sleutel voor 1 rupee per stuk."')
print(f'"Ik zie dat jij {player_rupees} rupee(s) hebt."')

while player_rupees > 0:
    keuze_item = input('Wat wil je kopen? (zwaard/schild/sleutel/stop): ').lower()
    if keuze_item == 'zwaard':
        player_attack += 2
        player_rupees -= 1
        print('Je aanval is nu sterker.')
    elif keuze_item == 'schild':
        player_defense += 1
        player_rupees -= 1
        print('Je verdediging is nu beter.')
    elif keuze_item == 'sleutel':
        has_key = True
        player_rupees -= 1
        print('Je hebt nu de sleutel voor de schatkist!')
    elif keuze_item == 'stop':
        break
    else:
        print('Geen geldig item.')

if player_rupees == 0:
    print('"Je hebt geen rupees meer, dus ik kan je niets meer verkopen!" zegt de goblin.')

print('Je verlaat de winkelkamer.')
print('')
time.sleep(1)

# === [kamer 4] === #
print('Een agressieve ork stormt op je af!')

if not fight_enemy(2, 0, 3, 'ork'):
    exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Je ziet een grote schatkist in het midden van de kamer...')
if has_key:
    print('Je gebruikt de sleutel en opent de schatkist. Je hebt gewonnen!')
else:
    print('De kist zit op slot. Zonder sleutel kun je hem niet openen. Game over.')