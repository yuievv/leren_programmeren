# Controleert of een getal een priemgetal is.
def is_prime(number:int) -> bool:
    # Als het getal kleiner of gelijk is aan 1, is het geen priemgetal
    if number <= 1:
        return False
    
    # 2 is het enige even priemgetal
    if number == 2:
        return True
    
    # Andere even getallen zijn geen priemgetallen
    if number % 2 == 0:
        return False
    
    # Controleer delers tot de wortel van het getal (efficiëntie)
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):  # Alleen oneven getallen controleren
        if number % d == 0:
            return False
    
    # Als geen delers gevonden zijn, is het een priemgetal
    return True

def primes_up_to(max_num: int) -> list:
    """Retourneert een lijst met alle priemgetallen tot en met max_num"""
    primes = []
    for num in range(2, max_num + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def first_n_primes(n: int) -> list:
    """Retourneert de eerste n priemgetallen"""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def primes_between(min_num: int, max_num: int) -> list:
    """Retourneert alle priemgetallen tussen min_num en max_num"""
    primes = []
    for num in range(min_num, max_num + 1):
        if is_prime(num):
            primes.append(num)
    return primes