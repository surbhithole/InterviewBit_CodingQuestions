# This function checks if the Number is a prime number or not
# Prime number is a number which has exactly two factors(1 and itself).
# "1" has one factor ie 1 and hence it is not a prime number.
# The smallest prime number is 2: The factors are (1,2)

import math
def primeNumber(N):
    #Edge case - Zero or One
    if N == 1 or N == 0:
        return "Not a prime number"
    #Negative number
    if N < 0:
        N = -(N)
    for i in range(2, int(math.sqrt(N))):
        if N % i == 0:
            return "Not a prime number"

    return "Prime number"

print(primeNumber(-13))