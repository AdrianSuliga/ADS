from math import log10
class Solution:
    def sort_nums(T:list[int]) -> None:
        def quick_sort(T:list[int], left:int, right:int):
            if left > right: return
            pivot = partition(T, left, right, (left + right) // 2)
            quick_sort(T, left, pivot - 1)
            quick_sort(T, pivot + 1, right)
        def partition(T:list[int], left:int, right:int, p_index:int) -> int:
            pivot = right
            T[p_index], T[right] = T[right], T[p_index]
            ind = left - 1
            for i in range(left, right):
                if is_bigger(T[i], T[pivot]):
                    ind += 1
                    T[ind], T[i] = T[i], T[ind]
            ind += 1
            T[ind], T[pivot] = T[pivot], T[ind]
            return ind
        def is_bigger(num1:int, num2:int) -> bool:
            s1, s2 = str(num1) + str(num2), str(num2) + str(num1)
            return s1 > s2

        quick_sort(T, 0, len(T) - 1)
    def largestNumber(self, nums: list[int]) -> str:
        result = ""
        Solution.sort_nums(nums)
        for i in range(len(nums)):
            if result == str(nums[i]) == "0": continue
            result += str(nums[i])
        return result
