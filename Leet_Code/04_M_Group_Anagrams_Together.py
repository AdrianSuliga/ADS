from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        m = defaultdict(list)
        for i in range(len(strs)):
            l = list(strs[i])
            l.sort()
            m[str(l)].append(strs[i])
        return list(m.values())
    

print(Solution.groupAnagrams(Solution, ["eat","tea","tan","ate","nat","bat"]))




""" passed 111/126 tests
    def areAnagrams(s1, s2):
        if s1 == s2: return True
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 == l2:
            return True
        else:
            return False
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        while len(strs) > 0:
            anagrams = [strs[0]]
            ind = 1
            while ind < len(strs):
                if Solution.areAnagrams(strs[ind], strs[0]):
                    anagrams.append(strs[ind])
                    strs.pop(ind)
                    ind = 1
                else:
                    ind += 1
            strs.pop(0)
            result.append(anagrams)
        return result
        """
