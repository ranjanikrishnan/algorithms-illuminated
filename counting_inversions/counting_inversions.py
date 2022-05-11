def counting_inversions(input_array):
    inversion_count = 0
    n = len(input_array)
    for i in range(n-1):
        for j in range(i + 1, n):
            if input_array[i] > input_array[j]:
                inversion_count += 1
    return inversion_count
