from test_lib import test, report
from functions import addition, subtraction, multiplication, division
from calculations import CALCULATIONS

# 1. Test Addition
n1, n2 = 5, 3
expected = addition(n1, n2)
result = CALCULATIONS['addition'](n1, n2)
test('Addition', expected, result)

# 2. Test Subtraction
n1, n2 = 10, 4
expected = subtraction(n1, n2)
result = CALCULATIONS['subtraction'](n1, n2)
test('Subtraction', expected, result)

# 3. Test Multiplication
n1, n2 = 6, 7
expected = multiplication(n1, n2)
result = CALCULATIONS['multiplication'](n1, n2)
test('Multiplication', expected, result)

# 4. Test Division
n1, n2 = 9, 3
expected = division(n1, n2)
result = CALCULATIONS['division'](n1, n2)
test('Division', expected, result)

# Generate the test report
report()