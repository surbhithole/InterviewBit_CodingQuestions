def isPalindrome(A):
    i = 0
    j = len(A) - 1

    while i < j:
        while i < len(A) and A[i].isalnum() == False:
            i += 1
        while j >= 0 and A[j].isalnum() == False:
            j -= 1
        if A[i].lower() == A[j].lower():
            print(A[i], A[j])
            i += 1
            j -= 1
        else:
            print("in False", A[i], A[j])
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))