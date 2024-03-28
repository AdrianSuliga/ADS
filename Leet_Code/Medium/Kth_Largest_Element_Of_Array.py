class Solution:
    def build_heap(T):
        n = len(T)
        for i in range((n - 2) // 2, -1, -1):
            Solution.heapify(T, n, i)

    def heapify(T, n, i):
        l, r, mi = 2 * i + 1, 2 * i + 2, i

        if l < n and T[l] > T[mi]: mi = l
        if r < n and T[r] > T[mi]: mi = r

        if mi != i:
            T[mi], T[i] = T[i], T[mi]
            Solution.heapify(T, n, mi)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        Solution.build_heap(nums)
        for i in range(k - 1):
            nums[0], nums[-1] = nums[-1], nums[0]
            nums.pop()
            n -= 1
            Solution.heapify(nums, n, 0)
        return nums[0]