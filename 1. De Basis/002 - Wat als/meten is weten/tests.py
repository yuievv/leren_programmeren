from meten_is_weten import vergelijk_getallen
from test_lib import test, report

# Test 1: beide getallen gelijk
expected = 'Beide getallen zijn even groot'
result = vergelijk_getallen(5, 5)
test('TEST nr1 == nr2', expected, result)

# Test 2: nr1 groter dan nr2
expected = 'Maximum: 10 en minimum: 5'
result = vergelijk_getallen(10, 5)
test('TEST nr1 > nr2', expected, result)

# Test 3: nr1 kleiner dan nr2
expected = 'Maximum: 8 en minimum: 3'
result = vergelijk_getallen(3, 8)
test('TEST nr1 < nr2', expected, result)

if __name__ == "__main__":
    report()