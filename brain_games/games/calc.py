import random


def generate_questions(questions_count=3):
    operations = "+-*"
    questions = []
    for i in range(questions_count):
        left_op = random.randint(1, 50)
        right_op = random.randint(1, 50)
        operation = random.choice(operations)
        # Just to make the game a little bit easier
        # (Imagine counting something like 48 * 23 in your head...)
        if operation == "*":
            left_op //= 2
            right_op //= 2
        question = f"{left_op} {operation} {right_op}"
        correct_answer = str(eval(question))
        questions.append((question, correct_answer))
    return questions
