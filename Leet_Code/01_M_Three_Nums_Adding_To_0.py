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
            j += 1
            k += 1

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