n, k = map(int, input().split())
lst = list(map(int, input().split(',')))

for _ in range(k):
    new_lst = []
    for i in range(n - 1):
        new_lst.append(lst[i + 1] - lst[i])
    lst = new_lst
    n -= 1
lst = list(map(str, lst))
print(','.join(lst))
