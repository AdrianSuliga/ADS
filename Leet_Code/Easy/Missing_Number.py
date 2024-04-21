class Solution: # Optimized O(n)
    def missingNumber(self, nums: list[int]) -> int:
        size = len(nums)
        result = size
        for i in range(size):
            result += i - nums[i]
        return result      

T = [9,6,4,2,3,5,7,0,1]
S = Solution()
print(S.missingNumber(T))

"""# brute force O(n logn)
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i != nums[i]: return i
        return n"""
        