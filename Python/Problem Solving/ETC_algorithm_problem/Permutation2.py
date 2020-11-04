import sys


def dfs(a):
    global cnt
    if a == m:
        if len(set(lst)) != len(lst):
            return
        sys.stdout.write(" ".join(lst) + "\n")
        cnt += 1
    else:
        for i in range(1, n + 1):
            lst[a] = str(i)
            dfs(a + 1)


cnt = 0
n, m = map(int, input().split())
lst = [0] * m
dfs(0)
print(cnt)
