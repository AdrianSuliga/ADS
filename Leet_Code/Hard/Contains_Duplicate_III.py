class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        start, end, size = 0, 0, len(nums)
        window = {}
        while end < size:
            if end - start > indexDiff:
                if nums[start] in window and window[nums[start]] > 0:
                    window[nums[start]] -= 1
                if nums[start] in window and window[nums[start]] == 0:
                    window.pop(nums[start])
                start += 1

            if nums[end] in window:
                window[nums[end]] += 1
            else:
                window[nums[end]] = 1
            end += 1
  

S = Solution()
print(S.containsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15], 1, 3))

# [1, 5, 9, 1, 5, 9] indDiff = 2, valDiff = 3
# [1, 5, 9]
#