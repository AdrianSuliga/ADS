class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, j, k = m - 1, n - 1, n + m - 1
        while i > -1 and j > -1:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while i > -1:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        while j > -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1