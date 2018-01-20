import re


# ---------------- ONE ----------------
# 1. Add a method that is going to ask for a username :
# Need to be write with lowercase letter (a-z), number (0-9), an underscore

def askUsername():
    username = input()
    patter = re.compile('^[a-z0-9_]*$')
    if patter.search(username) != None:
        print("Good username")
    else:
        print("Error in username")


# askUsername()


# ---------------- TWO ----------------
# 2. Add a method that is going to ask for a password:
# Need to be write with lowercase letter (a-z), number (0-9), letter (A-Z)
# and the length have to be between 8 and 16 characters

def askPassword():
    pswd = input()
    patter = re.compile('^[a-zA-Z0-9]{8,16}$')
    if patter.search(pswd) != None:
        print("Good password")
    else:
        print("Error in password")


# askPassword()

# ---------------- TWO ----------------
# 3. Add a method that is going to ask for email
# Need to have the format anything@domain.com (could accept also country e.g. anything@domain.com.bo)
def askEmail():
    email = input()
    patter = re.compile('^[\w]+@[\w-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$')
    if patter.search(email) != None:
        print("Good email")
    else:
        print("Error in email")


askEmail()
