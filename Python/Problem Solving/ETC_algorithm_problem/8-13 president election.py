n = int(input())
INF = 51
graph = [[INF] * (n + 1) for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1

for a in range(n + 1):
    graph[a][a] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            graph[b][a] = min(graph[b][a], graph[k][b] + graph[k][a])


lst_cnt = [INF]
for i in range(1, n + 1):
    max_val1 = 0
    max_val2 = 0
    for j in range(1, n + 1):
        if graph[i][j] < INF:
            max_val1 = max(max_val1, graph[i][j])
        if graph[j][i] < INF:
            max_val2 = max(max_val2, graph[j][i])
    lst_cnt.append(max(max_val1, max_val2))
min_val = min(lst_cnt)
candidate = [str(i) for i, v in enumerate(lst_cnt) if min_val == v]
print(min_val, lst_cnt.count(min_val))
print(' '.join(candidate))
