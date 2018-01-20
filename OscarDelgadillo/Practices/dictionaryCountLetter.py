# Write a program that reads a string and returns a table of the letters of the alphabet in
# alphabetical order which occur in the string together with the number of times each letter occurs.

print('---------------- COUNTER LETTERS WITH DICTIONARY ----------------')

string = "ThiS is String with Upper and lower case Letters"


def countLetter(string):
    dict = {}
    for letter in string.lower():
        if letter != ' ':
            dict[letter] = string.count(letter)
    return sorted(dict.items())


print(string)
print(countLetter(string))
