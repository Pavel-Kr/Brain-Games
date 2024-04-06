import random
import math


game_description = 'Answer "yes" if given number '\
    'is prime. Otherwise answer "no".'


def is_prime(num: int):
    if num == 2:
        return True
    i = 2
    while i <= math.ceil(math.sqrt(num)):
        if num % i == 0:
            return False
        i += 1
    return True


def generate_question():
    min_number = 2
    max_number = 100
    num = random.randint(min_number, max_number)
    question = str(num)
    correct_answer = is_prime(num) and "yes" or "no"
    return question, correct_answer
