# Test length of names of variables

nameOfSomeVariableForPython = 'This text is a test.'
thisVariableContain123NumbersInTheName = 'one two three - 1, 2, 3.'
onlyNumbersInTheContent = 85
listOfNumbers = [1, 2, 3, 4, 5, 6]

# Print content and type of the variables

print('CONTENT =', nameOfSomeVariableForPython, 'TYPE =', type(nameOfSomeVariableForPython))
print('CONTENT =', thisVariableContain123NumbersInTheName, 'TYPE =', type(thisVariableContain123NumbersInTheName))
print('CONTENT =', onlyNumbersInTheContent, 'TYPE =', type(onlyNumbersInTheContent))
print('CONTENT =', listOfNumbers, 'TYPE =', type(listOfNumbers))

# Addition operations

operatorOne = 10
operatorTwo = -23
result = operatorOne + operatorTwo;
print('ADD:', operatorOne, '+', operatorTwo, '=', result, ' - RESULT TYPE =', type(result))

# Subtraction operations

operatorOne = 22.2
operatorTwo = 85.7
result = operatorOne - operatorTwo;
print('SUB:', operatorOne, '-', operatorTwo, '=', result, ' - RESULT TYPE =', type(result))

# Multiplication operations

operatorOne = -75.2
operatorTwo = -15.7
result = operatorOne * operatorTwo;
print('MUL:', operatorOne, '*', operatorTwo, '=', result, ' - RESULT TYPE =', type(result))

# Division operations

dividend = 65
divider = 17
result = dividend / divider;
print('DIV:', dividend, '/', divider, '=', result, ' - RESULT TYPE =', type(result))

# Modulus operations

dividend = 65
divider = 17
result = dividend % divider;
print('MOD:', dividend, '%', divider, '=', result, ' - RESULT TYPE =', type(result))

# Exponent operations

base = 25
exponent = 6
result = base ** exponent;
print('EXP:', base, '^', exponent, '=', result, ' - RESULT TYPE =', type(result))

# Floor division operations

dividend = 5648
divider = 128.6
result = dividend // divider;
print('FLO:', dividend, '//', divider, '=', result, ' - RESULT TYPE =', type(result))
