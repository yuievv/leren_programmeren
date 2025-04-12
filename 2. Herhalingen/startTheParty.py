gastheer_input = input("Wie is de gastheer? ")

# Vraag het aantal gasten
try:
    gasten = int(input("Hoeveel gasten zijn er? "))
except ValueError:
    gasten = 0 

# Belangrijke namen
MIJN_NAAM = "Klaudia" 
SLB_NAAM = "Rudi" 

# Bepaal of er een gastheer is (lege input = geen gastheer)
gastheer = bool(gastheer_input.strip())
drank = True  
chips = True  

# Naamcondities
feest_garantie = gastheer_input.strip().lower() == MIJN_NAAM.lower()
geen_feest_garantie = gastheer_input.strip().lower() == SLB_NAAM.lower()

# Aangepaste originele voorwaarden voor integer gasten
start_condition_1 = gastheer or gasten > 0
start_condition_2 = gastheer or (gasten >= 4 and chips and drank)  # Minimaal 4 gasten nodig
start_condition_3 = not (chips and not drank)  
start_condition_4 = not (gasten > 0 and not chips and not drank)  
start_condition_5 = not (gastheer and not drank)  
start_condition_6 = not (not gastheer and gasten == 0 and chips)  

# Nieuwe voorwaarden voor aantal gasten
start_condition_7 = gasten >= 4 or gastheer  # Minimaal 4 gasten of gastheer
start_condition_8 = (gasten + (1 if gastheer else 0)) <= 20  # Max 20 personen totaal

# Combineer alle voorwaarden met de naamregels
if geen_feest_garantie:
    print('No Party - SLB verbod!')
elif feest_garantie:
    print('Start the Party - Jij bent de baas!')
elif (start_condition_1 and start_condition_2 and start_condition_3 and 
      start_condition_4 and start_condition_5 and start_condition_6 and
      start_condition_7 and start_condition_8):  
    print('Start the Party')  
else:  
    print('No Party')