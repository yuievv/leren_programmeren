def is_even(number: int) -> bool:
    # Controleert of een gegeven getal even is.
    return number % 2 == 0


def reverse_words(sentence: str) -> str:
    # Keert de volgorde van woorden in een zin om.
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


def unique_char_count(text: str) -> int:
    # Berekent het aantal unieke tekens in een string.
    return len(set(text))


def average_word_length(sentence: str) -> float:
    # Berekent de gemiddelde lengte van woorden in een zin.
    words = sentence.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0


def multiplication_table(number: int, max_factor: int = 10) -> None:
    # Drukt de vermenigvuldigingstabel af voor een gegeven getal
    for factor in range(1, max_factor + 1):
        result = factor * number
        print(f'{factor} x {number} = {result}')

# Test voor is_even
print(is_even(4))  #True
print(is_even(7))  #False

# Test voor reverse_words
print(reverse_words("wereld hallo"))  
print(reverse_words("leuk is programmeren"))  

# Test voor unique_char_count
print(unique_char_count("hello"))  #4 ('h', 'e', 'l', 'o')
print(unique_char_count("aaaa"))  #1 ('a')

# Test voor average_word_length
print(average_word_length("dit is een test"))  # Verwacht: 2.75
print(average_word_length("hallo"))  # Verwacht: 5.0

# Test voor multiplication_table
multiplication_table(5, 6)

