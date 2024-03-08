"""
Dana jest posortowana tablica T i x, czy istnieją takie i, j, że T[i] + T[j] == x?
"""
def searchForSum(T, x):
    i, j = 0, len(T) - 1
    while i < j:
        sum = T[j] + T[i]
        if sum == x:
            return True
        if sum > x:
            j -= 1
        else:
            i += 1
    return False


T = [2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 24, 27, 37]
print(searchForSum(T, 15))
