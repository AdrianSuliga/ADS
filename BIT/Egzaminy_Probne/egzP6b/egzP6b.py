from egzP6btesty import runtests 

# Adrian Suliga
# Algorytm odtwarza skoki Garka i zapisuje ilość odwiedzeń danego punktu do słownika.
# Jeśli odwiedziliśmy dany punkt nieparzystą ilość razy to żarówka tam pozostaje zapalona.
# Po zakończeniu podróży wystarczy przejść po parach klucz: wartość w słowniku i dla
# każdej nieparzystej wartości zwiększyć odpowiedni licznik o 1. Szacuję złożoność
# czasową i pamięciową algorytmu na O(n).

def jump ( M ):
    memo = {}
    cnt = 0

    memo[(0, 0)] = 1
    travel(0, M, 0, 0, memo)

    for _, value in memo.items():
        if value % 2 == 1: cnt += 1

    return cnt
    
def travel(i:int, M:list, x:int, y:int, memo:dict) -> None:
    while True:
        if i == len(M): break
        x, y = move(M[i], x, y)
        if (x, y) in memo: memo[(x, y)] += 1
        else: memo[(x, y)] = 1
        i += 1

def move(move:str, x:int, y:int) -> tuple:
    fst, snd = move[0], move[1]

    if fst == 'U': y += 2
    elif fst == 'D': y -= 2
    elif fst == 'R': x += 2
    elif fst == 'L': x -= 2

    if snd == 'U': y += 1
    elif snd == 'D': y -= 1
    elif snd == 'R': x += 1
    elif snd == 'L': x -= 1

    return x, y

runtests(jump, all_tests = True)
