import unittest
from math_quiz import random_number_generator, random_operation_generator, question_maker


class TestMathGame(unittest.TestCase):

    def test_random_number_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation_generator(self):
        # Test if only addition, subtraction, and multiplication operators are generated
        acceptable = ["+", "-", "*"]
        for _ in range(1000):
            rand_operator = random_operation_generator()
            self.assertTrue(rand_operator in acceptable)

    def test_question_maker(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 1, '-', '6 - 1', 5),
                (10, 1, '*', '10 * 1', 10),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                PROBLEM, ANSWER = question_maker(num1, num2, operator)
            self.assertTrue(PROBLEM == expected_problem and ANSWER == expected_answer)
if __name__ == "__main__":
    unittest.main()
