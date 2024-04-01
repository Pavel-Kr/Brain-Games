from brain_games.cli import welcome_user
import prompt


def run(game_description: str, questions: list):
    user_name = welcome_user()
    print(game_description)
    for question, correct_answer in questions:
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
