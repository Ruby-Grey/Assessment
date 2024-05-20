# Checks that users enter an integer
# that is less than (but not equal to) 6
def int_check():

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


# Main routine

# ask user what kind of maths they want

maths_type = ["Addition", "Subtraction", "Multiplication", "Division", "Mixed",]

maths_count = len(maths_type)

while True:

    print(f"What kind of maths do you want? (please enter a number from 1 to {maths_count}): ")

    maths_count = 1

    for maths in maths_type :

        print(f"{maths_count} - {maths}")

        maths_count = maths_count + 1

    user_choice = int_check()
    print(f"You chose {user_choice}")

    break
