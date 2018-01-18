# OPERATOR ==
print('---------------- OPERATOR == ----------------')
variableOne = 'circle'
variableTwo = 'circle'
if variableOne == variableTwo:
    result = 'EQUALS'
else:
    result = 'NOT EQUALS'
print("{0} == {1} ==> ARE {2}".format(variableOne, variableTwo, result))

# OPERATOR !=
print('---------------- OPERATOR != ----------------')
if variableOne != variableTwo:
    result = 'DIFFERENT'
else:
    result = 'NOT DIFFERENT'
print("{0} != {1} ==> ARE {2}".format(variableOne, variableTwo, result))

# OPERATOR >
print('---------------- OPERATOR > ----------------')
variableOne = 43232
variableTwo = 3324
print("{0} > {1} ==> {2}".format(variableOne, variableTwo, variableOne > variableTwo))

variableOne = 'C#'
variableTwo = 'Java'
print("{0} > {1} ==> {2}".format(variableOne, variableTwo, variableOne > variableTwo))

# OPERATOR <
print('---------------- OPERATOR < ----------------')
variableOne = 482.25
variableTwo = -53.2
print("{0} < {1} ==> {2}".format(variableOne, variableTwo, variableOne < variableTwo))

variableOne = 'Python2'
variableTwo = 'Python3'
print("{0} < {1} ==> {2}".format(variableOne, variableTwo, variableOne < variableTwo))

# OPERATOR >=
print('---------------- OPERATOR >= ----------------')
variableOne = 'PHP4'
variableTwo = 'PHP3'
print("{0} >= {1} ==> {2}".format(variableOne, variableTwo, variableOne >= variableTwo))

variableOne = 526
variableTwo = 526.1
print("{0} >= {1} ==> {2}".format(variableOne, variableTwo, variableOne >= variableTwo))

# OPERATOR <=
print('---------------- OPERATOR <= ----------------')
variableOne = 'PHP4'
variableTwo = 'PHP3'
print("{0} <= {1} ==> {2}".format(variableOne, variableTwo, variableOne <= variableTwo))

variableOne = 526
variableTwo = 526.1
print("{0} <= {1} ==> {2}".format(variableOne, variableTwo, variableOne <= variableTwo))

# OPERATOR =
print('---------------- OPERATOR = ----------------')
variableOne = 'Manual'
variableTwo = 'Automation'
print("variableOne = '{0}'".format(variableOne))
print("variableTwo = '{0}'".format(variableTwo))
variableOne = variableTwo
print("variableOne = variableTwo")
print("variableOne = '{0}'".format(variableOne))

# OPERATOR +=
print('---------------- OPERATOR += ----------------')
resultAdd = 0
index = 0
while index <= 5:
    resultAdd += index
    print('result =', resultAdd)
    index += 1

# OPERATOR -=
print('---------------- OPERATOR -= ----------------')
resultMin = 0
index = 5
while index <= 10:
    resultMin -= index
    print('result =', resultMin)
    index += 1

# OPERATOR *=
print('---------------- OPERATOR *= ----------------')
resultMul = 0
index = 11
while index <= 15:
    resultMul *= index
    print('result =', resultMul)
    index += 1

# OPERATOR /=
print('---------------- OPERATOR /= ----------------')
resultDiv = 0
index = 5
while index <= 10:
    resultDiv += index
    print('result =', resultDiv)
    index += 1

# OPERATOR in/not in
print('---------------- OPERATOR in/not in ----------------')
colorOne = 'red'
colorTwo = 'white'
listColors = ['blue', 'red', 'yellow', 'orange', 'gray', 'black']
if (colorOne in listColors):
    print(colorOne, " exists in list of colors")
else:
    print(colorOne, " exists doesn't exit in list of colors")

if (colorTwo not in listColors):
    print(colorTwo, " doesn't exist in list of colors")
else:
    print(colorTwo, "exists in list of colors")
