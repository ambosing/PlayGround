from collections import deque

v, e = map(int, input().split())
ind = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    ind[b] += 1


def topology_sort():
    result = []
    q = deque()
    for i in range(1, v + 1):
        if ind[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()

