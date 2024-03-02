"""
T - posortowana rosnąco tablica n elementów
znajdź najmniejszą liczbę całkowitą, której nie ma w tablicy
liczby w tablicy są z zakresu 0 ... m - 1
np. [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
n = 10
m = 12
"""
#Przechodzimy po elementach tablicy kolejno sprawdzając czy kolejny element ciągu jest równy indeksowi
#logarytmicznie: zaczynamy od środka i sprawdzamy czy indeksy się zgadzają