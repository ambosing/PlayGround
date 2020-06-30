import sys

while True:
    s = input()
    if s[0] == "0":
        break
    n, p = map(int, s.split())
    p = str(p)
    for i in range(1, n // 2, 2):
        lst = []
        for j in range(i, i + 2):
            lst.append(str(j))
        for j in range(n - i, n - i + 2):
            lst.append(str(j))
        if lst.count(p):
            lst.remove(p)
            print(' '.join(lst))
