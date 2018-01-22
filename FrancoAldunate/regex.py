# Module regex

import re


# Function: Validate user_name with lowercase letter (a-z), number (0-9), an underscore
def validate_user_name():
    pattern = re.compile('^[a-z0-9_]+$')
    user_name = input("Insert user_name: ")
    return pattern.search(user_name) != None


# Function: Validate user_name with lowercase letter (a-z), number (0-9), letter (A-Z)
# and the length have to be between 8 and 16 characters
def validate_user_password():
    pattern = re.compile('^[a-zA-Z0-9]{8,16}$')
    user_password = input("Insert user_password: ")
    return pattern.search(user_password) != None


# Function: Validate user_email with format anything@domain.com
# (could accept also country e.g. anything@domain.com.bo)
def validate_user_email():
    pattern = re.compile('^[\w]+@[\w-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$')
    user_email = input("Insert user_email: ")
    return pattern.search(user_email) != None


print("Execution...")
print(validate_user_name())
print()
print(validate_user_password())
print()
print(validate_user_email())
