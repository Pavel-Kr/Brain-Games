import random
import math


DESCRIPTION = 'Answer "yes" if given number '\
    'is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 100


def is_prime(num: int):
    if num <= 1:
        return False
    elif num == 2:
        return True
    i = 2
    while i <= math.ceil(math.sqrt(num)):
        if num % i == 0:
            return False
        i += 1
    return True


def generate_question():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(num)
    correct_answer = is_prime(num) and 'yes' or 'no'
    return question, correct_answer
