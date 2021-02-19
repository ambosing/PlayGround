import sys


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n + 1)]
edges = []
res = 0
last = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append([a, b, c])
edges.sort(key=lambda x: x[2])

for a, b, c in edges:
    if find_parent(p, a) != find_parent(p, b):
        union_parent(p, a, b)
        res += c
        last = c
print(res - last)
