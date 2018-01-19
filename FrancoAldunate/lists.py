# Practice
# Function 1:
# - No arguments defined
# - Should ask to the user the number of elements in the list
# - According the value inserted ask for each value of the array and push it in a new array
# - Return the array

ONE = 1


def list_builder():
    response = int(input("Please insert the number of elements for the list: "))
    print(f"The list will have a size of {response}")
    resultList = []
    for i in range(ONE, response + ONE):
        valueToInsert = input(f"Insert value {i}: ")
        resultList.append(valueToInsert)
    return resultList


# Function 2
# - Should receive 1 argument (the array returned in method 1)
# - should print the array

def print_list(input_list):
    print("Result: ", input_list)


print("Executing functions...")
print_list(list_builder())
