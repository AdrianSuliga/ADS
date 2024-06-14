from math import log10
class Solution:
    def reverse(self, x: int) -> int:
        length = int(log10(x))
        result = 0
        while x != 0:
            digit = x % 10
            result += digit * 10**length
            x //= 10
            length -= 1
        return result
