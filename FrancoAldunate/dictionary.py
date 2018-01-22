# Module dictionary
dict = {}


# 1. Function: Create Dictionary
def build_dictionary():
    global dict
    dict_lenght = int(input("Dictionary length: "))
    for i in range(dict_lenght):
        print(f"Element {i + 1}:")
        key = input("Insert key: ")
        value = input("Insert value: ")
        dict[key] = value


# 2. Function: Print Dictionary Keys
def print_dictionary_keys():
    global dict
    list = []
    separator = ","
    for key in dict:
        list.append(key)
        separator.join(list)
    print("Dictionary keys:", list)


# 3. Function: Print Dictionary Values
def print_dictionary_values():
    global dict
    list = []
    separator = ","
    for key in dict:
        list.append(dict[key])
    separator.join(list)
    print("Dictionary values:", list)


# 4. Function: Print Dictionary
def print_dictionary():
    global dict
    list = []
    separator = ","
    for key in dict:
        list.append(f"{key} : {dict[key]}")
    separator.join(list)
    print("Dictionary:", list)


# 5. Function: Find Dictionary Key
def find_key():
    global dict
    key = input("Find key: ")
    return key in dict.keys()


# 6. Function: Find Dictionary Value
def find_value():
    global dict
    value = input("Find value: ")
    return value in dict.values()


# Execution
print("Executing of functions...")
print()
build_dictionary()
print_dictionary_keys()
print_dictionary_values()
print_dictionary()
print(find_key())
print(find_value())
