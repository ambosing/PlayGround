def dfs(a, chk):
    global cnt
    if a == n - 1:
        cnt += 1
    else:
        for i in range(n):
            if graph[a][i] == 1 and chk[i] == 0:
                chk[i] = 1
                dfs(i, chk)
                chk[i] = 0


cnt = 0
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    row, col = map(int, input().split())
    graph[row - 1][col - 1] = 1
check = [0] * n
check[0] = 1
dfs(0, check)
print(cnt)
