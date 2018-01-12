# script to determine is a number is odd or even (use single line statement if applies)
def number_odd_even(number):
    if number % 2 == 0: print("number {} is odd".format(number))
    if number % 2 != 0: print(("number {} is even".format(number)))


number_odd_even(1)
number_odd_even(2)


# this function identify if the number is prime or notAccording a list of values between a Min and Max range.

def list_of_values_between_a_Min_and_Max_range(min, max):
    for num in range(min, max):
        prime = 1
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                prime = 0
                break
        if prime:
            print(f"{num} is prime")
        else:
            print(f"{num} is not prime")


Min = 10
Max = 118
list_of_values_between_a_Min_and_Max_range(min, max)
