from itertools import permutations


def solution(a, mul):
    for i in range(n):
        a[i] *= mul[i]
    return sum(a)


n, f = map(int, input().split())
lst = [i for i in range(1, n + 1)]

b = [1] * n
# 이항계수 구하기
for i in range(1, n - 1):
    b[i] = b[i-1] * (n - i) // i
for item in list(permutations(lst, n)):
    res = solution(list(item), b)
    if res == f:
        item = list(map(str, item))
        print(" ".join(item))
        break
