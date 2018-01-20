# Module that calcule age in minites, hours and days

#Function that calcule age in minites
def calculateAgleToMinutes(age):
    return calculateAgleToHours(age) * 60

#Function that calcule age in hours
def calculateAgleToHours(age):
    return calculateAgleToDays(age)* 24

#Function that calcule age in days
def calculateAgleToDays(age):
    return age * 365


# print (calculateAgleToDays(10))
# print (calculateAgleToHours(10))
# print (calculateAgleToMinutes(10))