class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        cnt0, cnt1, cnt2 = 0, 0, 0
        for i in range(n):
            if nums[i] == 0: cnt0 += 1
            elif nums[i] == 1: cnt1 += 1
            elif nums[i] == 2: cnt2 += 2
        for i in range(n):
            if cnt0 > 0:
                nums[i] = 0
                cnt0 -= 1
            elif cnt1 > 0:
                nums[i] = 1
                cnt1 -= 1
            elif cnt2 > 0:
                nums[i] = 2
                cnt2 -= 1
            
    def sortColorsV1(self, nums: list[int]) -> None:
        n = len(nums)
        if n <= 1: return
        pivot = n // 2
        L = nums[:pivot]
        R = nums[pivot:]
        Solution.sortColors(Solution, L)
        Solution.sortColors(Solution, R)
        i, j, k = 0, 0, 0
        while i < pivot and j < n - pivot:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        while i < pivot:
            nums[k] = L[i]
            i += 1
            k += 1
        while j < n - pivot:
            nums[k] = R[j]
            j += 1
            k += 1