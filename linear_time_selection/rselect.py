from typing import List
import random


def rselect(a: List[int], order: int):
    required_index = order - 1
    if len(a) == 1:
        return a[0]
    l = 0
    r = len(a)
    p = random.randint(l, r - 1)
    a[l], a[p] = a[p], a[l]
    p = l
    i, j = p+1, p+1
    while j <= len(a)-1:
        if a[j] <= a[p]:
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1
    a[p], a[i-1] = a[i-1], a[p]
    p = i-1
    if p == required_index:
        return a[p]
    elif p > required_index:
        return rselect(a[:p], order)
    else:
        return rselect(a[p+1:], order - p - 1)

