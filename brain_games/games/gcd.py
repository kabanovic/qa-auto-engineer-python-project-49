import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
NUMBER1 = 0
NUMBER2 = 100


def get_gcd(number1, number2):
    if number1 == 0 and number2 == 0:
        return 0

    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


def generate_round_data():
    number1 = random.randint(NUMBER1, NUMBER2)
    number2 = random.randint(NUMBER1, NUMBER2)
    question = f"{number1} {number2}"
    correct_answer = str(get_gcd(number1, number2))
    return question, correct_answer
