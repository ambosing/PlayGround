from collections import deque


def solution():
    n, k = map(int, input().split())
    lst = deque([str(i + 1) for i in range(n)])
    res = []
    cnt = 0
    while lst:
        cnt += 1
        num = lst.popleft()
        if cnt % k == 0:
            res.append(num)
        else:
            lst.append(num)
    print("<", ', '.join(res), ">", sep="")


solution()
