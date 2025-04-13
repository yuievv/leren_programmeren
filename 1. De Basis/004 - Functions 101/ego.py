import re

def extract_sub_sentences(text):
    """Extraheer deelzinnen uit een tekst door scheidingstekens te vervangen"""
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|")
    return [s.strip() for s in sub_sentences if s.strip()]

def calculate_ego_score(sub_sentences):
    """Bereken ego-score op basis van hoe vaak zinnen met 'ik' of 'mijn' beginnen"""
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.lower()
        words = sentence.split()
        if len(words) >= 1 and (words[0] in ('ik', 'mijn')):
            ego_score += 1
        elif len(words) >= 2 and words[1] in ('ik', 'mijn'):
            ego_score += 1
    return ego_score

# Testgeval 1: Originele sollicitatiebrief (hoge ego-score verwacht)
text1 = """Geachte heer/mevrouw,
Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf. Ik ben de beste kandidaat voor deze functie omdat ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren. Ik ben buitengewoon slim en in staat om snel nieuwe informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf. Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf, en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen. Mijn CV is overtuigend! Mijn referenties zijn heel positief over mij. Ik verdien daarom een plek in uw team.
Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen, zodat ik u persoonlijk kan overtuigen van mijn geschiktheid voor deze functie."""

# Testgeval 2: Bescheiden sollicitatiebrief (lagere ego-score verwacht)
text2 = """Geachte heer/mevrouw,
Na het lezen van de vacature voor programmeur bij uw bedrijf, ben ik enthousiast geworden over de mogelijkheid om deel uit te maken van uw team. In mijn vorige functies heb ik waardevolle ervaring opgedaan die goed aansluit bij wat u zoekt. Samenwerken in een team vind ik belangrijk, en ik sta altijd open voor feedback om mij verder te ontwikkelen. De projecten van uw bedrijf spreken mij aan omdat ze innovatief zijn en bijdragen aan betekenisvolle oplossingen."""

# Testgeval 3: Neutrale tekst (score 0 verwacht)
text3 = """Het is belangrijk om te kijken naar de verschillende aspecten van een sollicitatiebrief. Een goede brief bevat zowel informatie over de kandidaat als over de motivatie voor het bedrijf. Door aandacht te besteden aan zowel ervaringen als toekomstige doelen, ontstaat een gebalanceerd beeld."""

# Uitvoeren van de testen
test_cases = [
    ("Originele sollicitatiebrief", text1),
    ("Bescheiden sollicitatiebrief", text2),
    ("Neutrale tekst", text3)
]

for case_name, text in test_cases:
    sub_sentences = extract_sub_sentences(text)
    score = calculate_ego_score(sub_sentences)
    print(f"{case_name}:")
    print(f"Aantal deelzinnen: {len(sub_sentences)}")
    print(f"Ego-score: {score}")
    print(f"Percentage: {(score/len(sub_sentences))*100:.1f}%\n")