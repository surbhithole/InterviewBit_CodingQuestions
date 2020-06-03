# Sieve of Eratosthenes is the algorithm which finds all the prime numbers till the given number in a most efficient way
# Time complexity of the algorithm is O(n * loglogn)
# It creates a list of size of the given numbers. Traverse through the list and strikes off all the factors of the prime numbers
# In this algorithm we are finding factors of a number to eliminate them as they cannot be prime numbers. Factors of a number come in pairs. n = a*b where
# a <= sqrt(n) and b >= sqrt(n). Hence we run the loop till sqrt of n to find all the factors.

import math
def findAllPrimeNumbers(N):
    # numberList consists of the final prime numbers
    numberList = [1]*(N+1)
    # Since 0 and 1 cannot be prime numbers
    numberList[0] = 0
    numberList[1] = 0

    for i in range(2, int(math.sqrt(N))+1):
        if numberList[i] == 1:
            for j in range(i*i, N+1, i):
                if i*j <= N:
                    # Marking all the factors of a number to zero as they cannot be prime numbers
                    numberList[i*j] = 0

    resArr = []
    for i in range(len(numberList)):
        if numberList[i] == 1:
            resArr.append(i)
    return resArr

print(findAllPrimeNumbers(27))




