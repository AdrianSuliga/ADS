class Solution:
    def heap_sort(T):
        n = len(T)
        Solution.build_heap(T)
        for i in range(n - 1, 0, -1):
            T[0], T[i] = T[i], T[0]
            Solution.heapify(T, i, 0)

    def build_heap(T):
        n = len(T)
        for i in range(Solution.parent(n - 1), -1, -1):
            Solution.heapify(T, n, i)

    def heapify(T, n, i):
        l, r, mi = Solution.left(i), Solution.right(i), i

        if l < n and T[l][0] > T[mi][0]: mi = l
        if r < n and T[r][0] > T[mi][0]: mi = r

        if mi != i:
            T[mi], T[i] = T[i], T[mi]
            Solution.heapify(T, n, mi)
    
    def left(i): return 2 * i + 1
    def right(i): return 2 * i + 2
    def parent(i): return (i - 1) // 2

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        Solution.heap_sort(intervals)
        print(intervals)
        result = []
        for i in range(len(intervals)):
            if len(result) == 0 or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result