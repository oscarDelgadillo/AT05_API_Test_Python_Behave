#Practice 4.2 between a range of numbers verify if it is prime or not

# function that between a range of numbers verify if it is prime or not
def rangePrime(min, max):
    for num in range(min, max):
        prime = 1
        for i in range(2, (num//2)+1):
            if num % i == 0:
                prime=0
                break
        if prime:
            print(f"{num} is prime")
        else: print(f"{num} is not prime")

#call to the function
min =1
max = 9
rangePrime(min, max)