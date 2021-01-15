def counting_sort(arr):
    a = [0 for _ in range(max(arr) + 1)]
    for i in arr:
        a[i] += 1
    idx1 = 0
    for idx2, v in enumerate(a):
        while a[idx2] > 0:
            arr[idx1] = idx2
            idx1 += 1
            a[idx2] -= 1


lst = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
counting_sort(lst)
print(lst)
