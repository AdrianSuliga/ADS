class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        F = [1 for _ in range(n)]

        for k in range(1, n):
            for t in range(k):
                if nums[t] < nums[k] and F[k] < F[t] + 1:
                    F[k] = F[k] + 1
    
        return max(F) 