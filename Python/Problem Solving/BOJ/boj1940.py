n = int(input())
m = int(input())
lst = list(map(int, input().split()))
len_lst = len(lst)
lst.sort()
result = 0

for i in range(len_lst):
    if lst[i] == -1:
        continue
    for j in range(len_lst - 1, -1, -1):
        if lst[j] == -1 or i == j:
            continue
        if lst[i] + lst[j] == m:
            lst[i] = -1
            lst[j] = -1
            result += 1
print(result)
