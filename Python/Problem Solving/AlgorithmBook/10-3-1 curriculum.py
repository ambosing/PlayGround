from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
ind = [0] * (n + 1)
cost = [0] * (n + 1)
for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    for j in range(1, len(lst)):
        if lst[j] == -1:
            break
        graph[lst[j]].append(i)
        ind[i] += 1
    cost[i] = lst[0]
result = cost.copy()


def topology_sort():
    q = deque()
    for k in range(1, n + 1):
        if ind[k] == 0:
            q.append(k)
    while q:
        now = q.popleft()
        for k in graph[now]:
            ind[k] -= 1
            result[k] += cost[now]
            if ind[k] == 0:
                q.append(k)

    for idx in range(1, n + 1):
        print(result[idx])


topology_sort()
