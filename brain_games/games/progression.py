import random


def generate_questions(questions_count=3):
    questions = []
    for i in range(questions_count):
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
        questions.append((question, correct_answer))
    return questions
