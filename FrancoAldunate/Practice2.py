#Excercises from slides
a = 1
b = 2
list = [1,2,3,4,5]

if(a in list):
    print("a exists in list")
else:
    print("a does not exist in list")

if(b not in list):
    print("b does not exist in list")
else:
    print("b exists in list")

value_1 = 20
value_2 = 20

if(value_1 is value_2):
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if(id(value_1) == id(value_2)):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")
print()

#Practice
#Create a function that receive 3 arguments :
#	2 numbers
#	1 operations
#According the operation defined the expected result need to be printed. For example :  operator “*” , numbers: “5” “6”
#perform_operation(“*”,”5”,”6”) => 30
print("Practice 2: Functions")
print("1. Function to perform operation according to operator given")
def perform_operation(operator, a, b):
    print(f"operator {operator}, a = {a}, b = {b}")
    result = 0
    sum = "+"
    substraction = "-"
    multiplication = "*"
    division = "/"
    module = "%"
    power = "pow"

    if(operator is sum):
        result = a + b
    elif(operator is substraction):
        result = a - b
    elif (operator is multiplication):
        result = a * b
    elif (operator is division):
        result = a / b
    elif (operator is module):
        result = a % b
    elif (operator is power):
        result = a ** b
    else:
        print("No valid operator")
    print("Result = ",result)

perform_operation("+",5,500)
perform_operation("-",70,700)
perform_operation("*",7,7)
perform_operation("/",70,10)
perform_operation("%",10,3)
perform_operation("pow",2,5)