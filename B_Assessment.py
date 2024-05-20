# def addition_question():
#
#     value1 = random.randint(1, 10)
#     value2 = random.randint(1, 10)
#     question = str(value1) + " + " + str(value2) + " = ?"

# def addition_question():
#
#     number1 = random.randint(1, 10)
#     number2 = random.randint(1, 10)
#     addition_answer = number1 + number2
#     addition_question = str(number1) + str(number2)


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
and what type of maths you would like to work with.
Answer as many as you can correct!

good luck!

    ''')


# Checks that users enter an integer
# that is less than (but not equal to) 6
# (to see what type of maths they want)
def int_check_1():

    while True:

        error = "Please enter an integer between 1 - 5"

        try:
            response = int(input("Enter an integer: "))

            # checks that the number is less than 6
            if response > 5:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Check that users have entered a valid
# option based on a list
# (to see how many questions they want
def int_check_2(question):

    while True:

        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

# Check that users have entered a valid
# option based on a list


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

maths_count = len(maths_type)


print(f"What kind of maths do you want? (please enter a number from 1 to {maths_count}): ")

maths_count = 1

for maths in maths_type :

    print(f"{maths_count} - {maths}")

    maths_count = maths_count + 1

user_choice = int_check_1()
print(f"You chose {user_choice}")


# ask user for number of rounds / infinite mode

print()
num_questions = int_check_2("How many questions do you want to answer? ")

print(f"{num_questions} questions it is!")

# Game loop starts here
while question_num < num_questions:

    rounds_heading = f"\nQuestion {question_num + 1} of {num_questions}"

    print(rounds_heading)

    break
