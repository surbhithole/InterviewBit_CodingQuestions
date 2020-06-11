#Useful video - https://www.youtube.com/watch?v=JUzYl1TYMcU
def gcd(A,B):
    if A > B:
        num1 = A
        num2 = B
    else:
        num1 = B
        num2 = A

    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
        print(num1, num2)

    return num1

print(gcd(3768,1701))