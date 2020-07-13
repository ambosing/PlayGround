n = int(input())
lst = list()

for i in range(n):
    lst.append(list(map(int, input().split())))

t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if b == 0:
        for j in range(c):
            num = lst[a - 1].pop(0)
            lst[a - 1].append(num)
    if b == 1:
        for j in range(c):
            num = lst[a - 1].pop()
            lst[a - 1].insert(0, num)

limit = (n + 1) // 2
s = -1
e = n + 1
res = 0
for i in range(n):
    if i < limit:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
    res += sum(lst[i][s:e])
print(res)
