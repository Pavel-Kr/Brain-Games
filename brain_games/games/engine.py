from brain_games.cli import welcome_user
import prompt


def generate_questions(game_module):
    questions = []
    questions_count = 3
    for i in range(questions_count):
        question = game_module.generate_question()
        questions.append(question)
    return questions


def run(game_module):
    user_name = welcome_user()
    game_description = game_module.game_description
    print(game_description)
    questions = generate_questions(game_module)
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
