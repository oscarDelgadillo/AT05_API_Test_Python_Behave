def dictionary(words):
    """
    This function reads a string and returns a table of the letters
    of the alphabet in alphabetical order which occur in the string
    together with the number of times each letter occurs.
    :param words:
    :return:  map_result table of the letters
    """
    list_data = words.replace(" ", "").lower()
    map_result = {}
    for key in list_data:
        map_result[key] = list_data.count(key)
    return sorted(map_result.items())


string_data = "ThiS is String with Upper and lower case Letters"
map_data = dictionary(string_data)
for key_value in map_data:
    print(key_value)
