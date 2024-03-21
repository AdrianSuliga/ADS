# n - łączna długość liter, k - ilość liter w alfabecie
# sprawdzić czy dwa wyrazy są anagramem

def are_anagrams(s1, s2, k): # O(n + k) solution
    count_s = [0 for _ in range(k)]
    n = len(s1)
    for i in range(n):
        count_s[ord(s1[i])] += 1
        count_s[ord(s2[i])] -= 1
    for i in range(n):
        if count_s[i] != 0: return False
    return True

def are_anagrams_quicker(s1, s2, k): # use numpy to create array of size k in O(1)
    pass                             # than zero only those chars that are from s1