from zad1testy import Node, runtests

"""
Program znajduje w liście najmniejszy element, usuwa go z listy i buduje za pomocą
wycinanych elementów nową, już posortowaną listę. Wiedząc, że lista jest k-chaotyczna 
zawężamy obszar poszukiwań najmniejszego elementu na takie odległe od początku listy o k
W najgorszym przypadku algorytm sprawdzi wszystkie k liczb w liście, jako że lista ma n
elementów to uzyskana złożoność wynosi O(nk).
k = O(1) => dostajemy O(n)
k = O(logn) => dostajemy O(nlogn)
k = O(n) => dostajemy O(n^2)
"""

def SortH(p,k): 
    nNode = Node() # wartownik na początku listy
    nNode.next = p
    p = nNode
    result = Node() # Node od którego będziemy budować listę
    s = result # start listy (ustawiony na wartownika)
    while p.next is not None: # dopóki nie opróżnimy całej listy, pętla przerwie się gdy list p będzie miała postać None (wartownik) -> None
        q = extractSmallest(p, k) 
        result.next = q 
        result = result.next 
    return s.next # s.next, bo ustawiłem s na wartownika na początku

def extractSmallest(p, k):
    prev, it = p, 0
    p = p.next
    mini = p.val
    while it < k and p.next is not None:
        if p.next.val < mini:
            prev = p
            mini = p.next.val
        p = p.next
        it += 1
    buffor = prev.next
    prev.next = buffor.next
    return buffor

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
