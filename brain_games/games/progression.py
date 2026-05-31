import random

DESCRIPTION = 'What number is missing in the progression?'
MIN_LEN = 5
MAX_LEN = 10
MIN_NUMBER = 1
MAX_NUMBER = 50
MIN_STEP = 1
MAX_STEP = 20


def generate_progression(start, step, length):
    progression = []
    for index in range(length):
        current_element = start + index * step
        progression.append(str(current_element))
    return progression


def generate_round_data():
    len_progression = random.randint(MIN_LEN, MAX_LEN)
    start = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = generate_progression(start, step, len_progression)
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = " ".join(progression)
    return question, correct_answer