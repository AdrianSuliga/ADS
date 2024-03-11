class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen_nums = set()
        for number in nums:
            if number in seen_nums:
                return True
            else:
                seen_nums.add(number)
        return False