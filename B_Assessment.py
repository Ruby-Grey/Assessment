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

    correct_answers = 0

    for i in range(num_questions):
        print(f"Question {i+1} of {num_questions}")

        got_correct_answer = ask_addition_question()
        if got_correct_answer:

            correct_answers += 1

    return correct_answers

# subtraction questions


def ask_subtraction_question():

    subtraction_answer = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number1 = subtraction_answer + number2

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

    correct_answers = 0

    for i in range(num_questions):
        print(f"Question {i + 1} of {num_questions}")

        got_correct_answer = ask_subtraction_question()
        if got_correct_answer:
            correct_answers += 1

    return correct_answers


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

    correct_answers = 0

    for i in range(num_questions):
        print(f"Question {i + 1} of {num_questions}")

        got_correct_answer = ask_multiplication_question()
        if got_correct_answer:
            correct_answers += 1

    return correct_answers


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

    correct_answers = 0

    for i in range(num_questions):
        print(f"Question {i + 1} of {num_questions}")

        got_correct_answer = ask_division_question()
        if got_correct_answer:
            correct_answers += 1

    return correct_answers


# Mixed questions (gives a random type of question each time)
def mixed_quiz():

    correct_answers = 0

    for i in range(num_questions):
        print(f"Question {i + 1} of {num_questions}")

        random_question = random.randint(0, 3)

        got_correct_answer = False

        if random_question == 0:
            got_correct_answer = ask_addition_question()

        elif random_question == 1:
            got_correct_answer = ask_subtraction_question()

        elif random_question == 2:
            got_correct_answer = ask_multiplication_question()

        elif random_question == 3:
            got_correct_answer = ask_division_question()

        if got_correct_answer:
            correct_answers += 1

    return correct_answers


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
        error3 = "ok fine then, bye"

        to_check = input(question)

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1

            if response == 0:
                print(error3)
                quit()

            elif response < 1:
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

correct_count = 0

if user_choice == 1:

    correct_count = addition_quiz()

elif user_choice == 2:

    correct_count = subtraction_quiz()

elif user_choice == 3:

    correct_count = multiplication_quiz

elif user_choice == 4:

    correct_count = division_quiz()

elif user_choice == 5:

    correct_count = mixed_quiz()

    print(f"You got {correct_count} out of {num_questions} correct!")
    if correct_count == num_questions:
        print("Nice, you got them all 😀👍")
        print()
    elif correct_count == 0:
        print("...There's room for improvement. Keep practicing! ")
        print()

# congratulates user if they got all the answers correct, and
# encourages them to keep trying if they got it all incorrect
if num_questions == correct_count:
    print("Nice, you got them all!")

elif correct_count == 0:
    print("...There's room for improvement. Keep practicing!")


# displays stats

questions_incorrect = num_questions - correct_count

# calculate statistics
percent_correct = correct_count / num_questions * 100
percent_incorrect = questions_incorrect / num_questions * 100


show_history = string_checker("Do you want to see your stats? ")
if show_history == "yes":
    print("\n📊 GAME STATISTICS 📊")
    print(f"You got {correct_count} out of {num_questions} correct!")
    print(f"👍 Correct: {percent_correct:.2f} \t")
    print(f"😢 Incorrect: {percent_incorrect:.2f} \t")

else:
    print()
    print("Thanks for attempting the quiz!")
