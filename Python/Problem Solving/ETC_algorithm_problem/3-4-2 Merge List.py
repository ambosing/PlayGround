n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
res = []
i = 0
j = 0
for _ in range(n + m):
    if j == m:
        res.append(str(lst1[i]))
        i += 1
    elif i == n:
        res.append(str(lst2[j]))
        j += 1
    elif lst1[i] <= lst2[j]:
        res.append(str(lst1[i]))
        i += 1
    elif lst1[i] > lst2[j]:
        res.append(str(lst2[j]))
        j += 1

print(' '.join(res))
