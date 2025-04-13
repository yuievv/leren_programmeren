def vergelijk_getallen(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return 'Beide getallen zijn even groot'
    elif nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    else:
        return f'Maximum: {nr2} en minimum: {nr1}'

# Testen
if __name__ == "__main__":
    # Test 1: nr1 > nr2
    resultaat1 = vergelijk_getallen(10, 5)
    print(resultaat1)  # Maximum: 10 en minimum: 5
    
    # Test 2: nr1 < nr2
    resultaat2 = vergelijk_getallen(3, 7)
    print(resultaat2)  # Maximum: 7 en minimum: 3
    
    # Test 3: nr1 == nr2
    resultaat3 = vergelijk_getallen(4, 4)
    print(resultaat3)  # Beide getallen zijn even groot