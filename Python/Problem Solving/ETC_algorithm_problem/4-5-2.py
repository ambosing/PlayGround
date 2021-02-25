n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort()
cnt = n
for i in range(n - 1):
    for j in range(i + 1, n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt -= 1
            break
print(cnt)
