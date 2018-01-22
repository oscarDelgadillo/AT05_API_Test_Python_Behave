# Module messages

MINUS_ONE = -1
TWELVE = 12
EIGHTEEN = 18
THIRTY = 30


# Function: Print person'age message
def print_age_message(age: int):
    if MINUS_ONE < age <= TWELVE:
        print("You are a child, when the age is lower than 12")
    elif TWELVE < age < EIGHTEEN:
        print("Your are teenager, when the age is between 13 and 17")
    elif EIGHTEEN <= age < THIRTY:
        print("You are young, when the age is between 18 and 29")
    elif age >= THIRTY:
        print("You are adult, when the age is greater than 30")
