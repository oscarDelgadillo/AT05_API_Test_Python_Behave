def replace(words, old_word, new_word):
    """
    this function replace(words, old_word, new_word):
    that replaces all occurrences of old with new in a string
    :param words:
    :param old_word:
    :param new_word:
    :return: string
    """
    return new_word.join(words.split(old_word))


print(replace("Mississippi", "i", "I"))
print(replace("I love spom! Spom is my favorite food.Spom, spom, yum!", "o", "a"))
