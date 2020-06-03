import math

def isPrime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primesum(A):
    for i in range(2, (A // 2) + 1):
        if isPrime(i):
            if isPrime(A - i):
                return [i, A - i]

print(primesum(16))