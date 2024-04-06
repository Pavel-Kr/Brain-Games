import random


game_description = "What is the result of the expression?"


def generate_question():
    min_number = 1
    max_number = 50
    operations = "+-*"
    left_op = random.randint(min_number, max_number)
    right_op = random.randint(min_number, max_number)
    operation = random.choice(operations)
    # Just to make the game a little bit easier
    # (Imagine counting something like 48 * 23 in your head...)
    if operation == "*":
        left_op //= 2
        right_op //= 2
    question = f"{left_op} {operation} {right_op}"
    correct_answer = str(eval(question))
    return question, correct_answer
