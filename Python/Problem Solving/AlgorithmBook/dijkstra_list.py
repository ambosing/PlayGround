import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            idx = i
    return idx


def dijkstra(s):
    distance[s] = 0
    visited[s] = True
    for j in graph[s]:
        distance[j[0]] = j[1]
    for _ in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost



dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINYTY")
    else:
        print(distance[i])
