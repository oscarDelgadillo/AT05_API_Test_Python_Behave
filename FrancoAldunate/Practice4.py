# Excercises from slides
var = 100
if (var == 100): print("Value of expression is %d" % (var))
print()

some_value = 0
if some_value:
   print("Got a true expression value")
   print(some_value)
else:
   print("Got a false expression value")
   print(some_value)
print()

var = 100
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)
print()

num = -1
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
print()

count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1

print("Good bye!")
print()

count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")
print()

flag = 1
while (flag):
    print('Given flag is really true!')
    flag = 0
print("Good bye!")
print()

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
# iterate over the list
for val in numbers:
   sum = sum+val
print("The sum is", sum)
print()

genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):
   print("I like", genre[i])
print()

# Practice
print("Practice 4")
# 1. Create 1 script to determine if a number is odd or even
# (use single line statement if applies)
print("1. Determine if a number is odd or even")

def is_number_even(number):
    print(f" Is number {number} even?")
    return number % 2 == 0


print(is_number_even(8))
print(is_number_even(7))
print()

# 2. According a list of values between a Min and Max range,
# identify if the number is prime or not.
print("2. Determine if each number of a range is prime or not")


# determine if a number is prime or not
def is_prime(n):
    a = 0
    for i in range(1, n + 1):
        if n % i == 0:
            a += 1
    if a != 2:
        print(f"{n} is not prime")
    else:
        print(f"{n} is prime")


# Determine for each number of a list of values in Min and Max range if is prime or not
def prime_numbers(min, max):
    print(f"Prime numbers in range [{min},{max}]")
    for i in range(min, max + 1):
        is_prime(i)


prime_numbers(2, 20)
