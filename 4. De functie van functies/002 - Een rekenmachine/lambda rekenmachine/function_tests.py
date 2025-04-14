from functions import addition, subtraction, multiplication, division
from calculations import calculations
from test_lib import test, report

def test_functions():
    test("Optelling", addition(2,3), calculations['addition'](2,3))
    test("Aftrekking", subtraction(5,2), calculations['subtraction'](5,2))
    test("Vermenigvuldiging", multiplication(3,4), calculations['multiplication'](3,4))
    test("Deling", division(10,2), calculations['division'](10,2))
    test("Delen door nul", division(5,0), calculations['division'](5,0))

if __name__ == "__main__":
    test_functions()
    report()