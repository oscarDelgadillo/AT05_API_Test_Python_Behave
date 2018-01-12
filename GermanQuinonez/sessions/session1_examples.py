# Values and types
print(type(1))
print(type("Somthing"))
print(type(0.2))

# Variables

Message = "hi"
n = 1000
pi = 3.04e500
print(type(Message))
print(type(n))
print(type(pi))

# Membership operators

a = 1
b = 2
list = [1, 2, 3, 4, 5];

if (a in list):
    print("a exists list")
else:
    print("a does not exist list")

if (b not in list):
    print("b does not exist list")
else:
    print("b exists list")

# Identity operators

value_1 = 20
value_2 = 20

if value_1 is value_2:
    print("Line 1 - a and b have same identity")
else:
    print('Line 1 - a and b do not have same identity')

if id(value_1) == id(value_2):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")


# Functions

def print_lyrics():
    print("I'm a tester, and I'm okay.")
    print("I sleep all night and I work all day.")


print_lyrics()
