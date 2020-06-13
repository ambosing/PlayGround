m = int(input())
n = int(input())

arr = [1 for i in range(n + 1)]
arr[0] = 0
arr[1] = 0
for i in range(2, n + 1):
    if arr[i] == 0:
        continue
    if i ** 2 > n:
        break
    for j in range(i + i, n + 1, i):
        arr[j] = 0

lst = []
for i in range(m, n + 1):
    if arr[i] == 1:
        lst.append(i)

if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
