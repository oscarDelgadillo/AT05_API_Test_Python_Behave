# Practice 1
# Suppose any line of text can contain at most one url that starts with
# “http://” and ends at the next space in the line.
# Write a fragment of code to extract and print the full url if it is present.

def isUrl(inputString):
    if (inputString[0:7] == "http://") and inputString.find(" ") == len(inputString) - 1:
        return True
    else:
        return False


print("1. Determine if a Url is valid or not:")
print(isUrl("http://www.google.com "))
print(isUrl("http://www.google.com.bo  "))
print(isUrl("http://www.google.com"))
print(isUrl("htp://www.google.com "))
print()


# Practice 2
# Write a function replace(s, old, new) that replaces all occurrences of old
# with new in a string s:
def replaceWords(s, old, new):
    list = s.split(old)
    result = new.join(list)
    return result


print("2. Replace ocurrences of old with new in a string:")
print(replaceWords("23.414.123..231", ".", ","))
print(replaceWords("23.414.123..231", "3", "three"))
print(replaceWords("Missisipi", "i", "I"))
print(replaceWords("I love spom! Spom is my favorite food.Spom, spom, yum!", "om", "am"))
print(replaceWords("I love spom! Spom is my favorite food.Spom, spom, yum!", "o", "a"))
print()


# Practice 3
# Write a program that reads a string and returns a table of the letters of the alphabet
# in alphabetical order which occur in the string together with the number of times
#  each letter occurs.
# - Case should be ignored. A sample output of the program when the user enters the data

def dictionaryBuilder(inputString):
    dict = {}
    stringInLowerCase = inputString.lower()
    for i in stringInLowerCase:
        if i != " ":
            occurrences = stringInLowerCase.count(i)
            dict[i] = occurrences
    for key in sorted(dict):
        print(key, dict[key])


print("3. Generate a dictionary from string:")
dictionaryBuilder("ThiS is String with Upper and lower case Letters")
