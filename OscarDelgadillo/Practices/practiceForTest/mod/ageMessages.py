def getAgeMessage(age):
    if age <= 12:
        print("You are a child")
    elif age >= 13 and age <= 17:
        print("Your are teenager")
    elif age >= 18 and age <= 29:
        print("You are young")
    elif age >= 30:
        print("You are adult")