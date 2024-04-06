import random


game_description = "What number is missing in the progression?"


def generate_question():
    progression_len = 10
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    elem = start
    missing_elem = random.randint(0, progression_len - 1)
    progression = []
    for j in range(progression_len):
        if j == missing_elem:
            progression.append("..")
            correct_answer = str(elem)
        else:
            progression.append(str(elem))
        elem += step
    question = " ".join(progression)
    return question, correct_answer
