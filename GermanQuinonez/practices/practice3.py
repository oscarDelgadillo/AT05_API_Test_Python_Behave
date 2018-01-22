# python script applying at least one time each one of the operators learned.
# Print the values and the condition that give you the result obtained.
is_equal = "=="
is_not_equal = "!="
is_greater_than = ">"
is_less_than = "<"
is_greater_or_equal_than = ">="
is_less_or_equal_than = "<="


def perform_operation(operator, a, b):
    if operator == is_equal:
        result = a == b
    elif operator == is_not_equal:
        result = a != b
    elif operator == is_greater_than:
        result = a > b
    elif operator == is_less_than:
        result = a < b
    elif operator == is_greater_or_equal_than:
        result = a >= b
    elif operator == is_less_or_equal_than:
        result = a <= b
    print(f'{a} {operator} {operand_b} is {result}')


operand_a = 1
operand_b = 2
perform_operation(is_equal, operand_a, operand_b)
perform_operation(is_not_equal, operand_a, operand_b)
perform_operation(is_greater_than, operand_a, operand_b)
perform_operation(is_less_than, operand_a, operand_b)
perform_operation(is_less_or_equal_than, operand_a, operand_b)
perform_operation(is_greater_or_equal_than, operand_a, operand_b)

add_and = "+="
subtract_and = "-="
multiplication_and = "*="
division_and = "/="
modulus_and = "%="

valid_operator = [add_and, subtract_and, multiplication_and, division_and, modulus_and]


def assignment_operation(operator, a, b):
    if operator in valid_operator:
        print(f'operand ={a}')
        if operator == add_and:
            a += b;
        elif operator == subtract_and:
            a -= b;
        elif operator == multiplication_and:
            a *= b;
        elif operator == division_and:
            a /= b;
        elif operator == modulus_and:
            a %= b;
        print(f'operand {operator} {operand_b}')
        print(f'operand ={a}')
    else:
        print("invalid operator")


print(operand_a)
print(operand_b)
assignment_operation(add_and, operand_a, operand_b)
assignment_operation(subtract_and, operand_a, operand_b)
assignment_operation(multiplication_and, operand_a, operand_b)
assignment_operation(division_and, operand_a, operand_b)
assignment_operation(modulus_and, operand_a, operand_b)
