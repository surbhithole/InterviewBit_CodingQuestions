def getBinaryRep(num):
    binaryStr = ""
    while num > 0:
        remainder = num % 2
        num = num//2
        binaryStr += str(remainder)

    return ''.join(reversed(binaryStr))

def addZeros(str1, n):
    for i in range(n):
        str1 = "0" + str1
    return str1

def addPadding(num1, num2):
    if len(num1) > len(num2):
        num2 = addZeros(num2, len(num1) - len(num2))
    elif len(num2) > len(num1):
        num1 = addZeros(num1, len(num2) - len(num1))
    return num1, num2


def getXORSum(num1, num2):
    sumOfXOR = 0
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            sumOfXOR += 1
    return sumOfXOR


def hammingDistance(A):
    returnSum = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            num1 = getBinaryRep(A[i])
            num2 = getBinaryRep(A[j])
            paddedNum1, paddedNum2 = addPadding(num1, num2)
            returnSum += getXORSum(paddedNum1, paddedNum2)
    return 2 * returnSum

print(hammingDistance([2,4,6]))