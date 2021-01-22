import sys
import heapq

n, m, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append([y, z])

distance = [INF] * (n + 1)
start = c


def dijkstra(s):
    q = []
    distance[s] = 0
    heapq.heappush(q, [0, s])
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i, d in graph[now]:
            cost = dist + d
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


dijkstra(c)
cnt = -1
dist_max = 0
for dis in distance:
    if dis != INF:
        cnt += 1
        if dist_max < dis:
            dist_max = dis

print(cnt, dist_max)

