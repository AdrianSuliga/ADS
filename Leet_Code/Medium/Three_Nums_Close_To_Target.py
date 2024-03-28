class Solution:
    def merge_list(T):
        n = len(T)
        if n == 1:
            return
        pivot = n // 2
        L = T[:pivot]
        R = T[pivot:]

        Solution.merge_list(L)
        Solution.merge_list(R)

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
        while j < pivot:
            T[k] = R[j]
            j += 1
            k += 1

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
