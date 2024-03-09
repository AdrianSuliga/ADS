class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt = 0
        leader = nums[0]
        n = len(nums)
        for i in range(n):
            if nums[i] == leader:
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                leader = nums[i]
                cnt = 0
        return leader