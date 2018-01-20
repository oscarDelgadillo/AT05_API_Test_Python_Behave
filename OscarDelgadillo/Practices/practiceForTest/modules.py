print("---------------- ONE ----------------")
# 1. Create 1 module to Calculate age in minutes, hours and days
import mod.calculateAge
import mod.ageMessages

print("Insert the age: ", end='')
age = int(input())
mod.calculateAge.calculateAge(age)

print("---------------- TWO ----------------")
# 2. Create 1 module to print 4 different messages :
# You are a child, when the age is lower than 12
# Your are teenager, when the age is between 13 and 17
# You are young, when the age is between 18 and 29
# You are adult, when the age is greater than 30

mod.ageMessages.getAgeMessage(age)

print("---------------- THREE ----------------")


# 3.Create a script importing both modules and performing de action :
# Ask to the user the amount of users
# For all users define the name and the age for each one, save this data as a dictionary
# After all users are defined, need to :
# print the age in minutes, hours and days
# The expected message according the age define

def createUsersInDictionary():
    dict = {}
    print("Insert the quantity of users: ", end='')
    quantity = int(input())
    for x in range(0, quantity):
        print("Insert name: ", end='')
        name = input()
        print("Insert age: ", end='')
        age = int(input())
        dict[name] = age
    return dict


def printData(dict):
    for key in dict:
        print("[{0}]".format(key))
        mod.calculateAge.calculateAge(dict[key])
        mod.ageMessages.getAgeMessage(dict[key])

    print(end='\n')


printData(createUsersInDictionary())
