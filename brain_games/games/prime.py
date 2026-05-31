import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 50


def is_prime(number):
    if number < 2:
        return False
    divider = 2
    while divider * divider <= number:
        if number % divider == 0:
            return False
        divider += 1
    return True


def generate_round_data():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer