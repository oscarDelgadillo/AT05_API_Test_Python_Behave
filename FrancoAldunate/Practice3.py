#Practice Operators
#Create python script applying at least one time each one of the operators learned.
#Print the values and the condition that give you the result obtained.
print("Practice 3: Operators")
print("1. Comparison operators")

#Use of ==
print("Use of operator ==:")
def equals(string1, string2):
    print(f"Comparing the length of word {string1} with {string2}")
    if(len(string1) == len(string2)):
        print(f"Result: {string1} has the same length as {string2}")
    else:
        print(f"Result: {string1} has not the same length as {string2}")
equals("Automation","Manual")
equals("Test","Case")
print()

#Use of < and >
print("Use of operators < and >:")
def compare(a, b):
    print(f"Comparing values {a} and {b}")
    if(a > b):
        print(f"Result: {a} is greater than {b}")
    elif(a < b):
        print(f"Result: {a} is less than {b}")
    else:
        print(f"Result: {a} is equal to {b}")
compare(7, 5)
compare(7, 17)
compare(7, 7)
print()

#Use of >= and <=
print("Use of operators >= and <=:")
def is_in_range(x, lim_inf, lim_sup):
    print(f"Comparing if {x} is within the range [{lim_inf}, {lim_sup}]")
    if x >= lim_inf and x <= lim_sup:
        print(f"Result: {x} is within the range [{lim_inf}, {lim_sup}]")
    else:
        print(f"Result: {x} is not within the range [{lim_inf}, {lim_sup}]")
is_in_range(7,3,10)
is_in_range(8,12,22)
print()

#Use of !=
print("Use of operator !=:")
def is_different_than(a,b):
    print(f"Is {a} different than {b}?")
    if(a != b):
        return True
    else:
        return False
print(is_different_than(4.50,450))
print(is_different_than(50,50))
print()

print("2. Assignment operators")
#Use of =,+=, -=, *=, /=, %=
print("Use of operators =,+=:")
def hail_stone_sequence(x):
    count = 1
    if x > 1:
        if x % 2 == 0:
            count += hail_stone_sequence(x / 2)
            print(count)
        else:
            count += hail_stone_sequence((x * 3) + 1)
            print(count)
    return count
print("Hail stone sequence:")
hail_stone_sequence(70)
print()

print("Use of operators -=, *=, /=, %=:")
def function(a):
    print(f"Calculations using {a}")
    result = a
    result -= 2
    result *= 3
    result //= 4
    result %= 2
    print(f"Result = {result}")
function(7)
function(8)
print()

print("3. Membership operators")
#Use of in, not in
print("Use of operator in :")
def is_number_in_range(x, lim_inf, lim_sup):
    print(f"Is {x} in range [{lim_inf},{lim_sup}]?")
    if x in range(lim_inf, lim_sup):
        return f"Result: {x} is within range [{lim_inf},{lim_sup}]"
    else:
        return f"Result: {x} is not within range [{lim_inf},{lim_sup}]"
print(is_number_in_range(1,-22,44))
print(is_number_in_range(112,-22,44))
print()

print("Use of operator not in:")
def is_number_in_list(x, list):
    print(f"Is {x} in list {list}?")
    if x not in list:
        return "Result", False
    else:
        return "Result", True
print(is_number_in_list(7,[4,6,2,5,1,5,33,2,5,33]))
print(is_number_in_list(3,[343,21,35,73,23,453,3,32,1]))
print()

print("4. Identity operators")
#Use of is, is not
print("Use of operators is and is not:")
str1 = "This"
str2 = "This"
if str1 is str2: print(f"str1={str1} and str2={str2} have same identity")

str1 = "One"
str2 = "0ne"
if str1 is not str2: print(f"str1={str1} and str2={str2} have not same identity")