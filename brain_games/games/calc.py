import random

DESCRIPTION = 'What is the result of the expression?'
NUMBER1 = 1
NUMBER2 = 40
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
    number1 = random.randint(NUMBER1, NUMBER2)
    number2 = random.randint(NUMBER1, NUMBER2)
    operator = random.choice(OPERATORS)
    question = f"{number1} {operator} {number2}"
    correct_answer = str(calculate(number1, number2, operator))
    return question, correct_answer
