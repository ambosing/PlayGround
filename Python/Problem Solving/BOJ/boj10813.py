from collections import deque


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


n, m = map(int, input().split())
lst = [str(i + 1) for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    swap(lst, a - 1, b - 1)
print(' '.join(lst))
