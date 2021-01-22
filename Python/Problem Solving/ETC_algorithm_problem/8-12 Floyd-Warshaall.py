import sys

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for a in range(n + 1):
    graph[a][a] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if graph[row][col] >= INF:
            graph[row][col] = "M"
        if col != n + 1:
            print(graph[row][col], end=" ")
        else:
            print(graph[row][col])

