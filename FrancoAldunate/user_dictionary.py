# Module user_dictionary

ZERO = 0
TWENTY_FIVE = 25
TWENTY_SIX = 26
FIFTY = 50
FIFTY_ONE = 51
SEVENTY_FIVE = 75
SEVENTY_SIX = 76
ONE_HUNDRED = 100
dict = {}


# Function: Create dictionary
def create_dictionary():
    global dict
    flag = True
    while flag:
        print()
        response = input("Insert user? Yes: y, No: n ")
        if response.lower() == "n":
            flag = False
        elif response.lower() == "y":
            user_id = int(input("Insert user_id: "))
            user_name = input("Insert user_name: ")
            if 0 < user_id < 101 and len(user_name) < 9:
                dict[user_id] = user_name
            else:
                print("user_id or user_name is out of range")
                continue


# Function: Find user_id occurrences that start with a given number
def find_user_id_occurrences():
    global dict
    user_id_list = []
    number = int(input("Insert a number: "))
    for key in dict.keys():
        if str(key).startswith(str(number)):
            user_id_list.append(key)
    return user_id_list


# Function: Find user_name occurrences that start with a given character
def find_user_name_occurrences():
    global dict
    user_name_list = []
    character = input("Insert a character: ")
    for key in dict:
        if dict[key].startswith(character):
            user_name_list.append(dict[key])
    return user_name_list


# Function: Display user_id group
def display_user_id_group():
    global dict
    for key in dict:
        if ZERO < key < TWENTY_SIX:
            print(f"User {dict[key]} belongs to Group 1")
        elif TWENTY_FIVE < key < FIFTY_ONE:
            print(f"User {dict[key]} belongs to Group 2")
        elif FIFTY < key < SEVENTY_SIX:
            print(f"User {dict[key]} belongs to Group 3")
        elif SEVENTY_FIVE < key <= ONE_HUNDRED:
            print(f"User {dict[key]} belongs to Group 4")


print("Execution...")
create_dictionary()
print()
print(find_user_id_occurrences())
print()
print(find_user_name_occurrences())
print()
display_user_id_group()
