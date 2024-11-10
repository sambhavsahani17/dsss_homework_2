import random

def random_number_generator(min: int, max: int) -> int:
    """
    Function to generate a random integer within a give range.

    Args:
        min (int): The minimum integer the function should return.
        max (int): The maximum integer the function should return.
    
    Returns:
        int: A random integer between min and max, including min and max. 
    
    Raises:
        TypeError: If 'min' or 'max' are not integers.
        ValueError: If 'min' > 'max'.

    Examples:
        >>> random_number_generator(1, 4)
        3
        >>> random_number_generator(1, 4)
        1
    """
    if isinstance(min, int) == False:
        raise TypeError(f"Argument 'min' should be of type int, but got type {type(min).__name__}.")
    if isinstance(max, int) == False:
        raise TypeError(f"Argument 'max' should be of type int, but got type {type(max).__name__}.")
    if min > max:
        raise ValueError(f"Argument 'min' should be <= argument 'max'.")
    return random.randint(min, max)

def random_operation_generator() -> str:
    """
    Function to select a random operation, '+' addition, '-' subtraction, or '*' multiplication. 

    Returns:
        str: The symbol corresponding to the operation.
    
    Examples:
        >>> random_operation_generator()
        '+'
        >>> random_operation_generator()
        '-'
        >>> random_operation_generator()
        '*'
    """
    return random.choice(['+', '-', '*'])


def calculate(first_number: int, second_number: int, operation: str) -> tuple[str, int]:
    """
    This function, based on the given numbers and opeartion, returns a formatted question which can be displayed to the user for math quiz.
    Along with the formatted question, it also returns the correct answer.

    Args:
        first_number (int) : The first of the two numbers between which the given operation is performed.
        second_number (int) : The second of the two numberes between which the given operation is performed.
        operation (str) : The operation which is to be performed beween the two given numbers.

    Returns:
        tuple(str, int): A tuple whose first element is a string which contains the formatted question which can be displayed to the user
        and the second element contains the right answer of the quiz.

    Examples:
        >>> calculate(1, 2, "+")
        ('1 + 2', 3)
        >>> calculate(1, 2, "-")
        ('1 - 2', -1)
        >>> calculate(3, 2, "*")
        ('3 * 2', 6)
    """
    PROBLEM = f"{first_number} {operation} {second_number}"
    if operation == '+': ANSWER = first_number + second_number
    elif operation == '-': ANSWER = first_number - second_number
    else: ANSWER = first_number * second_number
    return PROBLEM, ANSWER 

def math_quiz() -> None:
    score = 0
    total_questions = 3

    if isinstance(total_questions, int) == False:
        raise TypeError(f"variable total_questions should be of type int, instead got type {type(total_questions).__name__}.")

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        first_number = random_number_generator(1, 5); second_number = random_number_generator(1, 5); operation = random_operation_generator()

        PROBLEM, ANSWER = calculate(first_number, second_number, operation)

        # in case of ValueError, allowing the user to retry up to max_error times assuming a typo was made
        error_count = 0
        max_error = 3
        while error_count < max_error:
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            try:
                useranswer = int(useranswer)
                break
            except ValueError:
                if error_count < max_error - 1:
                    print("You seem to have made a type. The answer can obviously only be an integer.")
                    print(f"I am going to be grateful and let you try {max_error - error_count - 1} more time/s.")
                error_count += 1

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()