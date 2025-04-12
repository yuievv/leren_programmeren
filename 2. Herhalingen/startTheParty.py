gastheer_input = input("Wie is de gastheer? ")

# Belangrijke namen
MIJN_NAAM = "Klaudia" 
SLB_NAAM = "Rudi" 

# Bepaal of er een gastheer is (lege input = geen gastheer)
gastheer = bool(gastheer_input.strip())
gasten = True  
drank = True  
chips = True  

# Naamcondities
feest_garantie = gastheer_input.strip().lower() == MIJN_NAAM.lower()
geen_feest_garantie = gastheer_input.strip().lower() == SLB_NAAM.lower()

# Originele voorwaarden
start_condition_1 = gastheer or gasten  
start_condition_2 = gastheer or (gasten and chips and drank)  
start_condition_3 = not (chips and not drank)  
start_condition_4 = not (gasten and not chips and not drank)  
start_condition_5 = not (gastheer and not drank)  
start_condition_6 = not (not gastheer and not gasten and chips)  

# Combineer alle voorwaarden met de naamregels
if geen_feest_garantie:
    print('No Party - SLB verbod!')
elif feest_garantie:
    print('Start the Party - Jij bent de baas!')
elif (start_condition_1 and start_condition_2 and start_condition_3 and 
      start_condition_4 and start_condition_5 and start_condition_6):  
    print('Start the Party')  
else:  
    print('No Party')