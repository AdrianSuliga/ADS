class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        my_map = {}
        for i in range(n):
            if nums[i] in my_map:
                my_map[nums[i]] += 1
            else:
                my_map[nums[i]] = 1
        
        value = n // 3
        result = []

        for item in my_map.items():
            if item[1] > value: result.append(item[0])
        
        return result

T = [3,2,3]
S = Solution()
print(S.majorityElement(T))