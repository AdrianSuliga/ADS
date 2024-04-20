class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        max1 = max(nums)
        min1 = min(nums)

        gap = max(1, (max1 - min1) // (n - 1))
        bucketCnt = (max1 - min1) // gap + 1

        maxNums = [-float('inf') for _ in range(bucketCnt)]
        minNums = [float('inf') for _ in range(bucketCnt)]

        for i in range(n):
            idx = (nums[i] - min1) // gap
            minNums[idx] = min(minNums[idx], nums[i])
            maxNums[idx] = max(maxNums[idx], nums[i])
        
        ans = 0
        prev = min1
        for i in range(bucketCnt):
            if minNums[i] == float('inf'): continue
            ans = max(ans, minNums[i] - prev)
            prev = maxNums[i]
        return ans
    

T = [1, 1, 1, 1]
S = Solution()
print(S.maximumGap(T))