dict = {}


# ---------------- ONE ----------------
# 1. Function to create the dictionary, the Function should ask for the length of the dictionary
#    According the length defined should ask to the user for the key and for 	the value.

def askElementsIntoDictionary():
    print("Insert the quantity of elements in the dictionary: ", end='')
    quantity = int(input())
    global dict
    for x in range(0, quantity):
        print("Insert key: ", end='')
        key = input()
        print("Insert value: ", end='')
        value = input()
        dict.update({key: value})


askElementsIntoDictionary()


# ---------------- TWO ----------------
# 2. Function to print the dictionary keys

def printKeysOfDictionary():
    print("Keys = ", end='')
    for key in dict:
        print("[{0}]".format(key), end='')
    print(end='\n')


printKeysOfDictionary()


# ---------------- THREE ----------------
# 3. Function to print the dictionary values

def printValuesOfDictionary():
    print("Values = ", end='')
    for key in dict:
        print("[{0}]".format(dict[key]), end='')
    print(end='\n')


printValuesOfDictionary()


# ---------------- FOUR ----------------
# 4. Function to print the dictionary

def printDictionary():
    print("Dictionary = {0}".format(dict))


printDictionary()


# ---------------- FIVE ----------------
# 5. Function to define is a key inserted by the user, exists on the dictionary

def validateKeyInDictionary():
    print("Search key: ", end='')
    key = input()
    if key in dict.keys():
        print("The key '{0}' exist in the dictinary".format(key))
    else:
        print("The key '{0}' doesn't exist in the dictinary".format(key))


validateKeyInDictionary()


# ---------------- SIX ----------------
# 6. Function to define is a value inserted by the user, exists on the dictionary.

def validateValueInDictionary():
    print("Search value: ", end='')
    value = input()
    if value in dict.values():
        print("The value '{0}' exist in the dictinary".format(value))
    else:
        print("The value '{0}' doesn't exist in the dictinary".format(value))


validateValueInDictionary()

# ---------------- SEVEN ----------------
# 7. Use the dictionary as a Global variable to be used in all functions.
