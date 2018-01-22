# Exercise one - Create 1 script to determine is a number is odd or even
print('---------------- ODD or EVEN NUMBERS ----------------')


def isOddOrEven(number):
    return 'even' if number % 2 == 0 else 'odd'


number = 7
print(number, 'is', isOddOrEven(number))
number = 21
print(number, 'is', isOddOrEven(number))
number = 50
print(number, 'is', isOddOrEven(number))

# Exercise two - According a list of values between a Min and Max range, identify if the number is prime or not
print('---------------- PRIME NUMBERS ----------------')


def isPrime(number):
    if number == 0: return 'Not Prime'
    if number == 1: return 'Prime'
    for i in range(2, int(abs(number) ** 0.5) + 1):
        if number % i == 0:
            return 'Not Prime'
    return 'Prime'
min = 0
max = 12
print('Min = {0} - Max = {1}'.format(min, max))
for tmp in range(min, max + 1):
    print(tmp, '=>', isPrime(tmp))

