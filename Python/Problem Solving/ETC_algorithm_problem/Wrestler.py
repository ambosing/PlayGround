
n = int(input())
a = list()

for _ in range(n):
    h, w = map(int, input().split())
    a.append([h, w])

cnt = n
for i in range(n):
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            cnt -= 1
            break
print(cnt)
