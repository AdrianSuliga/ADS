class Solution:
    def merge_sort(T):
        n = len(T)
        if n == 1: return
        pivot = n // 2
        L = T[:pivot]
        R = T[pivot:]
        Solution.merge_sort(L)
        Solution.merge_sort(R)
        i, j, k = 0, 0, 0
        while i < pivot and j < n - pivot:
            if L[i] <= R[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1
        while i < pivot:
            T[k] = L[i]
            i += 1
            k += 1
        while j < n - pivot:
            T[k] = R[j]
            k += 1
            j += 1

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        Solution.merge_sort(nums)
        n = len(nums)
        result = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k, p = j + 1, n - 1
                while k < p:
                    sum = nums[i] + nums[j] + nums[k] + nums[p]
                    if sum == target:
                        result.add((nums[i], nums[j], nums[k], nums[p]))
                        k += 1
                        p -= 1
                    elif sum > target:
                        p -= 1
                    else:
                        k += 1
        return list(result)

