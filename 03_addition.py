import random

quiz_length = 10


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def addition_quiz():

    correct_count = 0

    for i in range(quiz_length):
        print(f"Question {i+1} of {quiz_length}")

        got_correct_answer = ask_addition_question()
        if got_correct_answer:

            correct_count += 1

    print(f"You got {correct_count} out of {quiz_length} questions right.")
    if correct_count == quiz_length:
        print("You got them alllll correct!")
    elif correct_count == 0:
        print("..There's room for improvement. Keep practicing!")
        print()


def ask_addition_question():

    number_one = random.randint(1, 10)
    number_two = random.randint(1, 10)

    correct_answer = number_one + number_two

    while True:
        user_input = input(f"   {number_one} + {number_two} = ")
        if is_integer(user_input):
            break
        else:
            print("Please only type an integer. Try again...")

    user_answer = int(user_input)

    if user_answer == correct_answer:
        print("yipee!!!!! you got it!")
        print()
        return True
    else:
        print("YOU SUCK MAN")
        print()
        return False


addition_quiz()

# sneaky trix (division. we are so smart)
answer = random.randint(1, 10)
number1 = random.randint(1, 10)
number2 = number1 * answer
