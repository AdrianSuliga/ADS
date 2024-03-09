class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        n = len(nums)
        for i in range(n - 1):
            j, k = i + 1, n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < abs(result - target):
                    result = sum
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        return result
