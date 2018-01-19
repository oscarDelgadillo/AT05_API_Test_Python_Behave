def array_n():
    """
    This function asks to the user the number of elements in the list
    According the value inserted ask
    for each value of the array and push it in a new array
    :return: the array
    """
    print("Enter the number of elements in the list")
    number = int(input())
    list_result = []
    for i in range(number):
        print("Enter the value of element in the list")
        list_result.append(input())
    return list_result


def print_array(array):
    """"
    This function receive 1 argument array
    and print the array
    """
    for value in array:
        print(value)


array_data = array_n()
print_array(array_data)
