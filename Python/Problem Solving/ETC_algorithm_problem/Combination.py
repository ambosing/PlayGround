from sys import stdout


def check_big(a):
    for i in range(1, len(a)):
        if a[i - 1] >= a[i]:
            return False
    return True


def dfs(a):
    global cnt
    if a == m:
        if check_big(lst):
            stdout.write(" ".join(lst) + "n")
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
