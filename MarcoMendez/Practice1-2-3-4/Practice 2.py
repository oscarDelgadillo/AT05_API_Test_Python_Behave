print("----------------- Comparison operators -----------------")

variableOne = 10
variableTwo = 10
print("Variable: ", variableOne)
print("Variable: ", variableTwo)

print("---Variable One 10 == Variable Two 10 ---")
if variableOne == variableTwo:
    print(" values equals ")

variableOne = 10
variableTwo = 11
print("---Variable One 10 != Variable Two 11 ---")
if variableOne != variableTwo :
    print(" not values")

variableOne = 10
variableTwo = 9
result = 0
print("--- Variable One 10 > Variable Two 9 ---")
if variableOne > variableTwo:
    print("variable one is > ")

print("----------------- Assignment operators -----------------")
result += variableOne
result -= variableTwo
result *= variableOne
result /= variableOne

print("----------------- Membership operators -----------------")

a = 1
b = 2
list = [1, 2, 3, 4, 5 ];

if a in list:
   print("a exists list")
else:
   print("a does not exist list")

if b not in list:
    print("b does not exist list")
else:
    print("b exists list")

print("----------------- Identity operators -----------------")

value_1 = 20
value_2 = 20

if ( value_1 is value_2 ):
   print("Line 1 - a and b have same identity")
else:
   print('Line 1 - a and b do not have same identity')

if ( id(value_1) == id(value_2) ):
   print("Line 2 - a and b have same identity")
else:
   print("Line 2 - a and b do not have same identity")

print("----------------- Functions -----------------")

def print_lyrics():
    print("I'm a tester, and I'm okay.")
    print("I sleep all night and I work all day.")
print_lyrics()

def print_Block(block):
    print("-----------------",block, "-----------------")

print_Block("Practice1-2-3-4 - Create a function that receive 3 arguments : 1 operation and 2 numbers")
print("perform_operation(*,2,3) => 6")
def perform_operation(operation,valueONne,valueTwo):
   addition="+"
   multiplication="*"
   division="/"
   subtraction="-"
   if operation == addition:
       print("Addition result = ", valueONne + valueTwo )
   elif operation == subtraction:
       print("Subtraction result = ", valueONne - valueTwo)
   elif operation == multiplication:
       print("Multiplication result = ", valueONne * valueTwo)
   elif operation == division:
       print("Division result = ", valueONne / valueTwo)
   else:
    print("Operator no identified")


perform_operation("+",2,2)
perform_operation("-",2,2)
perform_operation("*",2,2)
perform_operation("/",15,3)

