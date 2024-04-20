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
    stop = start + step * PROGRESSION_LEN
    progression = list(map(str, range(start, stop, step)))
    missing_elem = random.randint(0, PROGRESSION_LEN - 1)
    correct_answer = progression[missing_elem]
    progression[missing_elem] = '..'
    question = ' '.join(progression)
    return question, correct_answer
