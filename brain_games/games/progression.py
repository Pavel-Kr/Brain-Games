import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LEN = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 5


def generate_question():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    elem = start
    missing_elem = random.randint(0, PROGRESSION_LEN - 1)
    progression = []
    for j in range(PROGRESSION_LEN):
        if j == missing_elem:
            progression.append('..')
            correct_answer = str(elem)
        else:
            progression.append(str(elem))
        elem += step
    question = ' '.join(progression)
    return question, correct_answer
