import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])


def dijkstra(s):
    distance[s] = 0
    q = []
    heapq.heappush(q, [0, s])
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for j in range(1, n + 1):
    if distance[j] == INF:
        print('INFINITY')
    else:
        print(distance[j])



