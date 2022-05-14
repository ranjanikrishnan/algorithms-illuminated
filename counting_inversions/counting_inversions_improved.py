def sort_and_count_inversions(a):
    n = len(a)
    if n == 0 or n == 1:
        return a, 0
    c, left_inversions = sort_and_count_inversions(a[:int(n/2)])
    d, right_inversions = sort_and_count_inversions(a[int(n/2):])
    b, split_inversions = merge_and_count_split_inversions(c, d)
    return b, left_inversions + right_inversions + split_inversions


def merge_and_count_split_inversions(c, d):
    n = len(c) + len(d)
    i = 0
    j = 0
    b = [0] * n
    split_inversions = 0
    for k in range(n):
        if j == len(d):
            b[k] = c[i]
            i += 1
            continue
        if i == len(c):
            b[k] = d[j]
            j += 1
            continue
        if c[i] < d[j]:
            b[k] = c[i]
            i += 1
        else:   # if d[j] < c[i]
            b[k] = d[j]
            j += 1
            split_inversions = split_inversions + (len(c) - i)
    return b, split_inversions

