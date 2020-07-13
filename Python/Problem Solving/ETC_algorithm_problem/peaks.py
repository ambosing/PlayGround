n = int(input())

lists = list()
lists.append([0] * (n + 2))
for i in range(n):
    lst = [0]
    lst.extend(map(int, input().split()))
    lst.append(0)
    lists.append(lst)
lists.append([0] * (n + 2))

cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        num = lists[i][j]
        if lists[i - 1][j] < num and lists[i + 1][j] < num \
                and lists[i][j + 1] < num and lists[i][j - 1] < num:
            cnt += 1
print(cnt)
