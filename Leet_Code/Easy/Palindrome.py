from math import log10
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        size = int(log10(x)) + 1
        T = [0 for _ in range(size)]
        idx = size - 1
        while x != 0:
            T[idx] = x % 10
            x //= 10
            idx -= 1
        i, j = 0, size - 1
        while i < j:
            if T[i] != T[j]: return False
            i += 1
            j -= 1
        return True
    def isPalindrome2(self, x:int) -> bool:
        return str(x)[::-1] == str(x)

S = Solution()
print(S.isPalindrome(0))