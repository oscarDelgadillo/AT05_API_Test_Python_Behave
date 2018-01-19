import math

# Excercises from slides

# Break examples
for val in "string":
    if val == "i":
        break
    print(val)
print("The end")
print()

val = 20
while val > 0:
    print("Current value :", val)
    val -= 1
    if val == 5:
        break
print("Good bye!")
print()

# Continue examples
for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")
print()

val = 20
while val > 0:
    print("Current value :", val)
    val -= 1
    if val == 5:
        continue

print("Good bye!")
print()

# Pass Statement examples
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
print()

# Practice
print("Practice: Statements and Loops")
# 1. Write a function area_of_circle(r) which returns the area of a circle of radius r
# only if the radius value is greater of 10.
print("1. Function that returns the area of a circle if its radius is greater than 10")

TWO = 2
TEN = 10


def area_of_circle(r):
    print(f"Radius value = {r}")
    if r > TEN:
        return math.pi * (r ** TWO)


print("Area of circle: ", area_of_circle(10))
print("Area of circle: ", area_of_circle(11))
print()

# Write a function sum_to(n) that returns the sum of all integer numbers
# up to and including only until any value lower than 35.
# So sum_to(10)wouldbe1+2+3...+10which would return the value 55,
# but if n=40 only until sum to 35 need to be returned.
print("2. Function that returns the sum af all integer numbers up to 35")

ONE = 1
THIRTY_SIX = 36


def sum_to_n(n):
    print(f"n = {n}")
    sum = 0
    val = 0
    while val < n + 1:
        sum += val
        if val == THIRTY_SIX:
            print("val is greater than 35")
            break
        print(f"val = {val}, sum = {sum}")
        val += ONE


sum_to_n(34)
print()
sum_to_n(37)
