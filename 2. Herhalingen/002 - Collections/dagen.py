# Tuple met alle dagen van de week
weekdagen = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')

# 1. Alle dagen van de week
print("Alle dagen van de week zijn:")
for dag in weekdagen:
    print(f"- {dag}")

# 2. De weekenddagen
print("\nDe weekenddagen zijn: ", end="")
print(" & ".join(weekdagen[5:]))

# 3. De werkdagen
werkdagen = weekdagen[:5]
print("\nDe werkdagen zijn: ", end="")
print(", ".join(werkdagen[:-1]), end=" & ")
print(werkdagen[-1])

# 4. Alle dagen in omgekeerde volgorde
print("\nAlle dagen van de week in omgekeerde volgorde zijn: ", end="")
print(" -> ".join(reversed(weekdagen)), end=".\n")

# 5. Werkdagen in omgekeerde volgorde
print("\nDe werkdagen in omgekeerde volgorde zijn:")
for dag in reversed(werkdagen):
    print(f"- {dag}")

# 6. Weekenddagen in omgekeerde volgorde
print("\nDe weekenddagen in omgekeerde volgorde zijn: ", end="")
print(" + ".join(reversed(weekdagen[5:])))