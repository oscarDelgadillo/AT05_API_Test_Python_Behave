# ---------------- ONE ----------------
# 1. Function that will create a dictionary with a list of userID and userName,
# the userID should be only numbers between 1 to 100.
# Username should be only lowercase (nor more than 8 digits)

def createDictionary():
    dict = {}
    print("Insert the quantity of elements in the dictionary: ", end='')
    quantity = int(input())
    for x in range(0, quantity):
        print("Enter user id: ", end='')
        userID = int(input())
        print("Enter user name: ", end='')
        username = input()
        if userID > 0 and userID <= 100:
            if (len(username) <= 8 and username.islower()):
                dict[userID] = username
            else:
                print("Error with the username. Username should be only lowercase (nor more than 8 digits)")
        else:
            print("Error with the userID. Range of userID [0-100]")
    return dict


users = createDictionary()


# print(createDictionary())


# ---------------- TWO ----------------
# 2. Function that is going to request to the user for a number (only 1 number)
# and need to return the amount of users that have their user ID starting with
# the number inserted (E.g. if user inserted 1, then could count all users
# with 1, 10,11,12,13..19 or 100), return and array with the user_ID that fulfilled this condition

def requestUserID(dict, number):
    list = []
    for key in dict:
        if (str(key).startswith(str(number))):
            list.append(key)
    return list


print('UserIDs: ', requestUserID(users, 1))


# ---------------- THREE ----------------
# 3. Function that is going to request to the user for a character (only 1 char)
# and need to return the amount of users that have their  userName starting with the character inserted
# (E.g. if user inserted a, then could count all users that start with a),
# return and array with the list of userName that fulfilled this condition

def requestUsername(dict, char):
    list = []
    for key in dict:
        if dict[key].startswith(char):
            list.append(dict[key])
    return list


print('Usernames: ', requestUsername(users, 'a'))

# ---------------- FOUR ----------------
# 4. Function to display a message considering :
# UseID between 1-25 "User belong Group 1"
# UseID between 26-50 "User belong Group 2"
# UseID between 51-75 "User belong Group 3"
# UseID between 76-100 "User belong Group 4"
# Consider to use Case Equality

def displayMessage(dict):
    for key in dict:
        if key >= 1 and key <=25:
            print("UserID[{0}] - User belong Group 1".format(key))
        elif key >= 26 and key <=50:
            print("UserID[{0}] - User belong Group 2".format(key))
        if key >= 51 and key <= 75:
            print("UserID[{0}] - User belong Group 3".format(key))
        elif key >= 76 and key <= 100:
            print("UserID[{0}] - User belong Group 4".format(key))

displayMessage(users)

