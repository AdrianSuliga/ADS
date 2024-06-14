class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, n = 0, len(s)

        for i in range(n):
            seen_chars = set()
            cnt = 0
            for j in range(i, n):
                if s[j] in seen_chars: break
                else: 
                    seen_chars.add(s[j])
                    cnt += 1
            result = max(result, cnt)
        
        return result
        