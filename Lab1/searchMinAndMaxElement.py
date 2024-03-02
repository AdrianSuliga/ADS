"""
find smallest and largest number in the array
"""
def lookForSmallestAndGreatest(T):
    mini, maks = float('inf'), -float('inf')
    for i in range(0, len(T), 2):
        if (T[i] < T[i+1]):
            if T[i] < min: pass
            if T[i+1] > max: pass
        else:
            if T[i+1] < min: pass
            if T[i] > max: pass