#Practice 3 handling the oopertors.

numberFirst = 123
numberSecond = 321

print("Handling over comparison operators")
resultTheOperation = numberFirst == numberSecond
print(f"{numberFirst} == {numberSecond} is {resultTheOperation}")

resultTheOperation = numberFirst != numberSecond
print(f"{numberFirst} != {numberSecond} is {resultTheOperation}")

resultTheOperation = numberFirst < numberSecond
print(f"{numberFirst} < {numberSecond} is {resultTheOperation}")

resultTheOperation = numberFirst > numberSecond
print(f"{numberFirst} > {numberSecond} is {resultTheOperation}")

resultTheOperation = numberFirst >= numberSecond
print(f"{numberFirst} >= {numberSecond} is {resultTheOperation}")

resultTheOperation = numberFirst <= numberSecond
print(f"{numberFirst} <= {numberSecond} is {resultTheOperation}")


print("Handling over Assignment operators")
number = 10;
number += 10;
print(f"The number is {number} and applying the operator +=10 is {number}")

number -= 1;
print(f"The number is {number} and applying the operator -=1 is {number}")

number *= 10;
print(f"The number is {number} and applying the operator *=10 is {number}")

number /= 10;
print(f"The number is {number} and applying the operator /=10 is {number}")

number %= 10;
print(f"The number is {number} and applying the operator %=10 is {number}")


listOfValues={1,4,6,8,9}
valueOne=4

print("Handling over Membership operators")
if valueOne in listOfValues:
    print(f" {valueOne} exists in list")
else:
    print(f" {valueOne} does not exists in list")

if valueOne not in listOfValues:
    print(f" {valueOne} does not exists in list")
else:
    print(f" {valueOne} exists in list")