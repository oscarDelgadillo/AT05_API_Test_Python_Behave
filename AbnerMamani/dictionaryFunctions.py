#Dictionary Pactice

#This dictionary variable isn gloval
myUsers={}

#This function Read a values integer of the keyboard
def readTheCantOfDictionari():
    while True:
        print("Please enter the number of items in your Dictionary")
        cant=input()
        try:
            cant = int(cant)
            return cant
        except ValueError:
            print("ATTENTION: You must enter a whole number.")

#Function load the dictionary without same values and keys
def loadDictionary():
    global myUsers
    cant=readTheCantOfDictionari()
    for i in range(1, cant + 1):
        print(f"Plase enter the {i} Key :")
        myKey = readAnewKey() #input()
        print(f"Plase enter the {i} value :")
        myValue = readANewValue()# input()
        myUsers[myKey]=myValue

#Function to print the dictionary keys
def printDictionaryKey():
    print(myUsers.keys())

#Function to print the dictionary values
def printDictionaryValues():
    print(myUsers.values())

#Function to print the dictionary
def printDictionary():
    print(myUsers)

#Function to define is a key inserted by the user, exists on the dictionary.
def keyExistsInDictionary(k):
    if k in myUsers.keys():
        return True
    else:
        return False

#Function to define is a value inserted by the user, exists on the dictionary.
def valueExistsInDictionary(va):
    if va in myUsers.values():
        return True
    else:
        return False
#Function to read a new Key and verify is already exists
def readAnewKey():
    while True:
        key=input()
        if keyExistsInDictionary(key):
            print("The key already exists")
        else:
            return key

#Function to read a new Value and verify is already exists
def readANewValue():
    while True:
        value=input()
        if valueExistsInDictionary(value):
            print("The value already exists")
        else:
            return value

#Use of the functions
loadDictionary()
printDictionaryKey()
printDictionaryValues()
printDictionary()
