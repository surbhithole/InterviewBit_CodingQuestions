def trailingZeroes1(A):
    totalZeros = 0
    divider = 5

    while A/divider > 0:
        totalZeros += A//divider

        divider *= 5

    return totalZeros

print(trailingZeroes1(15))