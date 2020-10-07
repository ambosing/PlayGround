def dfs(a):
    global cnt
    if a == m:
        print(' '.join(map(str, lst)))
        cnt += 1
        return
    else:
        for i in range(1, n + 1):
            lst[a] = i
            dfs(a + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    lst = [0] * m
    cnt = 0
    dfs(0)
    print(cnt)


