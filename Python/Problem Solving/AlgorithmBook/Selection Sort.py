lst = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(lst)):
    idx = i
    for j in range(i + 1, len(lst)):
        if lst[idx] > lst[j]:
            idx = j
    lst[i], lst[idx] = lst[idx], lst[i]
print(lst)

