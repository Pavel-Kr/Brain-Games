#!/usr/bin/env python3
import brain_games.games.engine as engine
from brain_games.games.calc import generate_questions


def main():
    game_description = "What is the result of the expression?"
    questions = generate_questions()
    engine.run(game_description, questions)
