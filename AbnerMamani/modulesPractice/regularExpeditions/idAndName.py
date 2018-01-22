
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

#Fuction that read of the keyboard only integer
def readOnlyInteger():
    while True:
       cant = input()
       try:
            cant = int(cant)
            return cant
       except ValueError:
           print("ATTENTION: You must enter number.")

# Function to read a userID should be only numbers between 1 to 100
def readAId():
    while True:
        key = readOnlyInteger()
        if key > 0 and key < 101:
            return key
        print("Only numbers to 100 please")

# Function to read a new Value as Username should be only lowercase (nor more than 8 digits)
def readAName():
    while True:
        value = input()
        if value.islower() and len(value) < 9:
            return value
        print("only lowercase nor more than 8 digits")


#Function load the dictionary
def loadDictionary():
    global myUsers
    cant=readTheCantOfDictionari()
    for i in range(1, cant + 1):
        print(f"Plase enter the {i} Key (only integer) :")
        myKey = readAId() #input()
        print(f"Plase enter the {i} value (name) :")
        myValue = readAName()# input()
        myUsers[myKey]=myValue

#Function that is going to request to the user for a number (only 1 number) and
# need to return the amount of users that have their user ID starting with the number inserted
def usersThatHaveTheirKey():
    print("Please inter an integer: ")
    var=readOnlyInteger()
    li=[]
    for key in myUsers:
        if str(key).startswith(var):
            li.append(key)
    return li

#Function that is going to request to the user for a character (only 1 char)
# and need to return the amount of users that have their  userName starting with the character inserted
def usersThatHaveTheirValue():
    var=input()
    li=[]
    for key in myUsers:
        if str(myUsers[key]).startswith(var):
            li.append(myUsers[key])
    return li


#Function to display a message considering :
# UseID between 1-25 “User belong Group 1”
# UseID between 26-50 “User belong Group 2”
# UseID between 51-75 “User belong Group 3”
# UseID between 76-100 “User belong Group 4”
def messageOfRangeOfKey():
    for key in myUsers:
        if key in range(1,26):
            print("User belong Group 1")
        elif key in range(26,51):
            print("User belong Group 2")
        elif key in range(51,76):
            print("User belong Group 3")
        elif key in range(76,101):
            print("User belong Group 4")

#Function to print the array received
def printAlist(li):
    print(li)



loadDictionary()
printAlist(usersThatHaveTheirKey())
printAlist(usersThatHaveTheirValue())