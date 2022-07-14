from typing import List


def partition(a: List[int], l: int, r: int) -> int:
    p = a[l]
    i = l+1
    for j in range(l+1, r):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    return i-1


def quick_sort(a: List[int], l: int, r: int):
    if l >= r:
        return
    i = l
    a[l], a[i] = a[i], a[l]
    j = partition(a, l, r)
    quick_sort(a, l, j)
    quick_sort(a, j+1, r)



