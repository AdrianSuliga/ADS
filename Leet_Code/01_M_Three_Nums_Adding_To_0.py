class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # n logn
        result = set()
        n = len(nums)
        for i in range(n - 1): # n^2
            j, k = i + 1, n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.add([nums[i], nums[j], nums[k]]) # linear for the most cases since its set
                    temp1, temp2 = j, k
                    while j < k and nums[temp1] == nums[j]: j += 1
                    while j < k and nums[temp2] == nums[k]: k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        return result
# Overall: O(nlogn + n^2) => O(n^2)