n = int(input())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

result = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    result.append(str(cnt))
print(' '.join(result))
