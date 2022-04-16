from typing import List


def merge_sort(a: List[int]) -> List[int]:
    n = len(a)
    if n == 1:
        return a
    print(a[:int(n/2)])
    print(a[int(n/2):])
    c = merge_sort(a[:int(n/2)])
    d = merge_sort(a[int(n/2):])
    return merge(c, d)


def merge(c: List[int], d: List[int]) -> List[int]:
    n = len(c) + len(d)
    i = 0
    j = 0
    b: List[int] = [0] * n
    for k in range(0, n):
        if j == len(d):
            b[k] = c[i]
            i = i + 1
            continue
        if i == len(c):
            b[k] = d[j]
            j = j + 1
            continue
        if c[i] < d[j]:
            b[k] = c[i]
            i = i + 1
        else:    # if d[j] < c[i]
            b[k] = d[j]
            j = j + 1
    return b


