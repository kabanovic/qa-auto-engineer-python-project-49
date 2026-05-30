import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(game_description, get_round_data):
    print("Welcome to the Brain Games!")
    name = welcome_user_and_get_name()
    print(game_description)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_round_data()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


def welcome_user_and_get_name():
    return welcome_user()
