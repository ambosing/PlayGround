def hanoi(h, a, b, c, res):
    if h < 1:
        return
    hanoi(h - 1, a, c, b, res)
    res.append((a, c))
    hanoi(h - 1, b, a, c, res)


n = int(input())
lst = []
hanoi(n, 1, 2, 3, lst)
print(len(lst))
for i, j in lst:
    print(i, j)
