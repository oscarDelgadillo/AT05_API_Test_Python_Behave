#Pactice2 a function with all operations arithmetic

#a diccionarion is created with the arithmetical ooperations
my_dict = {'+':'suma', '-':'sustaction', '*':'multiplication', '/':'divition', '//':'divition parse int','%':'modulus', '**':'exponent' }

#function that performs the artimetic operations
def aritmeticOperation(number1, number2, operator):
    if operator=="+": return (number1+number2)
    elif operator=="-": return (number1-number2)
    elif operator == "*": return (number1 * number2)
    elif operator == "/": return (number1 / number2)
    elif operator == "//": return (number1 // number2)
    elif operator == "**": return (number1 ** number2)
    elif operator == "%": return (number1 % number2)
    else: return "the operation is not implemented"

#function that formats the string to be displayed
def perform_operation(number1, number2, operator):
    result = aritmeticOperation(number1, number2, operator)
    operatorStr=my_dict[operator]
    print(f"The result of the {operatorStr}, {number1} and {number2} is: {result} ")

#ways of using the function
perform_operation(5,2,"+")
perform_operation(5,2,"-")
perform_operation(5,2,"*")
perform_operation(5,2,"/")
perform_operation(5.2,2,"//")
perform_operation(5,2,"**")
perform_operation(5,2,"%")

