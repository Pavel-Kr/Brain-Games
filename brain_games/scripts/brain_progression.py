from brain_games.games.progression import generate_questions
import brain_games.games.engine as engine


def main():
    game_description = "What number is missing in the progression?"
    questions = generate_questions()
    engine.run(game_description, questions)
