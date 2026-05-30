import random

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 40
OPERATORS = ["+", "-", "*"]


def calculate(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case _:
            raise ValueError(f"Неизвестный оператор: {operator}")


def generate_round_data():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)
    question = f"{number1} {operator} {number2}"
    correct_answer = str(calculate(number1, number2, operator))
    return question, correct_answer
