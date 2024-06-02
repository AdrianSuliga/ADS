class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)
        MAX_IDX = float('inf')

        for i in range(n):
            MAX_IDX = min(MAX_IDX, len(strs[i]))

        idx = 0
        result = ""

        while idx < MAX_IDX:
            letter = strs[0][idx]

            for i in range(n):
                if letter != strs[i][idx]: return result

            result += letter
            idx += 1

        return result