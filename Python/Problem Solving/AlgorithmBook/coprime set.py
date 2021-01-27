def find_parent(parent, x):
    if parent[x] != x:
        # return find_parent(parent, parent[x])
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

for _ in range(e):
    a1, b1 = map(int, input().split())
    union_parent(p, a1, b1)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(p, i), end=' ')

print()

print('부모테이블: ', end='')
for i in range(1, v + 1):
    print(p[i], end=' ')

