# Function 1:
# No arguments defined
# Should ask to the user the number of elements in the list
# According the value inserted ask for each value of the array and push it in a new array
# Return the array

print('---------------- FUNCTION ONE ----------------')


def askElements():
    print("Insert the quantity of elements in the list: ", end='')
    quantity = int(input())
    array = []
    for x in range(0, quantity):
        print("Insert element in the list: ", end='')
        array.append(input())

    return array


print(askElements())

# Function 2:
# Should receive 1 argument (the array returned in method 1)
# should print the array
print('---------------- FUNCTION TWO ----------------')


def printArray(array):
    print(array)


printArray(askElements())
