def print_Block(block):
    print("-----------------", block, "-----------------")



def operatorEquals(valueOne, valueTwo):
    print_Block(" Operator == ")
    if valueOne == valueTwo:
        print(valueOne, "and", valueTwo, "Are Equals")
    else:
        print(valueOne, "and", valueTwo, "Are not Equals")


def operatorNotEquals(valueOne, valueTwo):
    print_Block("Operator !=")
    if valueOne != valueTwo:
        print(valueOne, "and", valueTwo, "Are different")
    else:
        print(valueOne, "and", valueTwo, "Are Not different")


def operatorMajorThat(valueOne, valueTwo):
    print_Block("Operator >")
    if valueOne > valueTwo:
        print(valueOne, "is > ", valueTwo, ": true")
    else:
        print(valueOne, "is > ", valueTwo, ": false")


def operatorMinorThat(valueOne, valueTwo):
    print_Block("Operator < ")
    if valueOne < valueTwo:
        print(valueOne, "is < ", valueTwo, ": true")
    else:
        print(valueOne, "is < ", valueTwo, ": false")


def assignmentOperatorsAddition():
    print_Block("Assignment operators +=")
    result = 0
    index = 0
    while index <= 5:
        result += index
        print("result =", result)
        index += 1

def assignmentOperatorSubtration():
    print_Block("Operator -=")
    result = 0
    index = 5
    while index <= 10:
        result -= index
        print("result =", result)
        index += 1

def assignmentOperatorMultiplication():
    print_Block("Operator *=")
    result = 0
    index = 11
    while index <= 15:
        result *= index
        print('result =', result)
        index += 1


def assignmentOperatorDivision():
    print_Block(" Operator /= ")
    result = 0
    index = 5
    while index <= 10:
        result += index
        print('result =', result)
        index += 1

def listName(nameOne,nameTwo):
    print_Block(" Membership operators")
    listNames = ["Oscar","Franco","Abner","Silvia","Marcelo","Marco"]
    if nameOne in listNames:
        print(nameOne, " exists in list of names")
    else:
        print(nameOne, " exists doesn't exit in list of names")

    if nameTwo not in listNames:
        print(nameTwo, " doesn't exist in list of names")
    else:
        print(nameTwo, "exists in list of names")


operatorEquals("Hello","Hello")
operatorNotEquals("Hello","Hola")
operatorMajorThat(100,99)
operatorMajorThat("Pyton","Java")
operatorMinorThat(99,100)
operatorMinorThat("C","C++")
assignmentOperatorsAddition()
assignmentOperatorSubtration()
assignmentOperatorMultiplication()
assignmentOperatorDivision()
listName("Marco","Pedro")