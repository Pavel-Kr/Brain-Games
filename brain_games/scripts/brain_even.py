#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random
import prompt


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts_count = 3
    for i in range(attempts_count):
        num = random.randint(1, 100)
        is_even = num % 2 == 0
        correct_answer = is_even and "yes" or "no"
        print(f"Question: {num}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
