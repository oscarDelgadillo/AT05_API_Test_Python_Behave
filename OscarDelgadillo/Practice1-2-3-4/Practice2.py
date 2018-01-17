def perform_operation(operator, numberOne, numberTwo):
    if operator == '+':
        return numberOne + numberTwo
    if operator == '-':
        return numberOne - numberTwo
    if operator == '*':
        return numberOne * numberTwo
    if operator == '/':
        return numberOne / numberTwo
    if operator == '%':
        return numberOne % numberTwo
    if operator == '**':
        return numberOne ** numberTwo
    if operator == '//':
        return numberOne // numberTwo
    else:
        return 'error with the operator.'


numberOne = 8
numberTwo = 32
print(numberOne, '+', numberTwo, '=', perform_operation('+', numberOne, numberTwo))
print(numberOne, '-', numberTwo, '=', perform_operation('-', numberOne, numberTwo))
print(numberOne, '*', numberTwo, '=', perform_operation('*', numberOne, numberTwo))
print(numberOne, '/', numberTwo, '=', perform_operation('/', numberOne, numberTwo))
print(numberOne, '%', numberTwo, '=', perform_operation('%', numberOne, numberTwo))
print(numberOne, '**', numberTwo, '=', perform_operation('**', numberOne, numberTwo))
print(numberOne, '//', numberTwo, '=', perform_operation('//', numberOne, numberTwo))
