import random


def generate_questions(questions_count=3):
    questions = []
    for i in range(questions_count):
        num = random.randint(1, 100)
        is_even = num % 2 == 0
        question = str(num)
        correct_answer = is_even and "yes" or "no"
        questions.append((question, correct_answer))
    return questions
