import math
from typing import List
import statistics


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
    i = choose_median_pivot(a, l, r)
    a[l], a[i] = a[i], a[l]
    j = partition(a, l, r)
    quick_sort(a, l, j-1)
    quick_sort(a, j+1, r)


def choose_median_pivot(a: List[int], l: int, r: int) -> int:
    mid = (r - l) // 2
    numbers = [a[l], a[r-1], a[mid]]
    numbers.sort()
    median = statistics.median(numbers)
    median_index = a.index(math.floor(median))

    return median_index




