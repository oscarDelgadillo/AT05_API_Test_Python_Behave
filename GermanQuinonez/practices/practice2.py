# this function receive 3 arguments :
# 	2 numbers
# 	1 operations
# For example :  operator “*” , numbers: “2” “3”
# perform_operation(“*”,”2”,”3”) => 6
addition_operator = "+"
subtraction_operator = "-"
multiplication_operator = "*"
division_operator = "/"
modulus_operator = "%"
exponent_operator = "**"
floor_division_operator = "//"


def perform_operation(operator, a, b):
    if operator == addition_operator: result = a + b
    if operator == subtraction_operator: result = a - b
    if operator == multiplication_operator: result = a * b
    if operator == division_operator: result = a / b
    if operator == exponent_operator: result = a ** b
    if operator == floor_division_operator: result = a // b
    if operator == modulus_operator: result = a % b
    return result


number1 = 2
number2 = 3

print(perform_operation(addition_operator, number1, number2))
print(perform_operation(subtraction_operator, number1, number2))
print(perform_operation(multiplication_operator, number1, number2))
print(perform_operation(division_operator, number1, number2))
print(perform_operation(exponent_operator, number1, number2))
print(perform_operation(floor_division_operator, number1, number2))
print(perform_operation(modulus_operator, number1, number2))
