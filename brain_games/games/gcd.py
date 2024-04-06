import random
import math


game_description = "Find the greatest common divisor of given numbers."


def generate_question():
    min_number = 1
    max_number = 100
    num1 = random.randint(min_number, max_number)
    num2 = random.randint(min_number, max_number)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
