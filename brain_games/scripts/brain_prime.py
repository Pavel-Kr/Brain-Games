from brain_games.games.prime import generate_questions
import brain_games.games.engine as engine


def main():
    game_description = 'Answer "yes" if given number '\
        'is prime. Otherwise answer "no".'
    questions = generate_questions()
    engine.run(game_description, questions)
