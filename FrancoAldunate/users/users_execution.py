# Module execution

from AT05_API_Test_Python_Behave.FrancoAldunate.users.calculator import *
from AT05_API_Test_Python_Behave.FrancoAldunate.users.messages import print_age_message

dict = {}


# Function: Create dictionary
def build_dictionary():
    global dict
    users_amount = int(input("Users' amount: "))
    for i in range(users_amount):
        user_name = input(f"Insert user {i + 1} name: ")
        user_age = int(input(f"Insert user {i + 1} age: "))
        dict[user_name] = user_age


# Function: Print dictionary data
def print_data():
    global dict
    for key in dict:
        print(f"User {key}, age {dict[key]}:")
        print("Age in minutes =", calculate_age_in_minutes(dict[key]))
        print("Age in hours =", calculate_age_in_hours(dict[key]))
        print("Age in days =", calculate_age_in_days(dict[key]))
        print_age_message(dict[key])
        print()


print("Execution...")
build_dictionary()
print()
print_data()
