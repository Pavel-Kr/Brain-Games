from brain_games.cli import welcome_user
import prompt


QUESTIONS_COUNT = 3


def run(game_module):
    user_name = welcome_user()
    game_description = game_module.DESCRIPTION
    print(game_description)
    for _ in range(QUESTIONS_COUNT):
        question, correct_answer = game_module.generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
