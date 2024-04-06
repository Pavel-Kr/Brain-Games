import random


game_description = 'Answer "yes" if the number is '\
    'even, otherwise answer "no".'


def generate_question():
    min_number = 1
    max_number = 100
    num = random.randint(min_number, max_number)
    is_even = num % 2 == 0
    question = str(num)
    correct_answer = is_even and "yes" or "no"
    return question, correct_answer
