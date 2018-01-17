#Excercises from slides
print(type(1))
print(type("Test"))
print(type(0.2))

Message = "String test"
print(type(Message))
n = 1000
print(type(n))
pi = 3.1416
print(type(pi))

some_variable_really_long_is_accepted = "Any_value"
print(some_variable_really_long_is_accepted)
some123_variable = 1
print(some123_variable)
help("keywords")

#Practice Arithmetic's operators
#Create a new python script to :
# -Assign values to variables with long names and combining letters with numbers
print("Practice 1: Arithmetic's operators")
print("1. Assign values to variables with long names and combining letters with numbers")

result_of_concatenation_of_2_strings = "String1" + "String2"
print("Variable: result_of_concatenation_of_2_strings = ", result_of_concatenation_of_2_strings)

result_of_multiply_2_numbers_2_times = (7*77) * (7*77)
print("Variable: result_of_multiply_2_numbers_2_times = ", result_of_multiply_2_numbers_2_times)

result_of_22222_to_the_1000_power = 22222**1000
print("Variable: result_of_22222_to_the_1000_power = ", result_of_22222_to_the_1000_power)
print()

# -Perform arithmetic operations using all operators
print("2. Perform arithmetic operations using all operators")

#Addition
def add(a,b):
    print(f"Addition of: a = {a} + b = {b}")
    return "Result = ",a + b
print(add(7,14))

#Substraction
def sub(a,b):
    print(f"Substraction of: a = {a} - b = {b}")
    return "Result = ",a - b
print(sub(77,144))

#Multiplication
def multiply(a,b):
    print(f"Multiplication of: a = {a} x b = {b}")
    return "Result = ",a * b
print(multiply(7,-14))

#Quotient
def div(a,b):
    print(f"Quotient of: a = {a} / b = {b}")
    return "Result = ",a / b
print(div(7.55,14.99))

#Quotient with floor division
def div(a,b):
    print(f"Quotient with floor division of: a = {a} // b = {b}")
    return "Result = ",a // b
print(div(80,7))

#Modulus
def mod(a,b):
    print(f"a = {a} modulus b = {b}")
    return "Result = ",a % b
print(mod(100,3))

#Exponent or Power: where a is base and b is the power
def pow(a,b):
    print(f"Base a = {a}, to Power b = {b}")
    return "Result = ",a ** b
print(pow(77,777))

#Combination of operators
def percentageof(percentage_input,total):
    print(f"Percentage = {percentage_input}, Total = {total}")
    return "Result = ",total * percentage_input / 100
print(percentageof(7,5777))