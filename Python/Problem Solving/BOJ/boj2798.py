import sys


def solution():
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 0
    min_val = sys.maxsize
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k:
                    continue
                val = lst[i] + lst[j] + lst[k]
                if val <= m and m - val < min_val:
                    min_val = m - val
                    result = val
    print(result)


solution()
