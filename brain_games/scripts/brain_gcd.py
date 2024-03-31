#!/usr/bin/env python3
import brain_games.games.engine as engine
from brain_games.games.gcd import generate_questions


def main():
    game_description = "Find the greatest common divisor of given numbers."
    questions = generate_questions()
    engine.run(game_description, questions)
