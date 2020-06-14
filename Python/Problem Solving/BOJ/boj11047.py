n, k = map(int, input().split())
min_cnt = 0
len_lst = 0
lst = []

for i in range(n):
    lst.append(int(input()))
    len_lst += 1

for i in range(len_lst - 1, -1, -1):
    min_cnt += k // lst[i]
    k = k % lst[i]

print(min_cnt)
