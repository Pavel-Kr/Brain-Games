#!/usr/bin/env python3
import brain_games.games.engine as engine
from brain_games.games.even import generate_questions


def main():
    game_description = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = generate_questions()
    engine.run(game_description, questions)
