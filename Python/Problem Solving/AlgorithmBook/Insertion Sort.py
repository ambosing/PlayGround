lst = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
        else:
            break
print(lst)
