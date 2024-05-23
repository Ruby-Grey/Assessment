import random


# checks that a user's input is an integer
def int_check(string):

    try:
        int(string)
        return True
    except ValueError:
        return False


# addition questions
def ask_addition_question():

    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    addition_answer = number1 + number2

    while True:
        user_input = input(f"{number1} + {number2} = ")
        if int_check(user_input):
            break
        else:
            "Please enter an integer! Try again..."

    user_answer = int(user_input)

    if user_answer == addition_answer:
        print("You got it!")
        print()
        return True

    else:
        print(f"incorrect! D: (The answer was {addition_answer})")
        print()
        return False


def addition_quiz():

    correct_count = 0

    for i in range(num_questions):
        print(f"Question {i+1} of {num_questions}")

        got_correct_answer = ask_addition_question()
        if got_correct_answer:

            correct_count += 1

    print(f"You got {correct_count} out of {num_questions} correct!")
    if correct_count == num_questions:
        print("Nice, you got them all 😀👍")
        print()
    elif correct_count == 0:
        print("...There's room for improvement. Keep practicing! ")
        print()


# subtraction questions

def ask_subtraction_question():

    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    subtraction_answer = number1 - number2

    while True:

        user_input = input(f"{number1} - {number2} = ")
        if int_check(user_input):
            break
        else:
            print("Please enter an integer! Try again...")

    user_answer = int(user_input)

    if user_answer == subtraction_answer:
        print("You got it!")
        print()
        return True

    else:
        print(f"incorrect! D: (The answer was {subtraction_answer})")
        print()
        return False


def subtraction_quiz():

    correct_count = 0

    for i in range(num_questions):
        print(f"Question {i + 1} of {num_questions}")

        got_correct_answer = ask_subtraction_question()
        if got_correct_answer:
            correct_count += 1

    print(f"You got {correct_count} out of {num_questions} correct!")
    if correct_count == num_questions:
        print("Nice, you got them all 😀👍")
        print()
    elif correct_count == 0:
        print("...There's room for improvement. Keep practicing! ")
        print()


# multiplication questions

def ask_multiplication_question():

    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    multiplication_answer = number1 * number2

    while True:

        user_input = input(f"{number1} x {number2} = ")
        if int_check(user_input):
            break
        else:
            print("Please enter an integer! Try again...")

    user_answer = int(user_input)

    if user_answer == multiplication_answer:
        print("You got it!")
        print()
        return True

    else:
        print(f"incorrect! D: (The answer was {multiplication_answer})")
        print()
        return False


def multiplication_quiz():

    correct_count = 0

    for i in range(num_questions):
        print(f"Question {i + 1} of {num_questions}")

        got_correct_answer = ask_multiplication_question()
        if got_correct_answer:
            correct_count += 1

    print(f"You got {correct_count} out of {num_questions} correct!")
    if correct_count == num_questions:
        print("Nice, you got them all 😀👍")
        print()
    elif correct_count == 0:
        print("...There's room for improvement. Keep practicing! ")
        print()


# division questions

def ask_division_question():

    division_answer = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number1 = division_answer * number2

    while True:

        user_input = input(f"{number1} ÷ {number2} = ")
        if int_check(user_input):
            break
        else:
            print("Please enter an integer! Try again...")

    user_answer = int(user_input)

    if user_answer == division_answer:
        print("You got it!")
        print()
        return True

    else:
        print(f"incorrect! D: (The answer was {division_answer})")
        print()
        return False


def division_quiz():

    correct_count = 0

    for i in range(num_questions):
        print(f"Question {i + 1} of {num_questions}")

        got_correct_answer = ask_division_question()
        if got_correct_answer:
            correct_count += 1

    print(f"You got {correct_count} out of {num_questions} correct!")
    if correct_count == num_questions:
        print("Nice, you got them all 😀👍")
        print()
    elif correct_count == 0:
        print("...There's room for improvement. Keep practicing! ")
        print()

# mixed questions


# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's a lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if the user does not enter something that is valid
        print(error)
        print()


# displays instructions
def instruction():
    print('''

**** Instructions ****

Welcome to my maths quiz! 
Here you will choose how many questions you want to answer, 
and what type of maths you would like to work out.
Answer as many as you can correct!

good luck!

    ''')


# Checks that users enter an integer
# that is less than (but not equal to) 6
# (to see what type of maths they want)
def get_quiz_choice():

    while True:

        error = "Please enter an integer between 1 - 5"

        try:
            response = int(input("Enter an integer: "))

            # checks that number is above 1
            if response < 1:
                print(error)
                print()

            # checks that the number is less than 6
            elif response > 5:
                print(error)
                print()

            else:
                return response

        except ValueError:
            print(error)
            print()


# Check that users have entered a valid
# option based on a list
# (to see how many questions they want)
def get_question_amount(question):

    while True:

        error1 = "Please enter an integer that is between 1-50!"
        error2 = "...Maybe that's a bit too many (the limit is 50)"

        to_check = input(question)

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error1)
                print()

            # checks the number is below 50
            elif response > 50:
                print(error2)
                print()

            else:
                return response

        except ValueError:
            print(error1)
            print()


# Main routine

# Initialise game variables
question_num = 0
questions_correct = 0
questions_incorrect = 0

print()
print("👍 Ruby's maths quiz 👍")
print()

# ask user if they want to see the instructions and display
# them if required
want_instructions = string_checker("Would you like to read the instructions? ")

# Checks users enter yes(y) or no (n)
if want_instructions == "yes":
    instruction()


# ask user what kind of maths they want

maths_type = ["Addition", "Subtraction", "Multiplication", "Division", "Mixed",]

# lists the options (counts the number of options)
maths_count = len(maths_type)

print(f"What kind of maths do you want? (please enter a number from 1 to {maths_count}): ")

maths_count = 1

for maths in maths_type:

    print(f"{maths_count} - {maths}")

    maths_count = maths_count + 1

user_choice = get_quiz_choice()

# prints out the name of the maths type rather than the number
quiz_index = user_choice - 1
quiz_name = maths_type[quiz_index]

print(f"You chose {quiz_name}")


# ask user for number of questions

print()
num_questions = get_question_amount("How many questions do you want to answer? ")

# Game loop starts here

print("Test begin!")
print()

if user_choice == 1:

    addition_quiz()

elif user_choice == 2:

    subtraction_quiz()

elif user_choice == 3:

    multiplication_quiz()

elif user_choice == 4:

    division_quiz()

elif user_choice == 5:

    print("MIXED")
