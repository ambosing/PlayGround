n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
lst_len = n
idx = lst_len // 2
left = 0
right = lst_len

while lst[idx] != m:
    if lst[idx] < m:
        left = idx
        idx = (idx + right + 1) // 2
    elif lst[idx] > m:
        right = idx
        idx = (left + idx + 1) // 2
print(idx + 1)
