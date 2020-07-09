n, k = map(int, input().split())
lst = list()
len_lst = 0

for i in range(1, n + 1):
    if n % i == 0:
        lst.append(i)
        len_lst += 1

if len_lst < k:
    print(-1)
else:
    print(lst[k - 1])
