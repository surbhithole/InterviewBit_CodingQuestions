class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def getGCD(self, A, B):
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
        return num1

    def cpFact(self, A, B):
        gcdAB = self.getGCD(A, B)

        while gcdAB != 1:
            A = A // gcdAB
            gcdAB = self.getGCD(A, B)
        return A