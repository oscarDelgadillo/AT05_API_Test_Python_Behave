import re

def readNameOfUser():
    while True:
        print("Please enter a name")
        var =input()
        patron = re.compile('^[a-z0-9]*$')
        if not patron.match(var) == "None":
            return var
        print("Please enter a name")


def readPasswordOfUser():
    while True:
        print("Please enter a password")
        var =input()
        patron = re.compile('^[a-z0-9A-Z]{8,16}$')
        if not patron.match(var) == "None":
            return var
        print("Please enter a password")

def readEmailOfUser():
    while True:
        print("Please enter a email")
        var = input()
        patron = re.compile('^[\w]+@[\w-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$')
        if not patron.match(var) == "None":
            return var
        print("Please enter a email")


# print(readNameOfUser())
print(readEmailOfUser())