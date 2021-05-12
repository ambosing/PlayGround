def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
p = [i for i in range(v + 1)]

for _ in range(e):
    t, a, b = map(int, input().split())
    if t == 1:
        if find_parent(p, a) != find_parent(p, b):
            print("NO")
        else:
            print("YES")
    else:
        union_parent(p, a, b)
