import random


DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 25
OPERATIONS = ['+', '-', '*']


def generate_question():
    left_op = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_op = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)

    question = f'{left_op} {operation} {right_op}'

    if operation == '+':
        correct_answer = left_op + right_op
    elif operation == '-':
        correct_answer = left_op - right_op
    elif operation == '*':
        correct_answer = left_op * right_op

    correct_answer = str(correct_answer)
    return question, correct_answer
