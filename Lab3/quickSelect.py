from random import randint
class Solution:
    def quick_select(T, k, left, right):
        if left >= right: return T[left]
        while True:
            p_index = randint(left, right)
            pivot = Solution.partition(T, left, right, p_index)
            if k == pivot: return T[k]
            elif k < pivot: right = pivot - 1
            else: left = pivot + 1
    
    def partition(T, left, right, p_index):
        pivot = right
        T[p_index], T[right] = T[right], T[p_index]
        ind = left - 1
        for i in range(left, right):
            if T[i] > T[pivot]:
                ind += 1
                T[i], T[ind] = T[ind], T[i]
        ind += 1
        T[ind], T[pivot] = T[pivot], T[ind]
        return ind
    
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return Solution.quick_select(nums, k - 1, 0, len(nums) - 1)
