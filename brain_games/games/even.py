import random


DESCRIPTION = 'Answer "yes" if the number is '\
    'even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    is_even = num % 2 == 0
    question = str(num)
    correct_answer = is_even and 'yes' or 'no'
    return question, correct_answer
