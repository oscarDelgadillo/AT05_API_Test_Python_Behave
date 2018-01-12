my_dict = {'+':'suma', '-':'sustaction', '*':'multiplication', '/':'divicion', '%':'modulus', '**':'exponent' }

def aritmeticOperation(number1, number2, operator):
    if operator=="+": return (number1+number2)
    elif operator=="-": return (number1-number2)
    elif operator == "*": return (number1 * number2)
    elif operator == "/": return (number1 / number2)
    elif operator == "//": return (number1 // number2)
    elif operator == "**": return (number1 ** number2)
    else: return "the operation is not implemented"

def perform_operation(number1, number2, operator):
    result = aritmeticOperation(number1, number2, operator)
    operatorStr=my_dict[operator]
    print(f"The result of the {operatorStr}, {number1} and {number2} is: {result} ")


perform_operation(5,2,"*")

