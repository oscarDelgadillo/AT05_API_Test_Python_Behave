# Create 1 script to determine is a number is odd or even.

def print_Block(block):
    print("-----------------", block, "-----------------")


def isOddOrEven(number):
    print_Block("Determine is a number is odd or even")
    print("The Number is Odd" if number % 2 == 0 else "The Number is even")


# According a list of values between a Min and Max range,identify if the number is prime or not.

def is_prime(number):
    aux = 0
    for i in range(1, number + 1):
        if number % i == 0:
            aux += 1
    print(f"{number} is not prime"if aux != 2 else f"{number} is prime")

def prime_numbers(min, max):
    print(f"Prime numbers in range [{min},{max}]")
    for i in range(min, max + 1):
        is_prime(i)

isOddOrEven(10)
isOddOrEven(11)
prime_numbers(1, 10)
is_prime(3)
is_prime(9)