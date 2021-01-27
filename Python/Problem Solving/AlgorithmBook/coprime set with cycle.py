def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
p = [i for i in range(v + 1)]
cycle = False
for _ in range(e):
    a1, b1 = map(int, input().split())
    if find_parent(p, a1) == find_parent(p, b1):
        cycle = True
        break
    union_parent(p, a1, b1)


if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
