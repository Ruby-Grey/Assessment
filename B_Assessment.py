# from typing import Any

# import random


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


# Check that users have entered a valid
# option based on a list
def int_check(question):

    while True:

        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

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


def maths_medium(question, valid_answer=("addition", "multiplication", "subtraction", "division")):
    error = f"Please enter a valid option from the following list: {valid_answer}"

    while True:

        # Get user response and make sure it's a lowercase
        user_response = input(question).lower()

        for item in valid_answer:
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

# ask user for number of rounds / infinite mode
print()
num_questions = int_check("How many questions would you like? ")

print(f"You chose {num_questions} questions.")

# ask user what kind of maths they want to do

maths_type = maths_medium(f"Please choose a type of maths: ")
print(f"You chose {maths_type}")
