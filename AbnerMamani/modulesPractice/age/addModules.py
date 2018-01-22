#Import two modules
from calculateAge import *
from messageAccordingAge import messageAccordingTheAge
myUsers={}

#This function Read a values integer of the keyboard
def readTheAmountOfUsers():
    while True:
        print("Please enter the amount of users:")
        cant=input()
        try:
            cant = int(cant)
            return cant
        except ValueError:
            print("ATTENTION: You must enter a whole number.")


#Function load the dictionary with name and age of the users.
def loadDictionary():
    global myUsers
    cant=readTheAmountOfUsers()
    for i in range(1, cant + 1):
        print(f"Plase enter the {i} Name of the User :")
        myKey = input()
        print(f"Plase enter the {i} Age of the User :")
        myValue = input()
        myUsers[myKey]=myValue


#Function that print details
def printDetails():
    for key in myUsers:
       age= myUsers[key]
       age=int(age)
       # print (key +" "+ str(age))
       print(f" {key}: age:{age} "
             f"in Minites: {calculateAgleToMinutes(age)}, in Huors: {calculateAgleToHours(age)}, in Days: {calculateAgleToDays(age)}"
             f" and this is: {messageAccordingTheAge(age)}" )


#use of the functions
loadDictionary()
printDetails()