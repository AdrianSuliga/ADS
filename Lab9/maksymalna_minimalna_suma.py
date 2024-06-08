# Dany jest ciąg liczb naturalnych ( a_0, a_1, a_2, ..., a_(n - 1) )
# dzielimy go na k spójnych podciągów i liczymy sumy wszystkich podciągów
# s_1, s_2, ..., s_k, wartością podziału jest minimum z tych sum
# chcemy podzielić ten ciąg tak aby wartość podziału była maksymalna

# f(i, j, k) = max { min { f(i, u, k - 1), suma od u do j z elementów ciągu } | u jest w [i, j]}
# f(i, j, 1) = suma od i do j z elementów ciągu
# f(i, j, k) = -inf jeśli j - i + 1 < k

def maxi_mini(A:list, k:int) -> int:
    pass



A = [4, 9, 13, 3, 9, 32, 12, 18, 9, 3, 5, 23, 19]
k = 5

print(maxi_mini(A, k))