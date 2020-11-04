from sys import stdout


def dfs(a, b):
    global cnt
    if a == m:
        stdout.write(" ".join(lst) + "\n")
        cnt += 1
    else:
        for i in range(b, n + 1):
            lst[a] = str(i)
            dfs(a + 1, i + 1)


cnt = 0
n, m = map(int, input().split())
lst = [0] * m
dfs(0, 1)
print(cnt)
