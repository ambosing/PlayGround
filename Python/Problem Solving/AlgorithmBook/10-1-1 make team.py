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


def kruskal(parent):
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 0:
            union_parent(p, b, c)
        elif a == 1:
            if find_parent(p, b) == find_parent(p, c):
                sys.stdout.write("YES\n")
            else:
                sys.stdout.write("NO\n")


n, m = map(int, input().split())
p = [i for i in range(n + 1)]
kruskal(p)


