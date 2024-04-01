import random
import math


def is_prime(num: int):
    if num == 2:
        return True
    i = 2
    while i <= math.ceil(math.sqrt(num)):
        if num % i == 0:
            return False
        i += 1
    return True


def generate_questions(questions_count=3):
    questions = []
    for i in range(questions_count):
        num = random.randint(2, 100)
        question = str(num)
        correct_answer = is_prime(num) and "yes" or "no"
        questions.append((question, correct_answer))
    return questions
