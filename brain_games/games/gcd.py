import random
import math


def generate_questions(questions_count=3):
    questions = []
    for i in range(questions_count):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = f"{num1} {num2}"
        correct_answer = str(math.gcd(num1, num2))
        questions.append((question, correct_answer))
    return questions
