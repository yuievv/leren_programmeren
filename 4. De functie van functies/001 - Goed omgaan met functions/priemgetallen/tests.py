from functions import *
from test_lib import test, report

expected = False
result = is_prime(-7)
test('TEST: is_prime(-7)',expected, result)

expected = False
result = is_prime(0)
test('TEST: is_prime(0)',expected, result)

expected = False
result = is_prime(1)
test('TEST: is_prime(1)',expected, result)

expected = True
result = is_prime(2)
test('TEST: is_prime(2)',expected, result)

expected = True
result = is_prime(7)
test('TEST: is_prime(7)',expected, result)

expected = False
result = is_prime(66)
test('TEST: is_prime(66)',expected, result)

expected = True
result = is_prime(101)
test('TEST: is_prime(101)',expected, result)

expected = False
result = is_prime(19872496)
test('TEST: is_prime(19872496)',expected, result)

# Test voor primes_up_to
expected = [2, 3, 5, 7]
result = primes_up_to(10)
test('TEST: primes_up_to(10)', expected, result)

expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
result = primes_up_to(30)
test('TEST: primes_up_to(30)', expected, result)

# Test voor first_n_primes
expected = [2, 3, 5]
result = first_n_primes(3)
test('TEST: first_n_primes(3)', expected, result)

expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
result = first_n_primes(10)
test('TEST: first_n_primes(10)', expected, result)

# Test voor primes_between
expected = [11, 13, 17, 19]
result = primes_between(10, 20)
test('TEST: primes_between(10, 20)', expected, result)

expected = [101, 103, 107, 109, 113]
result = primes_between(100, 115)
test('TEST: primes_between(100, 115)', expected, result)

if __name__ == "__main__":
    report()
