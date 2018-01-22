# Write a function replace(s, old, new) that replaces all occurrences of old with new in a string s:

print('---------------- FUNCTION REPLACE ----------------')
# replace("Mississippi", "i", "I") == "MIssIssIppI"
# replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam,spam, yum!"
# replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam,spam, yum!"

cad = "Mississippi"
song = "I love spom! Spom is my favorite food.Spom, spom, yum!"


def replace(cad, oldLetter, newLetter):
    cad = cad.split(oldLetter)
    return newLetter.join(cad)


print(replace(cad, 'i', 'I'))
print(replace(song, 'om', 'am'))
print(replace(song, 'o', 'a'))
