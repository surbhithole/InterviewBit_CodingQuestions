# Calculate the factors of a number N

import math
def factorization(N):
    # Array stores the result
    resArr = []
    # Number is equal to 1
    if N == 1:
        return [1]
    # Run the loop till sqrt of the Number since all the pairs after the sqrt of the number are reversed and are similar pairs.
    # Eg: Factors(36) = {1,36}, {2,18},{3,12},{4,9},{6,6},{9,4},{12,3},{18,2},{36,1}
    # The pairs are exactly similar to the ones before sqrt of the Number. Hence the loop size is sqrt(N)
    for i in range(1, int(math.sqrt(N))):
        if N % i == 0:
            resArr.append(i)
            resArr.append(N//i)

    return resArr

print(factorization(36))
