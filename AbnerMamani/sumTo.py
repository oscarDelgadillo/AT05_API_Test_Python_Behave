#Function that:
#returns the sum of all integer numbers up to and including
# only until any value lower than 35. So sum_to(10)wouldbe1+2+3...+10
# which would return the value 55, but if n=40
# only until sum to 35 need to be returned.

def sumTo(n):
    sum=0
    for i in range(1,n+1):
        if i > 35:
            return sum
        sum+=i
    return sum

print(f"Sum to {10} is: ",sumTo(10))
print(f"Sum to {25} is: ",sumTo(25))
print(f"Sum to {35} is: ",sumTo(35))
print(f"Sum to {45} is: ",sumTo(45))
